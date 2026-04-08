# Veilleur v1.0.0 — Feature Roadmap

**Generated from**: PRD.md
**Last updated**: 2026-04-08
**Status**: Draft

## Features

### F-001: monorepo-scaffold
**Summary**: Turborepo monorepo with apps/dashboard (Next.js 15), apps/email-worker (CF Worker), and packages/core — all wired with shared TypeScript config.
**PRD sections**: Architecture (§5), Phase 1
**Depends on**: None
**Delivers**: Working monorepo, `turbo build` passes, empty Next.js app runs locally, shared types importable from core
**Estimated size**: S
**Status**: In Progress

### F-002: firestore-schema
**Summary**: Firestore client setup with typed collections (sources, newsletters, articles, pipeline_runs, metrics) and seed data utilities.
**PRD sections**: Architecture (§5), FR-3, FR-4, FR-5, FR-7, FR-12
**Depends on**: F-001
**Delivers**: Firestore client in packages/core, TypeScript types for all collections, emulator config for local dev
**Estimated size**: S
**Status**: Not started

### F-003: core-logic-port
**Summary**: Port source filtering, theme detection, and trend detection from Python to TypeScript in packages/core with tests.
**PRD sections**: FR-4, FR-5, Phase 1
**Depends on**: F-002
**Delivers**: `filterSources()`, `detectThemes()`, `detectTrends()` functions with unit tests, matching Python behavior
**Estimated size**: M
**Status**: Not started

### F-004: dashboard-shell
**Summary**: Next.js 15 App Router layout with sidebar navigation, header, and design tokens (navy/amber theme matching Astro site).
**PRD sections**: Phase 2, Design conventions
**Depends on**: F-001
**Delivers**: Dashboard shell with shadcn/ui, sidebar routes (Sources, Pipeline, Editor, Metrics, Newsletters), responsive layout
**Estimated size**: S
**Status**: Not started

### F-005: source-browser
**Summary**: Source browser page with date picker, theme-grouped source list, trend clusters, and source curation (select/deselect/further reading).
**PRD sections**: FR-4, FR-5, FR-6, Phase 2
**Depends on**: F-003, F-004
**Delivers**: `/sources` page, API routes (`/api/sources`, `/api/trends`), manual link addition, curation persisted to Firestore
**Estimated size**: M
**Status**: Not started

### F-006: newsletter-registry
**Summary**: Newsletter CRUD with active/inactive toggle, email vs RSS type, and last-fetched tracking.
**PRD sections**: FR-3, FR-2, Phase 2
**Depends on**: F-004, F-002
**Delivers**: `/newsletters` page, API routes (`/api/newsletters`), support for email and RSS source types
**Estimated size**: S
**Status**: Not started

### F-007: ingest-api
**Summary**: `/api/ingest` webhook endpoint authenticated via shared secret, receiving structured source payloads and writing to Firestore with URL deduplication.
**PRD sections**: FR-1, FR-2, Phase 3
**Depends on**: F-002
**Delivers**: Authenticated ingest endpoint, idempotent source creation, RSS fetch support
**Estimated size**: S
**Status**: Not started

### F-008: email-worker
**Summary**: CloudFlare Email Worker that parses newsletters, extracts links, scrapes via Jina Reader, and POSTs to ingest API.
**PRD sections**: FR-1, Phase 3
**Depends on**: F-007
**Delivers**: `apps/email-worker` deployed to CloudFlare, email parsing, parallel Jina scraping, unknown sender forwarding
**Estimated size**: M
**Status**: Not started

### F-009: pipeline-orchestrator
**Summary**: Step-by-step pipeline runner with per-step logging to Firestore, supporting full or individual step execution.
**PRD sections**: FR-7, Phase 4
**Depends on**: F-003
**Delivers**: Pipeline runner in packages/core, steps logged to `pipeline_runs`, trigger via API, partial failure handling
**Estimated size**: M
**Status**: Not started

### F-010: gemini-generation
**Summary**: Article generation via Gemini 2.5 Flash — narrative selection, article writing, fiches, LinkedIn post, image prompt, and header image via Imagen.
**PRD sections**: FR-7, FR-14, Phase 4
**Depends on**: F-009
**Delivers**: Gemini client in packages/core, generation pipeline steps, writing guide as system instruction, image generation
**Estimated size**: M
**Status**: Not started

### F-011: pipeline-monitor
**Summary**: Dashboard page showing pipeline job history with SSE-powered real-time progress and step-level detail with logs.
**PRD sections**: FR-8, FR-11, Phase 4
**Depends on**: F-009, F-004
**Delivers**: `/pipeline` page, SSE endpoint, step timeline with status icons, job history table with filtering
**Estimated size**: M
**Status**: Not started

### F-012: draft-editor
**Summary**: Split-view markdown editor with live preview for article, LinkedIn post, and image prompt editing with status workflow.
**PRD sections**: FR-9, Phase 5
**Depends on**: F-010, F-004
**Delivers**: `/editor` page, markdown editor + preview, edits persisted to Firestore, draft → reviewed → published workflow
**Estimated size**: M
**Status**: Not started

### F-013: publish-action
**Summary**: Publish button that writes article + fiches + image to the Astro site repo, commits, and pushes to trigger CloudFlare Pages deploy.
**PRD sections**: FR-10, Phase 5
**Depends on**: F-012
**Delivers**: Publish API route, git operations via simple-git, status update to "published"
**Estimated size**: S
**Status**: Not started

### F-014: metrics-dashboard
**Summary**: LinkedIn engagement recording, trend charts (Recharts), and insight cards with theme-based recommendations.
**PRD sections**: FR-12, FR-13, Phase 6
**Depends on**: F-004, F-002
**Delivers**: `/metrics` page, engagement recording form, line/bar charts, insight cards, articles-without-metrics highlight
**Estimated size**: M
**Status**: Not started

### F-015: cloud-scheduler
**Summary**: Three daily Cloud Scheduler jobs triggering the pipeline at scheduled times with fallback publish.
**PRD sections**: Phase 6, Goals (autonomy)
**Depends on**: F-009, F-013
**Delivers**: Cloud Scheduler config, 20h pipeline trigger, 23h fallback publish, warm-up ping
**Estimated size**: S
**Status**: Not started

### F-016: astro-migration
**Summary**: Move Astro site from GitHub Pages to CloudFlare Pages with custom domain and Firestore-based data export.
**PRD sections**: Phase 7
**Depends on**: F-002
**Delivers**: CloudFlare Pages deployment, custom domain, updated build pipeline exporting from Firestore
**Estimated size**: S
**Status**: Not started

### F-017: cloud-deployment
**Summary**: Dockerfile, Cloud Build trigger, and Cloud Run service config for the Next.js dashboard with end-to-end testing.
**PRD sections**: Phase 8
**Depends on**: F-011, F-012, F-014
**Delivers**: Production Dockerfile, Cloud Build CI/CD, Cloud Run service, full daily cycle test
**Estimated size**: M
**Status**: Not started

### F-018: cleanup-migration
**Summary**: Remove Python scripts, n8n/, launchd/ — migrate metrics, articles, and fiches data from v0.x to Firestore.
**PRD sections**: Phase 9
**Depends on**: F-017
**Delivers**: v0.x code removed, data migrated, CLAUDE.md updated for v1 architecture
**Estimated size**: S
**Status**: Not started

## Dependency Graph

```
F-001 (scaffold)
├── F-002 (firestore) ──┬── F-003 (core logic) ──┬── F-005 (source browser)
│                       │                         └── F-009 (pipeline) ── F-010 (gemini) ── F-012 (editor) ── F-013 (publish) ── F-015 (scheduler)
│                       ├── F-006 (newsletters)
│                       ├── F-007 (ingest API) ── F-008 (email worker)
│                       ├── F-014 (metrics)
│                       └── F-016 (astro migration)
├── F-004 (dashboard) ──┬── F-005
│                       ├── F-006
│                       ├── F-011 (monitor)
│                       └── F-014
│
F-017 (cloud deploy) ── depends on F-011, F-012, F-014
└── F-018 (cleanup)
```

## Milestones

### M1: Foundation (F-001 → F-003)
Monorepo running, Firestore connected, core business logic ported and tested. Ready to build UI.

### M2: Dashboard MVP (F-004 → F-006)
Dashboard shell with source browser, curation, and newsletter management. First usable UI.

### M3: Ingestion (F-007 → F-008)
Email-driven ingestion pipeline replaces n8n. Newsletters flow in automatically.

### M4: Generation (F-009 → F-011)
Full article generation pipeline with Gemini, real-time monitoring. Core value proposition working.

### M5: Edit & Publish (F-012 → F-013)
Draft editing and one-click publish. Complete authoring workflow.

### M6: Metrics & Automation (F-014 → F-015)
Engagement tracking and scheduled daily runs. Fully autonomous operation.

### M7: Ship (F-016 → F-018)
Cloud deployment, Astro migration, v0.x cleanup. Production-ready.
