"""Generate synthetic Moltbook-like documents for PoC sampling.

Creates markdown files under data/moltbook_samples/ named doc_0001.md ... doc_0100.md
Each file contains a title, metadata, and a conversational/narrative content sample.

Run: python3 scripts/generate_synthetic_moltbook.py --count 100
"""

import os
import argparse
from datetime import datetime

SAMPLE_PARAGRAPHS = [
    "Today in Moltbook, local contributors discussed the evolving community practices around collaborative publishing.",
    "An interview-style conversation highlighted changes in moderation and user-led curation across the platform.",
    "Historical archives showed repeated patterns of engagement during milestone events and launches.",
    "Technical notes: improvements to the sync service and caching were discussed to reduce latency for readers.",
    "Opinion pieces considered the impact of algorithmic surfacing on local community culture and norms.",
]


def generate_doc(idx):
    title = f"Moltbook Update #{idx}"
    date = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    content = "\n\n".join(SAMPLE_PARAGRAPHS)
    metadata = f"---\ntitle: {title}\ndate: {date}\nsource: moltbook\n---\n\n"
    return metadata + content


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--outdir", default="data/moltbook_samples", help="Output dir for generated documents")
    parser.add_argument("--count", type=int, default=100, help="Number of documents to generate")
    args = parser.parse_args()

    os.makedirs(args.outdir, exist_ok=True)

    for i in range(1, args.count + 1):
        filename = os.path.join(args.outdir, f"doc_{i:04d}.md")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(generate_doc(i))

    print(f"Generated {args.count} documents in {args.outdir}")


if __name__ == "__main__":
    main()
