---
name: sources
description: Display today's sources sorted by theme priority
argument-hint: "[date] [CARRY=N]"
---

# /sources — Display today's sources

Arguments: `$ARGUMENTS` (optional).

Parse arguments:
- First argument matching `YYYY-MM-DD` → DATE (default: today)
- Argument matching `CARRY=N` or just a number after the date → CARRY (default: 0)

Examples: `/sources`, `/sources 2026-03-15`, `/sources 2026-03-15 CARRY=2`, `/sources 2026-03-15 2`

## Execution

```bash
just sources {DATE} {CARRY}
```

## Display

Show a summary table from the returned JSON:

| # | Source | Newsletter | Theme | Content |
|---|--------|------------|-------|---------|

Where:
- **Source**: original title (truncated to 60 chars) + URL
- **Newsletter**: source newsletter name
- **Theme**: IA / Leadership / Data / Tech / Autre
- **Content**: scraped content length (or "empty" if no content)

Then display filtered sources with their filter reason (`filter_reason`) in a separate section.

Show totals per category at the end.
