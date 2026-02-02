# PoC Task: Postgres + pgvector

Project: Brapil Moltbook Agent 1
Status: Not started
Created: 2026-02-02

Purpose
Implement the PoC described in `logs/poc_postgres_pgvector_2026-02-02.md` to evaluate retrieval quality and operational overhead.

Checklist
- [x] Create PoC plan and log file
- [ ] Sample 100 Moltbook documents for ingest
- [ ] Implement LangChain ingestion script
- [ ] Implement LlamaIndex ingestion script
- [ ] Build evaluation scripts for recall@k and latency
- [ ] Run PoC and collect metrics
- [ ] Produce PoC results report and recommend next steps

Owner
- Agent: GitHub Copilot
- Reviewer: Project stakeholder

Notes
- Strictly self-hosted, free-first approach. Use HF sentence-transformers for embeddings.
