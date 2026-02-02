# Moltbook API Discovery Log — 2026-02-02

Project: Brapil Moltbook Agent 1
Date: 2026-02-02
Research Topic: Moltbook API and Programmatic Retrieval

## Summary
Successfully identified the Moltbook API structure, official SDK, and public endpoints for retrieving real post content.

## Findings

### Official API Details
- **Base URL**: `https://www.moltbook.com/api/v1`
- **Documentation (internal reference)**: `https://www.moltbook.com/skill.md` (as referenced in API index metadata)
- **Authentication**: `Authorization: Bearer YOUR_API_KEY` (required for write actions/registration/claimed status)

### Public Programmatic Endpoints (No API Key Required for GET)
- **Global Feed**: `GET https://www.moltbook.com/api/v1/posts`
- **Submolt Feed**: `GET https://www.moltbook.com/api/v1/posts?submolt={name}`
- **Submolt List**: `GET https://www.moltbook.com/api/v1/submolts`
- **Single Post**: `GET https://www.moltbook.com/api/v1/posts/{id}`
- **Search**: `GET https://www.moltbook.com/api/v1/search?q={query}` (verified via SDK code, needs confirmation for public access)

### Official SDK & Packages
- **NPM Package**: `moltbook` (v1.1.0)
- **GitHub Repository**: [wong2/moltbook-ts](https://github.com/wong2/moltbook-ts)
- **Other Packages**:
  - `moltbook-http-mcp`: MCP server for Moltbook operations.
  - `@moltcraft/moltbook-mcp`: Advanced MCP with engagement tracking.

### Developer & Community Info
- **Founder**: [@mattprd](https://x.com/mattprd)
- **Project Account**: [@moltbook](https://x.com/moltbook)
- **Developer Gateway**: `https://www.moltbook.com/developers/apply`

## Validation
- `curl -s "https://www.moltbook.com/api/v1/posts?limit=5"`: Successfully returned 5 real posts in JSON format.
- `curl -s "https://www.moltbook.com/api/v1/submolts"`: Successfully returned list of submolts.

## Next Steps
- Integrate real data retrieval into `scripts/ingest_langchain.py`.
- Replace `data/moltbook_samples` with real JSON files or a direct API ingestion pipeline.
- Evaluate the `moltbook-http-mcp` for agent-driven interactions.
