# ADR-003: Jina Reader for web scraping

- **Status**: Accepted
- **Date**: 2026-03-08

## Context

The n8n workflow needs to extract article content from URLs found in newsletters. The extracted content must be clean markdown suitable for LLM processing. We evaluated several approaches: custom scraping (Puppeteer/Playwright), Jina Reader API, and other extraction services (Diffbot, ScrapingBee).

## Decision

Use [Jina Reader](https://r.jina.ai) (`r.jina.ai/{url}`) for markdown extraction, integrated directly into the n8n workflow.

## Arguments for this approach

1. **Zero configuration** — no API key required, no authentication setup
2. **Clean markdown output** — returns well-structured markdown, ideal for LLM consumption
3. **n8n native integration** — simple HTTP Request node, no custom code needed
4. **Free tier sufficient** — ~200 requests/day covers our volume (5-15 newsletters × ~10 links each)
5. **Handles JavaScript rendering** — works on SPAs and dynamic pages unlike simple HTTP fetches

## Arguments against

1. **External dependency** — service availability is outside our control
2. **Rate limits** — free tier caps at ~200 requests/day, could become a bottleneck if volume grows
3. **No SLA** — free service with no uptime guarantee
4. **Content quality varies** — some pages return partial or noisy content (cookie banners, navigation)

## Alternatives considered

- **Custom Puppeteer/Playwright scraper**: full control but significant maintenance burden, needs hosting
- **Diffbot / ScrapingBee**: better quality extraction but paid services, overkill for current volume
- **Simple HTTP fetch + cheerio**: fast but fails on JavaScript-rendered pages

## Consequences

- If Jina Reader becomes unavailable or rate-limited, the fallback is to add a paid API key or switch to a self-hosted solution
- Content quality filtering is handled downstream in `load_sources.py` (MIN_CONTENT_LENGTH = 500 chars)
- If daily link volume exceeds ~150, we should consider a paid plan or alternative service
