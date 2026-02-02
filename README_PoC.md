PoC: Postgres + pgvector (v0.1)

Quick start
1. Start Postgres (docker-compose):
   - cd infra && docker-compose up -d
2. Install pgvector in the Postgres image if not present.
3. Run DB setup script:
   - ./scripts/setup_db.sh
4. Generate sample documents (synthetic placeholders):
   - python3 scripts/generate_synthetic_moltbook.py --count 100
   - (Replace with real Moltbook samples by placing files in data/moltbook_samples/)
5. Ingest with LangChain variant:
   - python3 scripts/ingest_langchain.py --folder data/moltbook_samples
6. Ingest with LlamaIndex variant (will insert duplicates unless table cleared):
   - python3 scripts/ingest_llamaindex.py --folder data/moltbook_samples
7. Run evaluation:
   - python3 scripts/eval_recall_latency.py

Notes
- These scripts use Hugging Face sentence-transformers by default. Install dependencies via requirements.txt.
- Currently uses synthetic placeholder documents if real Moltbook content isn't provided. Replace with real data by adding files to data/moltbook_samples and re-ingesting.
