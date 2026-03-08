# ADR-002: File-based JSON storage over database

- **Status**: Accepted
- **Date**: 2026-03-08

## Context

The project needs to store newsletter data scraped by n8n (email content, extracted links, article text from Jina Reader). We evaluated whether to use a database (SQLite, PostgreSQL) or flat JSON files.

## Decision

Store all source data as date-prefixed JSON files in `data/raw/` with the naming convention `YYYY-MM-DD-newsletter-{slug}.json`.

Each file contains a simple structure:
```json
{
  "newsletter": "Newsletter Name",
  "received_at": "2026-03-06T08:30:00Z",
  "links": [
    {"url": "...", "title": "...", "content": "markdown content"}
  ]
}
```

## Arguments for this approach

1. **Inspectable** — files can be read, diffed, and debugged with standard tools (`cat`, `jq`, `diff`)
2. **Version-controllable (optional)** — files live under `data/raw/` on disk and can be committed to git if `.gitignore` is adjusted, but are typically kept local
3. **Zero infrastructure** — no database server to install, configure, or maintain
4. **n8n compatibility** — n8n writes directly to the filesystem via volume mount, no database driver needed
5. **Sufficient at current scale** — typically 5-15 newsletter files per day, glob-based loading is fast enough

## Arguments against

1. **No relational queries** — cross-newsletter searches require loading all files into memory
2. **No indexing** — searching historical content is O(n) over all files
3. **Duplication risk** — in the main generation pipeline (`load_sources.py`), the same link appearing in multiple newsletters is deduplicated at load time, not at storage level; some analysis scripts (e.g., trend detection) intentionally keep duplicates

## Consequences

- Python scripts use `glob.glob()` to discover files by date pattern
- The upcoming vector search feature (#1) will add ChromaDB as a complementary index layer, not replace file storage
- If daily volume exceeds ~50 files or historical queries become frequent, migration to SQLite should be considered
- The flat file approach supports the n8n → filesystem → Claude Code pipeline without additional dependencies
