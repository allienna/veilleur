---
name: sources
description: Display today's sources sorted by theme priority
argument-hint: "[date]"
---

# /sources — Display today's sources

Target date is `$ARGUMENTS` if provided, otherwise today's date (YYYY-MM-DD).

## Execution

```bash
just sources {DATE}
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
