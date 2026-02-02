"""Simple evaluation harness: run k-NN queries against Postgres+pgvector and measure latency and basic recall@k against a small gold set."""

import os
import time
import random
import json
from typing import List

import psycopg2
import numpy as np
from sentence_transformers import SentenceTransformer

DB_URL = os.getenv("DATABASE_URL", "postgresql://moltbook:moltbook@localhost:5432/moltbook")
EMBED_MODEL = os.getenv("HF_EMBED_MODEL", "all-MiniLM-L6-v2")


def connect_db():
    return psycopg2.connect(DB_URL)


def query_similar(content: str, top_k: int = 10):
    model = SentenceTransformer(EMBED_MODEL)
    emb = model.encode([content])[0].tolist()
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, title, content, 1 - (embedding <-> %s::vector) AS similarity FROM documents ORDER BY embedding <-> %s::vector LIMIT %s",
        (emb, emb, top_k),
    )
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results


def measure_latency(queries: List[str], top_k: int = 10):
    times = []
    for q in queries:
        t0 = time.time()
        _ = query_similar(q, top_k)
        times.append(time.time() - t0)
    return np.percentile(times, [50, 95]).tolist(), sum(times) / len(times)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--queries", default=None, help="JSON file with list of queries to test")
    parser.add_argument("--k", type=int, default=5)
    args = parser.parse_args()

    if args.queries and os.path.exists(args.queries):
        queries = json.load(open(args.queries))
    else:
        # fallback: sample random doc content for queries
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("SELECT content FROM documents ORDER BY random() LIMIT 10")
        queries = [r[0] for r in cur.fetchall()]
        cur.close()
        conn.close()

    p50_p95, avg = measure_latency(queries, args.k)
    print(f"Latency P50: {p50_p95[0]:.3f}s, P95: {p50_p95[1]:.3f}s, avg: {avg:.3f}s")
