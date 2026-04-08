# Veilleur v1.0.0 — Product Requirements Document

**Last updated**: 2026-04-08
**Status**: Draft
**Previous version**: v0.3.0 (Python pipeline with n8n ingestion)

## 1. Overview

### Problem Statement

The current veilleur pipeline (v0.x) relies on n8n (Docker + Colima) to scrape newsletters from Gmail. OAuth tokens expire regularly, n8n flows break silently, and debugging requires navigating a visual workflow editor. Article review happens via Notion MCP, adding another fragile integration point. The pipeline mixes Python scripts, Claude CLI subprocesses, launchd plists, and Docker — too many moving parts for a single-user tool.

### Goals & Success Metrics

| Goal | Metric |
|------|--------|
| Reliable ingestion | Event-driven email processing; zero n8n/Docker/Gmail dependency |
| Self-service workflow | Full article lifecycle (ingest → curate → generate → edit → publish) from a single dashboard |
| Remove Notion | Draft review happens in the front-end editor |
| Maintain autonomy | Daily pipeline runs unattended at 20h with fallback publish at 23h |
| Clean architecture | Single language (TypeScript), cloud-native, ~$1.25/month total cost |

### Target Users

| Persona | Description | Primary needs |
|---------|-------------|---------------|
| Aurélien (sole user) | Engineering Director & GenAI Architect, daily LinkedIn author | Reliable daily pipeline, fast source curation, draft editing, metrics visibility |

## 2. User Stories

### Ingestion
- As a user, I want newsletters received at a custom email address and processed automatically
- As a user, I want to add/remove newsletter sources from the dashboard
- As a user, I want to add a manual URL to include articles found outside newsletters

### Source Curation
- As a user, I want to browse today's sources grouped by theme
- As a user, I want to see trend clusters (topics hot across multiple newsletters)
- As a user, I want to select/deselect sources for the article

### Article Generation
- As a user, I want to trigger article generation from the dashboard
- As a user, I want to see generation progress in real time (step-by-step with logs)
- As a user, I want the pipeline to run automatically at 20h and publish by 23h if I don't review

### Draft Editing
- As a user, I want to edit the generated article in a markdown editor with live preview
- As a user, I want to review the LinkedIn post text and image prompt alongside the article
- As a user, I want a "publish" button that commits to git and triggers the Astro deploy

### Pipeline Monitoring
- As a user, I want to see job history with status per step
- As a user, I want to read logs for any failed step

### Metrics
- As a user, I want to record LinkedIn engagement from the dashboard
- As a user, I want charts showing engagement trends over time and by theme
- As a user, I want insights (top themes, recommendations) to guide future articles

## 3. Functional Requirements

### Ingestion

#### FR-1: CloudFlare Email Worker
Receive newsletters at a custom domain email address. A CloudFlare Email Worker parses the email, extracts links, scrapes content via Jina Reader, and POSTs structured data to the Cloud Run API.
**Acceptance criteria**:
- [ ] Email Routing configured for `watch@{domain}` on CloudFlare
- [ ] Worker matches incoming emails against known newsletter senders
- [ ] Links extracted from HTML email body
- [ ] Content scraped via Jina Reader (parallel, with timeout)
- [ ] Structured payload POSTed to `/api/ingest` with auth secret
- [ ] Per-newsletter failure does not block others
- [ ] Unknown senders forwarded to fallback inbox

#### FR-2: RSS feed support
For newsletters offering RSS, fetch directly without email.
**Acceptance criteria**:
- [ ] Newsletter config supports `type: email | rss` with `rss_url` field
- [ ] RSS entries converted to the same source format
- [ ] Deduplication if a source appears in both email and RSS

#### FR-3: Newsletter registry
Store newsletter sources in Firestore with metadata and fetch configuration.
**Acceptance criteria**:
- [ ] CRUD via API and dashboard
- [ ] Toggle active/inactive per newsletter
- [ ] Track `last_fetched_at` per newsletter

### Source Management

#### FR-4: Source browser
Display sources for a given date, grouped by theme, with trend clusters.
**Acceptance criteria**:
- [ ] Sources loaded from Firestore `sources` collection
- [ ] Trend detection via graph-based clustering (ported from `detect_trends.py`)
- [ ] Filterable by theme, newsletter, trend membership

#### FR-5: Source curation
Toggle source selection for article inclusion.
**Acceptance criteria**:
- [ ] Mark sources as "selected", "further reading", or "excluded"
- [ ] Persist curation status in Firestore
- [ ] Pass curated selection to the generation step

#### FR-6: Manual link addition
Add a URL not from any newsletter.
**Acceptance criteria**:
- [ ] Fetches content via Jina Reader
- [ ] Creates source document in Firestore
- [ ] Appears in source browser immediately

### Article Generation & Editing

#### FR-7: Pipeline orchestration
Step-by-step pipeline runner with logging per step.
**Acceptance criteria**:
- [ ] Steps: ingest → filter → trends → generate → fiches → image → index → publish
- [ ] Each step logged to Firestore `pipeline_runs` with status, duration, output
- [ ] Can trigger full pipeline or individual steps
- [ ] Generation uses Gemini 2.5 Flash API (deterministic orchestration, LLM for writing only)

#### FR-8: Real-time pipeline progress
Stream pipeline logs to the dashboard.
**Acceptance criteria**:
- [ ] SSE endpoint for live log streaming
- [ ] Dashboard shows step timeline with status icons updating in real time

#### FR-9: Draft editor
Markdown editor with live preview for article review.
**Acceptance criteria**:
- [ ] Split view: markdown editor + rendered preview
- [ ] Edits saved via API (persisted to Firestore)
- [ ] LinkedIn post and image prompt editable alongside
- [ ] Status workflow: draft → reviewed → published

#### FR-10: Publish action
Write article + fiches + image to Astro site repo and push.
**Acceptance criteria**:
- [ ] Writes to `site/src/content/articles/`, `site/src/content/fiches/`, `site/public/images/`
- [ ] Creates git commit with conventional message
- [ ] Pushes to main, triggering CloudFlare Pages deploy
- [ ] Updates article status to "published"

### Pipeline Monitoring

#### FR-11: Job history dashboard
List past pipeline runs with filtering.
**Acceptance criteria**:
- [ ] Table: date, status, steps completed, duration, errors
- [ ] Filter by date range, status (success/failed/running)
- [ ] Click through to step-level detail with logs

### Metrics

#### FR-12: Metrics recording
Record LinkedIn engagement via dashboard.
**Acceptance criteria**:
- [ ] Input: likes, comments, reposts, impressions
- [ ] Engagement score auto-computed (likes + comments×3 + reposts×5)
- [ ] Upsert by date

#### FR-13: Metrics dashboard
Visualize engagement trends.
**Acceptance criteria**:
- [ ] Line chart: engagement over time
- [ ] Bar chart: average engagement by theme
- [ ] Insight cards: top themes, recommendations, trend direction
- [ ] Highlight articles without recorded metrics

### Media

#### FR-14: Image generation
Dashboard button to generate header image via Gemini Imagen.
**Acceptance criteria**:
- [ ] Uses same `@google/genai` SDK as text generation
- [ ] Status and logs visible in pipeline monitor

---

### Nice-to-Have (post-MVP)

- **FR-15**: Drag-and-drop source ordering in curation view
- **FR-16**: Side-by-side diff between draft versions
- **FR-17**: Mobile-responsive dashboard
- **FR-18**: Instagram carousel generation (Playwright on Cloud Run)
- **FR-19**: NotebookLM podcast generation (needs cloud-compatible approach)

## 4. Non-Functional Requirements

### Performance
- Dashboard pages load under 2s (includes Cloud Run cold start mitigation)
- Ingestion completes within 5 minutes for 20 newsletters
- API responses under 200ms for read endpoints (after warm-up)

### Reliability
- Pipeline failures logged and visible in dashboard; no silent breakage
- Graceful degradation: if one step fails, subsequent independent steps can still run
- Cloud Run auto-restarts on crash

### Scalability
- Single-user. Cloud Run scales to zero when idle, scales to 1 on request.
- Firestore handles all concurrency natively.

## 5. Architecture & Tech Stack

### System Architecture

```
┌─────────────────────────────┐
│  CloudFlare Email Workers   │  watch@{domain}
│  (newsletter ingestion)     │
└───────────┬─────────────────┘
            │ POST /api/ingest
┌───────────▼─────────────────┐
│  GCP Cloud Run              │
│  Next.js 15 (App Router)    │  Dashboard + API routes
│  ┌────────────────────────┐ │
│  │  packages/core          │ │  Shared TypeScript modules
│  │  (sources, trends,      │ │  (ported from Python scripts)
│  │   generation, metrics,  │ │
│  │   search)               │ │
│  └────────────────────────┘ │
└──┬────┬────┬───────────────┘
   │    │    │
   │    │    └── Gemini API (@google/genai)
   │    │        • 2.5 Flash (article generation)
   │    │        • Imagen 4 (header images)
   │    │        • Embeddings (vector search)
   │    │
   │    └─────── Cloud Storage (raw content, images)
   │
   └──────────── Firestore (database + vector search)

GCP Cloud Scheduler ──→ Cloud Run (3 daily cron triggers)

┌─────────────────────────────┐
│  CloudFlare Pages           │  Astro static site
│  (deploys on git push)      │  Custom domain
└─────────────────────────────┘
```

### Tech Stack

| Component | Choice | Rationale |
|-----------|--------|-----------|
| Language | TypeScript (everywhere) | Single language for Cloud Run, CloudFlare Workers, and frontend |
| Full-stack framework | Next.js 15 (App Router) | Dashboard + API routes in one container; Server Components for fast loads |
| UI components | shadcn/ui + Tailwind | Same design tokens as Astro site (navy/amber) |
| Database | Firestore (Native mode) | Free tier (1GB, 50K reads/day); vector search replaces ChromaDB |
| Object storage | Cloud Storage (GCS) | Free tier (5GB); stores raw content and images |
| AI (text) | Gemini 2.5 Flash | ~$0.004/article; same SDK as image generation; Gemini Pro as fallback |
| AI (images) | Gemini Imagen 4 | Already in use; same `@google/genai` SDK |
| Email ingestion | CloudFlare Email Workers | Event-driven; zero Gmail/OAuth dependency |
| Static site | Astro on CloudFlare Pages | Replaces GitHub Pages; faster CDN, custom domain |
| Scheduler | GCP Cloud Scheduler | 3 daily HTTP triggers to Cloud Run ($0.30/month) |
| Domain | CloudFlare Registrar | At-cost pricing; integrated with Pages/Email/Workers |
| Monorepo | Turborepo | Manages dashboard, email-worker, site, and shared core package |
| CI/CD | Cloud Build | 120 free min/day; builds and deploys to Cloud Run on push |

### Integrations

| System | Purpose | Interface |
|--------|---------|-----------|
| Gemini API | Text generation + images + embeddings | `@google/genai` SDK |
| Jina Reader | Scrape article content | HTTPS (`r.jina.ai/{url}`) |
| CloudFlare Email | Receive newsletters | Email Workers (TypeScript) |
| GitHub (git) | Publishing to Astro site | `simple-git` npm package |

## 6. Error Handling

### User-Facing Errors
- Pipeline step failures shown with red status + expandable error log in dashboard
- Ingestion failures per-newsletter shown individually (partial success is OK)
- Toast notifications for action results (save, publish, trigger)

### Internal Error Patterns
- All pipeline steps log to Firestore `pipeline_runs` (structured logs)
- Cloud Run logs to Cloud Logging (free)

### Graceful Degradation
- Email Worker failure → emails queue in CloudFlare; retry on next delivery
- Gemini API timeout → step marked failed, user can retry from dashboard
- One newsletter failure does not block others

## 7. Security & Compliance

### Authentication & Authorization
- Single-user: optional password protection via `VEILLEUR_PASSWORD` env var
- Email Worker → API authenticated via shared secret header

### Data Privacy
- Gemini API key stored in GCP Secret Manager (or Cloud Run env vars)
- No PII beyond newsletter content; no compliance requirements

## 8. Configuration

### Environment Variables

| Variable | Purpose | Required |
|----------|---------|----------|
| `GEMINI_API_KEY` | Text generation + image generation | Yes |
| `INGEST_SECRET` | Email Worker → API authentication | Yes |
| `VEILLEUR_PASSWORD` | Optional dashboard password | No |
| `GCP_PROJECT_ID` | Firestore + Cloud Storage project | Yes |

### External Services
- CloudFlare: domain + email routing + Pages (configured via dashboard)
- GCP: Firestore + Cloud Storage + Cloud Run + Cloud Scheduler (configured via `gcloud`)
- Gemini: API key

## 9. Implementation Sequence

### Phase 1: Foundation
- Turborepo monorepo scaffold (`apps/dashboard`, `apps/email-worker`, `packages/core`)
- Port source filtering, theme detection, trend detection from Python to TypeScript
- Firestore setup with collections schema
- Basic integration tests for core logic

### Phase 2: Dashboard + Source Browser
- Next.js app with layout shell (sidebar, header)
- Source browser page (date picker, theme groups, trend clusters, curation)
- API routes: `/api/sources`, `/api/trends`, `/api/newsletters`
- Newsletter registry CRUD

### Phase 3: Email Ingestion
- CloudFlare Email Worker (email parsing, link extraction, Jina scraping)
- Email Routing configuration on custom domain
- `/api/ingest` webhook endpoint
- Retire n8n

### Phase 4: Article Generation
- Pipeline orchestrator with per-step logging
- Gemini 2.5 Flash API integration (narrative selection + article + fiches)
- Gemini Imagen integration (header image)
- SSE endpoint for real-time progress
- Pipeline monitor page in dashboard

### Phase 5: Draft Editor + Publish
- Markdown editor with live preview
- Article/post/image-prompt editing
- Status workflow (draft → reviewed → published)
- Publish action (git commit + push → CloudFlare Pages deploy)

### Phase 6: Metrics + Scheduler
- Metrics recording and charts (Recharts)
- Engagement insights
- Cloud Scheduler integration (3 daily jobs)

### Phase 7: Astro Migration
- Move Astro site to CloudFlare Pages
- Custom domain configuration
- Update build pipeline to export data from Firestore

### Phase 8: Cloud Deployment
- Dockerfile for Next.js dashboard
- Cloud Build trigger on push
- Cloud Run service configuration
- End-to-end testing of full daily cycle

### Phase 9: Cleanup
- Remove Python scripts, n8n/, launchd/
- Update CLAUDE.md with new architecture
- Data migration (metrics, articles, fiches from v0.x)

## 10. Risks & Mitigations

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| Gemini Flash quality vs Claude | Articles may need more editing | Medium | Gemini Pro fallback; iterative prompt tuning; writing guide as system instruction |
| CloudFlare Email Worker limitations | Email parsing edge cases | Medium | Forward unknown emails to fallback; manual link addition as backup |
| Cloud Run cold starts | Dashboard loads slowly after idle | Medium | Cloud Scheduler warm-up ping; min-instances=1 if needed ($0) |
| TypeScript rewrite scope | ~2000 lines to port | Medium | Pure data processing (no ML); phased approach; each phase independently useful |
| Firestore NoSQL modeling | Different from SQLite relational model | Low | Simple document structure; denormalized for read performance |

## 11. Out of Scope

- Multi-user support, roles, or permissions
- Mobile app (nice-to-have FR-17, post-MVP)
- Notion integration (explicitly removed)
- n8n compatibility layer
- Instagram carousel (deferred — needs Playwright on Cloud Run)
- NotebookLM podcast (deferred — nlm CLI is macOS-only)
- Automated LinkedIn posting (manual copy-paste stays)
- AI-powered newsletter discovery / recommendation
