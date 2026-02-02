# MCP, Tool, and Reference Index

Project: Brapil Moltbook Agent 1

Purpose
Track all MCPs, tools, and reference materials required for the prime directive, including access status and version.

| Category | Name | Description | Source | Version | Access status | Last reviewed |
| --- | --- | --- | --- | --- | --- | --- |
| Framework | LangChain | Orchestration, prompts, memory, RAG pipelines; Python and JS. | https://github.com/langchain/langchain | v0.x | Available | 2026-02-02 |
| Framework | LlamaIndex | Document indexing and retrieval (RAG support). | https://gpt-index.readthedocs.io/ | v0.x | Available | 2026-02-02 |
| Vector DB | Pinecone | Managed vector database with easy scale. | https://www.pinecone.io | n/a | Evaluating access | 2026-02-02 |
| Vector DB | Qdrant | Open-source vector DB, good for on-prem or cloud self-hosting. | https://qdrant.tech | n/a | Evaluating access | 2026-02-02 |
| Observability | OpenTelemetry + Grafana | Telemetry, metrics, and dashboards for observability. | https://opentelemetry.io, https://grafana.com | n/a | Evaluating | 2026-02-02 |
| Observability | Loki | Log aggregation integrated with Grafana for searchable, selectable logs. | https://grafana.com/oss/loki | n/a | Evaluating (self-host preferred) | 2026-02-02 |
| Observability | Sentry | Error and performance monitoring for applications and SDKs. | https://sentry.io | n/a | Evaluating (self-host or cloud) | 2026-02-02 |
| MCP | Google Vertex AI / Gemini 3 | Primary context model. Integrate via Vertex AI SDK and IAM. | https://cloud.google.com/vertex-ai | Gemini 3 | Requires access & approval | 2026-02-02 |
| MCP | Opus 4.5 | Primary code generation model. Integrate via provider API and strict test harnessing. | Provider docs | Opus 4.5 | Requires access | 2026-02-02 |
| Tooling | Docker / Kubernetes | Containerization and orchestration for running services and PoCs. | https://docker.com, https://kubernetes.io | n/a | Available | 2026-02-02 |
| Logging | Loki / ELK | Logging stack options for searchable, auditable logs. | https://grafana.com/oss/loki, https://www.elastic.co | n/a | Evaluating | 2026-02-02 |

Notes
- These entries are initial; details like versions, access contacts, and licenses will be filled as research continues.
