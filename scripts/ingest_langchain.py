"""Ingest documents into Postgres+pgvector using Hugging Face sentence-transformers (via LangChain embeddings)."""

import os
import glob
import json
import time
from pathlib import Path

import psycopg2
from psycopg2.extras import Json
from sentence_transformers import SentenceTransformer

DB_URL = os.getenv("DATABASE_URL", "postgresql://moltbook:moltbook@localhost:5432/moltbook")
EMBED_MODEL = os.getenv("HF_EMBED_MODEL", "all-MiniLM-L6-v2")


def connect_db():
    return psycopg2.connect(DB_URL)


def embed_texts(texts, model):
    return model.encode(texts, show_progress_bar=False)


def ingest_folder(folder):
    model = SentenceTransformer(EMBED_MODEL)
    files = sorted(glob.glob(os.path.join(folder, "*.md")))
    conn = connect_db()
    cur = conn.cursor()

    for fpath in files:
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        title = Path(fpath).stem
        embedding = embed_texts([content], model)[0].tolist()
        cur.execute(
            "INSERT INTO documents (title, content, metadata, embedding) VALUES (%s, %s, %s, %s)",
            (title, content, Json({"source": "moltbook_sample", "path": fpath}), embedding),
        )
        conn.commit()
        print(f"Inserted {title}")
    cur.close()
    conn.close()


if __name__ == "__main__":
    import argparse

    p = argparse.ArgumentParser()
    p.add_argument("--folder", default="data/moltbook_samples", help="Folder with docs to ingest")
    args = p.parse_args()
    ingest_folder(args.folder)
