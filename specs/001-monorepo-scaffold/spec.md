# Spec: Monorepo Scaffold

**Track ID**: 001-monorepo-scaffold
**Roadmap ref**: F-001
**Status**: In Progress
**Created**: 2026-04-08
**Branch**: feat/001-monorepo-scaffold
**PRD sections**: Architecture (§5), Phase 1
**Depends on**: None

## Context

The v0.x codebase mixes Python scripts, shell wrappers, n8n flows, and launchd plists. The v1 rebuild consolidates everything into a single TypeScript monorepo managed by Turborepo. This feature creates the empty but fully wired scaffold — every subsequent feature builds on top of it.

## User Stories

- As a developer, I want a single `turbo build` command that builds all packages so that CI and local dev use the same workflow
- As a developer, I want shared TypeScript types importable from `@veilleur/core` so that dashboard and email-worker stay in sync
- As a developer, I want `turbo dev` to start the Next.js dashboard with hot reload so that I can iterate quickly
- As a developer, I want `turbo test` to run tests across all packages so that quality gates work from day one

## Functional Requirements

### FR-1: Turborepo root configuration
Root `package.json` with Turborepo as dev dependency. `turbo.json` defining `build`, `dev`, `test`, and `lint` pipelines with correct dependency graph (`packages/core` builds before `apps/*`).

### FR-2: packages/core
Shared TypeScript package (`@veilleur/core`):
- `package.json` with `name: "@veilleur/core"`, `main` and `types` pointing to build output
- `tsconfig.json` extending a shared base config, `strict: true`
- Placeholder `src/index.ts` exporting a version string
- Vitest config for unit tests
- One trivial test proving the setup works

### FR-3: apps/dashboard
Next.js 15 App Router application:
- Created via `create-next-app` with App Router, TypeScript, Tailwind, ESLint
- Depends on `@veilleur/core` (workspace dependency)
- `tsconfig.json` with `strict: true`
- Default Next.js pages replaced with a minimal "Veilleur Dashboard" placeholder page
- Imports and displays the version string from `@veilleur/core` (proves cross-package imports work)

### FR-4: apps/email-worker
CloudFlare Email Worker stub:
- `package.json` with `name: "@veilleur/email-worker"`
- `tsconfig.json` with `strict: true`, targeting ES2022
- `wrangler.toml` with email worker binding (placeholder config)
- Placeholder `src/index.ts` with the CF Email Worker entry point signature (`email(message, env, ctx)`)
- No deployment — just the local project structure

### FR-5: Shared TypeScript configuration
`packages/tsconfig/` with shared base configs:
- `base.json`: `strict: true`, `esModuleInterop`, `skipLibCheck`, `forceConsistentCasingInFileNames`, `resolveJsonModule`
- `nextjs.json`: extends base, adds Next.js-specific settings (JSX, module resolution, plugins)
- `worker.json`: extends base, targets ES2022, `lib: ["ES2022"]`
- Each app/package tsconfig extends the appropriate shared config

### FR-6: Linting and formatting
- ESLint config at root or per-package (consistent rules)
- Prettier config at root (consistent formatting)
- Both wired into `turbo lint`

### FR-7: .gitignore and workspace hygiene
- Root `.gitignore` covering `node_modules/`, `.turbo/`, `dist/`, `.next/`, `.wrangler/`, `.env*`
- No lockfile conflicts (single `package-lock.json` at root or pnpm workspace)
- `README.md` not required (CLAUDE.md serves as project docs)

## Error Scenarios

- `turbo build` must fail with a clear TypeScript error if `strict: true` is violated (e.g., implicit `any`)
- `turbo test` must exit non-zero if any test fails

## Acceptance Criteria

- [ ] AC-1: `turbo build` succeeds with zero errors across all 3 packages
- [ ] AC-2: `turbo test` runs and passes (at least 1 test in packages/core)
- [ ] AC-3: `turbo dev` starts the Next.js dashboard on localhost
- [ ] AC-4: Dashboard page imports and renders the `@veilleur/core` version string
- [ ] AC-5: All tsconfigs have `strict: true`
- [ ] AC-6: apps/email-worker has a valid wrangler.toml and CF Worker entry point
- [ ] AC-7: `turbo lint` passes with zero warnings
- [ ] AC-8: No `any` types in any source file

## Out of Scope

- Firestore client setup (F-002)
- shadcn/ui or Tailwind design tokens (F-004)
- CI/CD pipeline (F-017)
- Any business logic — this is pure scaffolding

## Decisions

1. **Package manager**: pnpm (Turborepo recommended, better workspace support)
2. **Node version**: Node 20 LTS (`.node-version` + `engines` field)
