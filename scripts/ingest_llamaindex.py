"""Ingest documents using LlamaIndex to produce embeddings, then store into Postgres+pgvector (same table)."""

import os
import glob
from pathlib import Path
import json

import psycopg2
from psycopg2.extras import Json
from llama_index import SimpleDirectoryReader, ServiceContext, GPTVectorStoreIndex
from llama_index.embeddings import HuggingFaceEmbedding

DB_URL = os.getenv("DATABASE_URL", "postgresql://moltbook:moltbook@localhost:5432/moltbook")
EMBED_MODEL = os.getenv("HF_EMBED_MODEL", "all-MiniLM-L6-v2")


def connect_db():
    return psycopg2.connect(DB_URL)


def ingest_folder_with_llamaindex(folder):
    # Use LlamaIndex's Hugging Face wrapper to get embeddings
    hf = HuggingFaceEmbedding(model_name=EMBED_MODEL)
    files = sorted(glob.glob(os.path.join(folder, "*.md")))
    conn = connect_db()
    cur = conn.cursor()

    for fpath in files:
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        title = Path(fpath).stem
        emb = hf._get_embeddings(content)
        cur.execute(
            "INSERT INTO documents (title, content, metadata, embedding) VALUES (%s, %s, %s, %s)",
            (title, content, Json({"source": "moltbook_sample", "path": fpath}), emb),
        )
        conn.commit()
        print(f"Inserted {title} via LlamaIndex embeddings")

    cur.close()
    conn.close()


if __name__ == "__main__":
    import argparse

    p = argparse.ArgumentParser()
    p.add_argument("--folder", default="data/moltbook_samples", help="Folder with docs to ingest")
    args = p.parse_args()
    ingest_folder_with_llamaindex(args.folder)
