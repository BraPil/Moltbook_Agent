# Tool / MCP / SDK Research Task

Project: Brapil Moltbook Agent 1
Status: In progress
Created: 2026-02-02
Last updated: 2026-02-02

Purpose
Discover, explore, debate, and evaluate candidate tools, MCPs, SDKs, and other resources to select an optimal technology stack for accomplishing the prime directive.

Progress summary
- Initial candidate list created and added to `indexes/mcp_tool_reference_index.md`.
- `logs/tool_research_results_2026-02-02.md` added with focused recommendations.
- Clarifying answers recorded: prefer self-hosted/free options; dataset scale: as-needed to accomplish the prime directive; query patterns: to be explored during research; KG features: plan for future support; no compliance constraints at present.
- Next: run a scored comparison between Postgres+pgvector and Weaviate and prepare a small PoC plan to empirically compare recall/latency/operational overhead.
- Action: PoC for Postgres+pgvector initiated (sample 100 docs; LangChain + LlamaIndex ingestion variants).

Scope
- Identify candidates for agent runtime and orchestration, context management, retrieval tools, observability, logging, and data governance.
- Evaluate integrations with Opus 4.5 (for code generation) and Gemini 3 (for context) and other MCPs we might use.
- Consider privacy, security, cost, scalability, versioning, and license constraints.

Selection criteria (initial)
- Alignment with prime directive and governance protocols
- Reproducibility, auditability and logging support
- Data privacy and security practices
- Compatibility with Opus 4.5 and Gemini 3 workflows
- Community support and maintainability
- Cost and licensing model

Deliverables
- A prioritized list of candidate tools and MCPs, with brief pros/cons and integration notes
- A recommended stack and implementation plan (high-level)
- A small PoC plan for the top candidate(s) with success criteria

Next steps
- Populate the candidate list in `indexes/mcp_tool_reference_index.md` as items are researched
- Run focused research per candidate and log findings to the research task file
- Present findings and recommendation for approval

Owner
- Agent: GitHub Copilot (initial research)
- Review: Project stakeholder
