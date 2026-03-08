# ADR-004: n8n as workflow orchestrator

- **Status**: Accepted
- **Date**: 2026-03-08

## Context

The project needs an automated pipeline to: monitor a Gmail inbox for newsletters, extract links, scrape content via Jina Reader, and write structured JSON files to disk. We evaluated several orchestration approaches.

## Decision

Use [n8n](https://n8n.io) running in Docker as the workflow orchestrator for email ingestion and data extraction.

The setup is defined in `n8n/docker-compose.yml`. The compose file mounts a host `data` directory (configured as an absolute path) into the container at `/data/veilleur`, and workflows write JSON outputs under `/data/veilleur/raw`, which corresponds to `data/raw/` on the host. The workflow itself is exported as `n8n/workflow-veilleur.json`.

## Arguments for this approach

1. **Visual workflow editor** — non-code pipeline design, easy to debug and modify
2. **Gmail integration built-in** — OAuth2-based email trigger, no custom IMAP code
3. **HTTP nodes for Jina Reader** — direct API calls without custom scripting
4. **File system write** — writes JSON directly to mounted volume, no intermediate service needed
5. **Self-hosted via Docker** — no third-party orchestration SaaS; workflows integrate with external services (Gmail, Jina Reader) while keeping orchestration and local file writes under our control
6. **Workflow as code** — exportable JSON workflow can be version-controlled

## Arguments against

1. **Docker dependency** — requires Docker running locally for the ingestion pipeline
2. **Limited programmatic control** — complex logic is harder to express than in pure code
3. **Single point of failure** — if n8n container stops, no emails are processed
4. **Credential management** — OAuth2 tokens stored in n8n's internal database, not in project config

## Alternatives considered

- **Custom Python script + cron**: full control, but reimplements email polling, error handling, retries
- **Temporal / Airflow**: production-grade orchestration, but massive overkill for a single-user pipeline
- **GitHub Actions**: CI-native but awkward for email monitoring and local file writes
- **Make.com / Zapier**: cloud-hosted alternatives but paid and less control over data

## Consequences

- n8n handles only the ingestion phase (email → JSON files); content generation remains in Claude Code
- The workflow JSON should be re-exported after any manual changes in the n8n UI
- If moving to a multi-user setup (phase 3), n8n would likely be replaced by a proper backend API
- Local Docker setup documented in `docs/n8n-google-cloud-setup.md`
