import os
import httpx
import json
from datetime import datetime

# Configuration
API_URL = "https://www.moltbook.com/api/v1/posts"
DATA_DIR = "/workspaces/Moltbook_Agent/data/moltbook_samples"
LIMIT = 100

def fetch_posts(limit=100):
    posts = []
    offset = 0
    batch_size = 50
    
    print(f"Fetching {limit} posts from {API_URL}...")
    
    while len(posts) < limit:
        remaining = limit - len(posts)
        current_batch = min(batch_size, remaining)
        
        try:
            response = httpx.get(
                API_URL, 
                params={"limit": current_batch, "offset": offset},
                timeout=30.0
            )
            response.raise_for_status()
            data = response.json()
            
            if not data.get("success"):
                print(f"API Error: {data.get('error', 'Unknown error')}")
                break
                
            batch_posts = data.get("posts", [])
            if not batch_posts:
                break
                
            posts.extend(batch_posts)
            offset += len(batch_posts)
            print(f"Fetched {len(posts)}/{limit} posts...")
            
            if not data.get("has_more"):
                break
                
        except Exception as e:
            print(f"Request failed: {e}")
            break
            
    return posts[:limit]

def save_to_markdown(posts):
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    
    # Clean existing files
    for f in os.listdir(DATA_DIR):
        if f.endswith(".md"):
            os.remove(os.path.join(DATA_DIR, f))
    
    print(f"Saving {len(posts)} posts to {DATA_DIR}...")
    
    for i, post in enumerate(posts):
        filename = f"doc_{str(i+1).zfill(4)}.md"
        filepath = os.path.join(DATA_DIR, filename)
        
        # Meta data
        content = "---\n"
        content += f"id: {post.get('id')}\n"
        content += f"title: {json.dumps(post.get('title'))}\n"
        content += f"author: {post.get('author', {}).get('name')}\n"
        content += f"submolt: {post.get('submolt', {}).get('name')}\n"
        content += f"created_at: {post.get('created_at')}\n"
        content += f"post_url: https://www.moltbook.com/post/{post.get('id')}\n"
        content += "source: moltbook_real\n"
        content += "---\n\n"
        
        # Body
        post_content = post.get("content", "")
        if post_content:
            content += post_content
        else:
            content += "[No content]"
            
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
            
    print("Done.")

if __name__ == "__main__":
    real_posts = fetch_posts(LIMIT)
    if real_posts:
        save_to_markdown(real_posts)
    else:
        print("No posts fetched.")
