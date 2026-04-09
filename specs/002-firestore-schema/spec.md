# Spec: Firestore Schema

**Track ID**: 002-firestore-schema
**Roadmap ref**: F-002
**Status**: Draft
**Created**: 2026-04-09
**Branch**: feat/002-firestore-schema
**PRD sections**: Architecture (§5), FR-3, FR-4, FR-5, FR-7, FR-12
**Depends on**: F-001 (Complete)

## Context

F-001 delivered the monorepo scaffold. This feature adds the Firestore data layer that every subsequent feature depends on: typed collections, a typed client, and local dev infrastructure. Without it, no feature can read or write persistent data.

The v1 rebuild consolidates SQLite (metrics), ChromaDB (vector search), and filesystem JSON (raw sources) into a single Firestore database with vector search. This spec defines the schema, the client wrapper, and the emulator setup — no business logic, no UI.

## User Stories

- As a developer, I want to import typed Firestore collections from `@veilleur/core` so that reads and writes are type-safe
- As a developer, I want to run Firestore locally via the emulator so I can develop and test without hitting GCP
- As a developer, I want to seed the emulator with sample data so that UI features can be developed quickly
- As a developer, I want documented collection schemas so future features know the data shape without reverse-engineering

## Functional Requirements

### FR-1: Firestore client wrapper
Create a typed Firestore client in `packages/core/src/db/` that:
- Initializes with GCP project ID from env (`GCP_PROJECT_ID`)
- Uses the Firestore emulator in development (`FIRESTORE_EMULATOR_HOST` env var)
- Exports typed collection references (one per collection)
- Uses `firebase-admin` SDK (server-side only; no client SDK — writes go through API routes per constitution §4.4)

### FR-2: Collection: `newsletters`
Newsletter registry per PRD FR-3.
```typescript
{
  id: string;              // slug (e.g., "tldr-ai")
  name: string;            // display name
  type: "email" | "rss";
  email_sender?: string;   // for type=email
  rss_url?: string;        // for type=rss
  themes: string[];        // default themes for this newsletter
  priority: number;        // ordering weight
  active: boolean;
  last_fetched_at?: Timestamp;
  created_at: Timestamp;
  updated_at: Timestamp;
}
```

### FR-3: Collection: `sources`
Individual source items (articles, links) per PRD FR-4/FR-5.
```typescript
{
  id: string;                // auto-generated
  url: string;               // unique per date
  title: string;
  content: string;           // markdown scraped via Jina
  newsletter_id: string;     // ref to newsletters
  publisher: string;         // extracted from sender (for trend detection)
  themes: string[];          // detected themes
  received_at: Timestamp;
  date: string;              // YYYY-MM-DD for daily grouping
  curation: "selected" | "further_reading" | "excluded" | null;
  trend_cluster_id?: string; // if part of a trend
  created_at: Timestamp;
}
```

### FR-4: Collection: `articles`
Generated articles per PRD FR-9/FR-10.
```typescript
{
  id: string;                // YYYY-MM-DD
  date: string;              // YYYY-MM-DD
  title: string;
  content: string;           // full markdown
  linkedin_post: string;
  image_prompt: string;
  image_url?: string;
  themes: string[];
  source_ids: string[];
  status: "draft" | "reviewed" | "published";
  published_at?: Timestamp;
  created_at: Timestamp;
  updated_at: Timestamp;
}
```

### FR-5: Collection: `pipeline_runs`
Per-step pipeline logs per PRD FR-7. Constitution §2.2 (no silent failures).
```typescript
{
  id: string;                      // auto-generated
  date: string;                    // YYYY-MM-DD
  step: string;                    // "ingest" | "filter" | "trends" | "generate" | ...
  status: "running" | "success" | "failed" | "skipped";
  started_at: Timestamp;
  finished_at?: Timestamp;
  duration_ms?: number;
  error?: string;
  output?: Record<string, unknown>;
}
```

### FR-6: Collection: `metrics`
LinkedIn engagement per PRD FR-12.
```typescript
{
  id: string;                // YYYY-MM-DD (article ID)
  date: string;
  likes: number;
  comments: number;
  reposts: number;
  impressions?: number;
  engagement_score: number;  // computed: likes + comments*3 + reposts*5
  recorded_at: Timestamp;
}
```

### FR-7: Firestore emulator config
Provide `firebase.json` and `.firebaserc` at repo root (or `packages/core/`) to run the emulator locally.
- Emulator accessible on default port
- `just` or `pnpm` recipe to start/stop the emulator
- `FIRESTORE_EMULATOR_HOST` env var picks up emulator automatically

### FR-8: Seed data utility
Provide `packages/core/src/db/seed.ts` that populates the emulator with:
- 2-3 sample newsletters
- ~10 sample sources for today's date
- 1 sample article (draft status)
- A few sample metrics rows

Runnable via `pnpm --filter @veilleur/core seed`.

### FR-9: Schema documentation
A `packages/core/src/db/README.md` (or `SCHEMA.md`) that documents all collections, their fields, and their relationships. Updated whenever a collection is added/changed. Referenced from constitution's quality gate (§5 "New Firestore collections/fields documented in schema file").

## Error Scenarios

- Emulator not running when code tries to connect → clear error message pointing to start command
- Missing `GCP_PROJECT_ID` env var in production → fail fast on startup with readable error
- Invalid document shape on write → fail fast with TypeScript error (no runtime validation needed; API routes validate input per constitution §5)

## Acceptance Criteria

- [ ] AC-1: `@veilleur/core` exports `db` with typed collection references (`db.newsletters`, `db.sources`, `db.articles`, `db.pipeline_runs`, `db.metrics`)
- [ ] AC-2: All collection types exported as TypeScript types (`Newsletter`, `Source`, `Article`, `PipelineRun`, `Metrics`)
- [ ] AC-3: Firestore emulator starts via a documented command
- [ ] AC-4: Seed script populates the emulator with sample data without errors
- [ ] AC-5: A vitest integration test reads from and writes to the emulator, verifying type safety round-trip
- [ ] AC-6: `turbo build` and `turbo test` pass (including new Firestore tests)
- [ ] AC-7: `packages/core/src/db/SCHEMA.md` documents all 5 collections
- [ ] AC-8: No `any` types in the db module
- [ ] AC-9: Missing emulator connection produces a clear, actionable error

## Out of Scope

- Vector search indexes (added when F-003 or a search feature needs them)
- Firestore security rules (deny-all except Cloud Run SA — deferred to F-017 deployment)
- Data migration from v0.x SQLite/ChromaDB (F-018)
- CRUD API routes (F-006 for newsletters, F-007 for ingest, F-014 for metrics)
- UI for any collection (F-005, F-006, F-011, F-014)

## Open Questions

1. **Timestamp fields**: Use Firestore `Timestamp` type directly or ISO strings? Firestore native Timestamps give better querying but need conversion at API boundaries. Recommendation: **Firestore `Timestamp`** in the DB layer, converted to ISO strings at API route boundaries.
2. **Emulator vs real Firestore for tests**: Vitest tests can hit the emulator (slower but realistic) or mock the client (faster but less safe). Recommendation: **hit the emulator** for this feature's tests (proves the schema works) with a `pnpm test:integration` script separate from unit tests.
3. **firebase.json location**: Repo root or `packages/core/`? Root is standard for Firebase CLI. Recommendation: **repo root**.
4. **Seed data source**: Hardcoded in `seed.ts` or loaded from a JSON fixture? Recommendation: **hardcoded in TS** for type safety and simplicity (small dataset).
