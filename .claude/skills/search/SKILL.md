---
name: search
description: Semantic search in article history
argument-hint: "<query>"
---

# /search — Search article history

Perform a semantic search across past articles indexed in ChromaDB.

## Execution

```bash
just search "$ARGUMENTS"
```

## Display results

Show results as a table:

| Date | Title | Relevance | Themes | Excerpt |
|------|-------|-----------|--------|---------|

If no results:
- if `total_indexed == 0`, indicate the history is empty and suggest running `just index-all` to index existing articles;
- if `total_indexed > 0`, indicate no indexed article matches this query and suggest refining the search.
