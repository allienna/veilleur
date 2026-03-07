# /sources — Display today's sources

Read all files matching the pattern `../data/raw/{DATE}-newsletter-*.json` where {DATE} is the provided argument (e.g. `/sources 2026-03-06`) or today's date if no argument.

Display a summary as a table:

| # | Source | Newsletter | Topic | Relevance |
|---|--------|------------|-------|-----------|

Where:
- **Source**: original title (truncated to 60 chars) + URL
- **Newsletter**: name of the originating newsletter
- **Topic**: AI / Leadership / Data / Tech / Marketing / Other
- **Relevance**: 🟢 (article) / 🟡 (further reading) / 🔴 (filtered out)

Show the total per category at the end.
