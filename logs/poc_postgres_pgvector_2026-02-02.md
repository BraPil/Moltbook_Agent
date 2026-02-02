# PoC: Postgres + pgvector — 2026-02-02

Project: Brapil Moltbook Agent 1
Date: 2026-02-02

Purpose
Proof-of-Concept to evaluate Postgres + pgvector for retrieval and vector similarity as a baseline for Moltbook RAG workflows.

Scope
- Dataset: 100 real Moltbook documents (sampled).
- Embeddings: Hugging Face sentence-transformers (self-hosted inference).
- Ingestion: LangChain and LlamaIndex ingestion variants will both be used for comparison.
- Systems: Postgres + pgvector (primary PoC);
- Metrics: recall@k, median/p95 latency, ingest throughput (docs/sec), resource usage, and operational friction.

Plan
1. Prepare a sample of 100 Moltbook documents and a small gold set for evaluation.
2. Build an ingestion script for LangChain and one for LlamaIndex to embed and store documents in Postgres+pgvector.
3. Implement simple retrieval queries (semantic similarity, metadata filters, full-text + vector hybrid queries).
4. Run evaluation metrics and record results.
5. Produce a short comparison report with recommendations.

Deliverables
- `docker-compose.yml` for Postgres + pgvector
- Ingestion scripts: `scripts/ingest_langchain.py`, `scripts/ingest_llamaindex.py`
- Evaluation scripts: `scripts/eval_recall_latency.py`
- Results report: `logs/poc_postgres_pgvector_results_2026-02-XX.md`

Status
- PoC created and planned. Ready to begin data sampling and script implementation.

Recorded by
- Agent: GitHub Copilot
- Date: 2026-02-02
