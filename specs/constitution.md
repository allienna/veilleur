# Project Constitution

> Non-negotiable principles for Veilleur v1.0.0. Reject any PR that violates these.

## 1. Project Context

Veilleur automates daily LinkedIn tech watch article generation: ingest newsletters, curate sources, generate articles via LLM, edit, and publish to an Astro static site. Single-user tool for Aurelien Allienne. The v1 rebuild replaces Python/n8n/Docker with a unified TypeScript stack on GCP.

## 2. Non-Negotiable Principles

1. **Single language**: All application code is TypeScript. No Python, no shell scripts for business logic.
2. **No silent failures**: Every pipeline step logs status, duration, and errors to Firestore `pipeline_runs`. If it can fail, it must be visible in the dashboard.
3. **Partial success over total failure**: One newsletter/source/step failing must not block others. Ingestion, scraping, and pipeline steps degrade individually.
4. **No Notion dependency**: Draft review and editing happen in the built-in dashboard editor. Notion MCP is removed.
5. **No n8n/Docker/Colima dependency**: Email ingestion is event-driven via CloudFlare Email Workers. Zero Docker in the pipeline.
6. **No Gmail OAuth**: Newsletters arrive at `watch@{domain}` via CloudFlare Email Routing. No OAuth token management.
7. **Secrets never in code**: `GEMINI_API_KEY`, `INGEST_SECRET`, `VEILLEUR_PASSWORD` stored in GCP Secret Manager or Cloud Run env vars. Never committed.
8. **Deterministic orchestration**: Pipeline steps are deterministic TypeScript code. LLM calls are confined to content generation (article writing, fiches, image prompts) — never for control flow or routing.
9. **Idempotent ingestion**: Re-processing the same email or RSS entry must not create duplicate sources. Deduplicate by URL.

## 3. Tech Stack

| Component | Choice | Locked? |
|-----------|--------|---------|
| Language | TypeScript | Locked |
| Full-stack framework | Next.js 15 (App Router) | Locked |
| UI components | shadcn/ui + Tailwind | Locked |
| Database | Firestore (Native mode) | Locked |
| Object storage | Cloud Storage (GCS) | Locked |
| AI (text) | Gemini 2.5 Flash (`@google/genai`) | Locked (Gemini Pro as fallback) |
| AI (images) | Gemini Imagen 4 (`@google/genai`) | Locked |
| Email ingestion | CloudFlare Email Workers | Locked |
| Static site | Astro on CloudFlare Pages | Locked |
| Scheduler | GCP Cloud Scheduler | Locked |
| Monorepo | Turborepo | Locked |
| CI/CD | Cloud Build | Locked |
| Content scraping | Jina Reader (`r.jina.ai`) | Flexible |

## 4. Coding Standards

1. **Monorepo structure**: `apps/dashboard` (Next.js), `apps/email-worker` (CF Worker), `packages/core` (shared logic). All business logic lives in `packages/core`.
2. **Strict TypeScript**: `strict: true` in all tsconfigs. No `any` except at SDK boundaries with explicit casts.
3. **Server Components by default**: Client Components only when interactivity is required (`"use client"` directive).
4. **API routes for mutations**: All writes go through Next.js API routes (`app/api/`), never direct Firestore calls from client.
5. **Design tokens**: navy `#162d60`, amber `#f59f0a`, background `#f8f7f5`. Fonts: Poppins (headings), Work Sans (body). Consistent with existing Astro site.
6. **Conventional commits**: `feat:`, `fix:`, `docs:`, `chore:`, `refactor:`, `test:`.

## 5. Quality Gates

Every PR must pass ALL of these:

- [ ] `tsc --noEmit` passes with zero errors
- [ ] All existing tests pass (`turbo test`)
- [ ] No secrets or API keys in committed code
- [ ] New Firestore collections/fields documented in schema file
- [ ] Pipeline steps log to `pipeline_runs` with status and duration
- [ ] Partial failure handled (one source/newsletter failing does not crash the step)
- [ ] API routes validate input and return structured error responses
- [ ] No direct Firestore writes from client components

## 6. Compliance & Security

1. **Auth**: Email Worker authenticates to API via `INGEST_SECRET` header. Dashboard optionally protected by `VEILLEUR_PASSWORD`.
2. **Transport**: All external calls over HTTPS. Cloud Run enforces HTTPS.
3. **Data**: No PII beyond newsletter content. No user data collection. No analytics tracking.
4. **Dependencies**: Use well-maintained packages only. Pin major versions. Audit with `npm audit` before merge.
5. **Firestore rules**: Deny all external access. Only Cloud Run service account has read/write.
