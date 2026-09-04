# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Context

This project automates the generation of daily LinkedIn articles from tech watch newsletters.
Author: Aurélien Allienne, Engineering Director & GenAI Architect at SFEIR Lille.

Pipeline: **n8n** ingests and scrapes newsletters (Gmail → Jina Reader) into `data/raw/`, **Claude Code**
filters sources, writes the article, and publishes it, and the Astro **site** is the review/publish target
(replacing the earlier Notion-based review room described in some older docs).

## Commands

### Python environment
This project uses [uv](https://docs.astral.sh/uv/). Always prefix Python commands with `uv run`; install deps with `uv sync`.

### Tests
```bash
just test                    # run full pytest suite (tests/)
just test-file FILE           # run a single test file, e.g. tests/test_detect_trends.py
```
Tests cover `scripts/` logic only (carry-forward filtering, trend detection, metrics DB/insights, ChromaDB indexing, search) — there is no test suite for the Astro site.

### Sources & article generation
- `just sources [DATE] [CARRY=N]` — load and filter daily sources (JSON on stdout), with optional N-day carry-forward
- `just add-link DATE URL` — manually add a link, scraped via Jina Reader, saved to `data/raw/DATE-newsletter-manual.json`
- `just read-content DATE 0 2 5` — read full content of sources at given indices
- `just detect-trends [DATE] [CARRY=N]` — cross-newsletter trend detection
- `just save-processed DATE FILES...` — record which raw files were used, after generation

### History & search (ChromaDB)
- `just index [DATE]` — index the day's article
- `just index-all` — backfill index for all existing articles
- `just search "query" [LIMIT]` — semantic search across article history

### LinkedIn metrics (SQLite)
- `just metrics DATE LIKES COMMENTS REPOSTS`
- `just metrics-show DATE` / `just metrics-list` / `just metrics-untracked` / `just metrics-import FILE`
- `just insights` / `just insights-for-generate` — engagement insights report, the latter formatted for injection into `/generate`

### Site
- `just site` — install deps and run the Astro dev server
- `just export-site-data` — export ChromaDB/SQLite → JSON consumed by the site (needed for the trends page)
- `just add-image DATE FILE` / `just add-blog-image SLUG FILE` — copy an image into `site/public/images/`

### Images & social spin-offs
- `just generate-image DATE` — generate the article image from its prompt file via the Gemini API
- `just instagram [DATE]` — generate Instagram carousel + reel from an article
- `just instagram-carousel [DATE]` — carousel only
- `just instagram-setup` — one-time Playwright/Chromium install (used for carousel rendering)

### NotebookLM
- `just notebook [DATE] [--dry-run] [--audio]` — build a NotebookLM notebook from daily sources

### Sentinel automation (launchd, macOS)
- `just sentinel-install` / `just sentinel-stop` / `just sentinel-status` — manage the launchd agent
- `just sentinel-logs [DATE]` — show sentinel + autopublish logs for a date
- `just sentinel-run [DATE]` — run sentinel manually (testing)

### Infra
- `just start-n8n` / `just restart-n8n` — n8n via Docker (starts Colima first if needed)

**Rule: always use `just` recipes rather than calling scripts under `scripts/` directly** — they set up args/env consistently.

## Available skills (`.claude/skills/`)

- `/generate` — Generate the daily article (filter, write, publish to site). Writing rules live in `.claude/skills/generate/writing-guide.md`
- `/fiches [date]` — Generate source fiches for an already-published article and publish them to the site
- `/blog <slug>` — Publish a personal blog post to the site (separate track from tech watch articles)
- `/sources` — Display today's sources sorted by theme priority
- `/search` — Semantic search in article history
- `/notebook [date] [--audio] [--video] [--dry-run]` — Create a NotebookLM notebook from daily sources, optionally a podcast/video
- `/ship` — Create branch, commit, push and open a PR
- `/review-pr <pr-number>` — Fetch PR review comments, fix issues, reply to each comment
- `/merge` — Copilot review, comment resolution, squash merge

## Architecture

### Data flow
```
Gmail newsletters
  → n8n (Docker, docker-compose.yml in n8n/)
  → Jina Reader scraping
  → data/raw/DATE-newsletter-NN.json  (per-newsletter raw scrape, "links" array with url/title/content)
  → /generate (Claude Code): filter sources → detect trends → write article
  → site/src/content/articles/DATE.md (+ image, fiches)
  → Astro build → GitHub Pages
```

### Daily automation (launchd, `launchd/`)
Two scheduled agents chain the pipeline end-to-end without manual intervention:
- **sentinel** (`scripts/sentinel.py`, fires ~20:00) — checks there are enough sources (`MIN_SOURCES`), runs `claude -p` to generate the article autonomously, retries on transient API errors (429/5xx)
- **autopublish** (`scripts/autopublish.py`, fires 23:00) — if the article generated by sentinel hasn't been manually reviewed/published by then, publishes it as-is
Logs land in `data/logs/DATE-sentinel.log` and `data/logs/DATE-autopublish.log`; `just sentinel-status`/`sentinel-logs` surface them.

### History & metrics layer
- `data/chromadb/` — vector index of past articles + sources, used by `/search` and by `/generate` to avoid repeating recent topics
- `data/metrics.db` (SQLite) — LinkedIn engagement per article date; `scripts/metrics_insights.py` correlates themes with engagement to bias future angle selection

### Astro site (`site/`)
Static site, deployed on GitHub Pages at `https://allienna.github.io/veilleur` (`astro.config.mjs`: `base: '/veilleur'`, `output: 'static'`).

```
site/src/
├── content/
│   ├── articles/    # Tech watch articles (YYYY-MM-DD.md)
│   ├── blog/        # Personal blog posts (slug.md)
│   └── fiches/       # Source fiches (one per article source)
├── layouts/
│   ├── BaseLayout.astro    # Header, footer, fonts
│   ├── ArticleLayout.astro # Tech watch article page — parses "## Sources" / "Pour aller plus loin" from the markdown body
│   ├── BlogLayout.astro    # Personal blog post page — no sources parsing, no fiches, no AI disclaimer
│   ├── PageLayout.astro    # Static pages with optional hero image
│   └── FicheLayout.astro   # Source fiche detail page
├── pages/     # Astro routes
├── data/      # JSON exported by `just export-site-data` (tracked placeholders, regenerated at build/deploy time)
└── styles/global.css
```

Tech watch and blog posts share the homepage feed, sorted by date, distinguished by badge ("Veille" amber / "Article" navy).

Deployment: `.github/workflows/deploy.yml` triggers on push to `main` when `site/**` changes — exports data, builds, deploys to Pages. No CI runs the Python test suite; run `just test` locally before pushing changes to `scripts/`.

### Raw file format (produced by n8n)
```json
{
  "newsletter": "Newsletter name",
  "received_at": "2026-03-06T08:30:00Z",
  "links": [
    { "url": "https://...", "title": "Link title", "content": "Markdown content scraped via Jina Reader" }
  ]
}
```

### Article frontmatter (tech watch)
```yaml
title: "Article title"
date: 2026-03-09
themes: [IA, Sécurité, Leadership]
sources: 6
image: 2026-03-09.png
```

### Blog post frontmatter
```yaml
title: "Post title"
date: 2026-03-12
description: "Short description for cards and OG meta"
themes: [Data, Architecture]
image: my-post-slug.png
```

### Design conventions (site)
- **Fonts**: Poppins (headings, `font-display`), Work Sans (body, `font-sans`)
- **Colors**: primary `#f59f0a` (amber), navy-custom `#162d60`, background-light `#f8f7f5`
- **Header/Footer**: `bg-slate-900`
- **Mascot**: Le Veilleur owl — voice/style bible in `.claude/skills/generate/writing-guide.md`
