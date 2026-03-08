# ADR-001: Keep Python over Go for scripting layer

- **Status**: Accepted
- **Date**: 2026-03-08
- **Context trigger**: Article ["Go is the Best Language for AI Agents"](https://getbruin.com/blog/go-is-the-best-language-for-agents/) by Bruin Data

## Context

The project uses Python scripts (~600 LOC) for data processing: loading JSON sources, filtering, and reading content. With the upcoming vector search feature (#1, ChromaDB), we evaluated whether migrating to Go would be a better long-term choice, especially given claims that Go is better suited for LLM-generated code.

## Arguments for Go

The Bruin article makes the following claims:

1. **Static typing helps agents self-correct** — compile errors give LLMs a feedback loop to fix their own code
2. **Standardized tooling** — `gofmt`, `go test`, `go build` are built-in, no ecosystem fragmentation
3. **Simplicity** — Go is easy to read, reducing risk of LLM-generated "magic" code
4. **Cross-platform binaries** — trivial multi-OS builds
5. **"Agents produce valid Go 95% of the time"** — though the author admits: *"I have absolutely no data whatsoever on this... treat this more as vibes"*

These arguments are strongest for **building production CLI tools and agent infrastructure**, which is the author's use case (Bruin CLI).

## Arguments for staying with Python

1. **Scale doesn't justify it** — ~600 lines of JSON filtering/processing scripts. Type safety concerns are minimal at this scale.
2. **ChromaDB is Python-native** — the vector search feature (#1) requires ChromaDB (or equivalent), which is zero-config in Python. A Go migration would force a different vector DB or add a service dependency.
3. **AI/ML ecosystem** — embedding models, NLP libraries, and AI SDKs (Claude, Voyage) have first-class Python support. Go equivalents are either missing or require HTTP wrappers.
4. **Verbosity trade-off** — Go's explicit error handling and struct definitions would roughly double the codebase size for the same functionality.
5. **Python tooling is mature enough** — `ruff` + `pytest` provide standardized linting and testing, addressing the "fragmentation" argument.
6. **Scripts are called by Claude Code** — they read files, filter, and output JSON to stdout. They're not long-running services where Go's concurrency and performance advantages matter.

## Decision

Keep Python for the scripting and data processing layer.

## Consequences

- Python remains the single language for scripts, vector search, and AI integrations
- If a SaaS backend is built (phase 3), Go or TypeScript should be re-evaluated for the API layer where Go's strengths (performance, binaries, concurrency) would be relevant
- This decision should be revisited if the scripting layer grows significantly in complexity or if we need cross-platform distribution
