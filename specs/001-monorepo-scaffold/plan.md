# Plan: Monorepo Scaffold

**Spec**: specs/001-monorepo-scaffold/spec.md

## Architecture Decisions

### AD-1: pnpm workspaces
- **Choice**: pnpm with `pnpm-workspace.yaml`
- **Rationale**: Turborepo's recommended package manager; strict dependency isolation; disk-efficient via content-addressable store
- **Alternatives considered**: npm workspaces (simpler but slower, hoisting issues), yarn (no clear advantage over pnpm)

### AD-2: Monorepo lives at project root
- **Choice**: Place `package.json`, `turbo.json`, `pnpm-workspace.yaml` at repo root alongside existing Python files
- **Rationale**: The v0.x Python code coexists during migration. Root-level monorepo config is standard for Turborepo. `.gitignore` already handles Python artifacts.
- **Alternatives considered**: Nested `v1/` directory (adds path complexity, breaks standard tooling expectations)

### AD-3: packages/core builds with tsup
- **Choice**: Use tsup (esbuild-based) to build `packages/core` into CJS + ESM
- **Rationale**: Fast, zero-config for library builds. Next.js and CF Workers can both consume the output. Vitest runs tests directly on source.
- **Alternatives considered**: tsc only (slower, no bundling), unbuild (heavier)

### AD-4: Vitest for testing
- **Choice**: Vitest in packages/core (and as default for future packages)
- **Rationale**: Fast, native TypeScript/ESM support, compatible with Turborepo pipelines. Same assertion API as Jest.
- **Alternatives considered**: Jest (slower TypeScript support, ESM issues)

### AD-5: Biome for linting and formatting
- **Choice**: Biome instead of ESLint + Prettier
- **Rationale**: Single tool for both linting and formatting, 10-100x faster than ESLint, zero config for TypeScript. Reduces dependency count.
- **Alternatives considered**: ESLint + Prettier (industry standard but slower, more config files, two tools to maintain)

## Affected Files

### New Files

| File | Purpose |
|------|---------|
| `package.json` | Root workspace config, Turborepo + Biome dev deps |
| `pnpm-workspace.yaml` | Workspace package globs |
| `turbo.json` | Pipeline definitions (build, dev, test, lint) |
| `biome.json` | Linting and formatting config |
| `.node-version` | Pin Node 20 LTS |
| `packages/tsconfig/base.json` | Shared strict TS base config |
| `packages/tsconfig/nextjs.json` | Next.js-specific TS config |
| `packages/tsconfig/worker.json` | CF Worker TS config |
| `packages/tsconfig/package.json` | Package metadata for tsconfig |
| `packages/core/package.json` | @veilleur/core package config |
| `packages/core/tsconfig.json` | Extends base.json |
| `packages/core/tsup.config.ts` | Build config |
| `packages/core/src/index.ts` | Exports version string |
| `packages/core/src/__tests__/index.test.ts` | Trivial version test |
| `packages/core/vitest.config.ts` | Vitest config |
| `apps/dashboard/` | Next.js 15 app (created via create-next-app) |
| `apps/dashboard/tsconfig.json` | Extends nextjs.json |
| `apps/email-worker/package.json` | @veilleur/email-worker config |
| `apps/email-worker/tsconfig.json` | Extends worker.json |
| `apps/email-worker/wrangler.toml` | CF Email Worker binding |
| `apps/email-worker/src/index.ts` | Worker entry point stub |

### Modified Files

| File | Change |
|------|--------|
| `.gitignore` | Add `node_modules/`, `.turbo/`, `dist/`, `.next/`, `.wrangler/`, `.env*` |

## Implementation Phases

### Phase 1: Root configuration
- Create root `package.json` with `"private": true` and workspace scripts
- Create `pnpm-workspace.yaml` pointing to `apps/*` and `packages/*`
- Create `turbo.json` with `build`, `dev`, `test`, `lint` pipelines
- Create `biome.json` with TypeScript rules
- Create `.node-version` with `20`
- Update `.gitignore` with Node/Turborepo entries

### Phase 2: Shared TypeScript configs
- Create `packages/tsconfig/package.json`
- Create `base.json` with strict settings
- Create `nextjs.json` extending base with JSX, Next.js plugin
- Create `worker.json` extending base with ES2022 target

### Phase 3: packages/core
- Create `package.json` for `@veilleur/core` with tsup build, vitest test
- Create `tsconfig.json` extending base
- Create `tsup.config.ts` for CJS + ESM output
- Create `src/index.ts` exporting `VERSION` string
- Create `vitest.config.ts`
- Create `src/__tests__/index.test.ts` asserting VERSION is a string
- Verify: `pnpm --filter @veilleur/core build` and `pnpm --filter @veilleur/core test`

### Phase 4: apps/dashboard
- Run `pnpm create next-app@latest apps/dashboard` with App Router, TypeScript, Tailwind, ESLint=no (using Biome)
- Update `tsconfig.json` to extend shared nextjs config
- Add `@veilleur/core` as workspace dependency
- Replace default page with minimal placeholder importing VERSION from core
- Verify: `turbo build` and `turbo dev`

### Phase 5: apps/email-worker
- Create `package.json` with `@cloudflare/workers-types` dev dep
- Create `tsconfig.json` extending worker config
- Create `wrangler.toml` with email worker binding (placeholder)
- Create `src/index.ts` with CF Email Worker signature
- Verify: `turbo build` passes for email-worker

### Phase 6: Verification
- Run `turbo build` — all 3 packages build with zero errors
- Run `turbo test` — core test passes
- Run `turbo lint` — Biome passes with zero warnings
- Verify dashboard imports and renders core VERSION
- Verify no `any` types in any source file

## Test Strategy

- **Framework**: Vitest (packages/core). Next.js tests deferred to F-004+.
- **Happy paths**: VERSION export is a non-empty string, matches package.json version
- **Error scenarios**: `turbo build` must fail on `strict: true` violations (verified manually during Phase 6)
- **Edge cases**: Cross-package import resolution (dashboard → core)

## Risk & Complexity

- **Estimated complexity**: Low
- **Key risks**:
  - `create-next-app` may generate config that conflicts with shared tsconfig — fix by overriding after generation
  - CF Worker types may need pinning to match wrangler version
- **New dependencies**: turbo, pnpm, tsup, vitest, biome, @cloudflare/workers-types, next 15, react 19
