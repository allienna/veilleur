# Tasks: Monorepo Scaffold

**Plan**: specs/001-monorepo-scaffold/plan.md
**Status**: Ready
**Total**: 11 tasks across 6 phases

## Phase 1: Root configuration

- [x] **T-1.1**: Create root package.json and pnpm workspace
  - **Do**: Create `package.json` with `"private": true`, `"name": "veilleur"`, workspace scripts (`build`, `dev`, `test`, `lint`), and dev dependencies (`turbo`). Create `pnpm-workspace.yaml` with `packages: ["apps/*", "packages/*"]`. Create `.node-version` with `20`.
  - **Test**: `pnpm install` succeeds without errors

- [x] **T-1.2**: Create turbo.json pipeline config
  - **Do**: Create `turbo.json` defining `build` (depends on `^build`), `dev` (persistent, no cache), `test`, and `lint` pipelines.
  - **Test**: `pnpm turbo --dry-run build` shows the pipeline graph

- [x] **T-1.3**: Add Biome config and update .gitignore
  - **Do**: Add `@biomejs/biome` as root dev dep. Create `biome.json` with TypeScript linting and formatting rules. Update `.gitignore` to add `node_modules/`, `.turbo/`, `dist/`, `.next/`, `.wrangler/`, `.env*`, `pnpm-lock.yaml` exclusions as needed.
  - **Test**: `pnpm biome check .` runs without config errors

## Phase 2: Shared TypeScript configs

- [x] **T-2.1**: Create shared tsconfig packages
  - **Do**: Create `packages/tsconfig/package.json` with `"name": "@veilleur/tsconfig"`. Create `base.json` (`strict: true`, `esModuleInterop`, `skipLibCheck`, `forceConsistentCasingInFileNames`, `resolveJsonModule`, `isolatedModules`). Create `nextjs.json` extending base with JSX preserve, module bundler resolution, Next.js plugin. Create `worker.json` extending base with ES2022 target and lib.
  - **Test**: Files exist and are valid JSON (`node -e "require('./packages/tsconfig/base.json')"`)

## Phase 3: packages/core

- [x] **T-3.1**: Create @veilleur/core package with build
  - **Do**: Create `packages/core/package.json` with `"name": "@veilleur/core"`, `main` and `types` pointing to `dist/`, scripts for `build` (tsup) and `test` (vitest). Create `tsconfig.json` extending `@veilleur/tsconfig/base.json`. Create `tsup.config.ts` outputting CJS + ESM. Create `src/index.ts` exporting `export const VERSION = "1.0.0"`.
  - **Test**: `pnpm --filter @veilleur/core build` succeeds and `dist/` contains output

- [x] **T-3.2**: Add Vitest and first test
  - **Do**: Add vitest as dev dep. Create `vitest.config.ts`. Create `src/__tests__/index.test.ts` testing that VERSION is a non-empty string.
  - **Test**: `pnpm --filter @veilleur/core test` passes

## Phase 4: apps/dashboard

- [x] **T-4.1**: Scaffold Next.js 15 dashboard app
  - **Do**: Run `pnpm create next-app@latest apps/dashboard` with App Router, TypeScript, Tailwind, no ESLint (using Biome). Remove default ESLint config if generated. Update `tsconfig.json` to extend `@veilleur/tsconfig/nextjs.json` while keeping Next.js required paths.
  - **Test**: `pnpm --filter @veilleur/dashboard dev` starts on localhost

- [x] **T-4.2**: Wire dashboard to @veilleur/core
  - **Do**: Add `"@veilleur/core": "workspace:*"` to dashboard dependencies. Replace default `page.tsx` with a minimal "Veilleur Dashboard" page that imports and renders `VERSION` from `@veilleur/core`.
  - **Test**: `pnpm turbo build` succeeds across all packages; dashboard page shows version string

## Phase 5: apps/email-worker

- [x] **T-5.1**: Create CloudFlare Email Worker stub
  - **Do**: Create `apps/email-worker/package.json` with `"name": "@veilleur/email-worker"`, `@cloudflare/workers-types` as dev dep, build script using tsc. Create `tsconfig.json` extending `@veilleur/tsconfig/worker.json`. Create `wrangler.toml` with email worker binding (placeholder domain). Create `src/index.ts` with the CF Email Worker entry point signature (`email(message, env, ctx)` returning void).
  - **Test**: `pnpm turbo build` passes including email-worker

## Phase 6: Verification

- [x] **T-6.1**: Full pipeline verification
  - **Do**: Run `turbo build`, `turbo test`, `turbo lint` across all packages. Fix any remaining issues (implicit any, lint warnings, build errors).
  - **Test**: All three commands pass with zero errors and zero warnings

- [x] **T-6.2**: Verify strict mode enforcement
  - **Do**: Temporarily add `const x = null; x.foo` to `packages/core/src/index.ts` and verify `turbo build` fails. Remove the bad code. Grep all tsconfigs for `"strict": true`.
  - **Test**: Build fails on strict violation, then passes after removal; all tsconfigs have strict enabled
