---
name: notebook
description: Create a NotebookLM notebook from daily sources and generate a podcast
argument-hint: "[date] [--audio] [--video] [--dry-run]"
---

# /notebook — Create a NotebookLM notebook from daily sources

Arguments: `$ARGUMENTS` (optional).

Parse arguments:
- First argument matching `YYYY-MM-DD` → DATE (default: today)
- `--audio` → also generate a podcast after adding sources
- `--video` → also generate a cinematic video after adding sources
- `--dry-run` → preview filtered sources without creating anything

Examples: `/notebook`, `/notebook 2026-03-16`, `/notebook 2026-03-16 --audio --video`, `/notebook --dry-run`

## Prerequisites

The `nlm` CLI must be installed and authenticated:
```bash
nlm login --check
```

If not authenticated, ask the user to run `nlm login` first.

## Execution

### Step 1 — Dry run preview

Always start with a dry run to show the user what will be added:

```bash
just notebook {DATE} --dry-run
```

Display the filtered source list grouped by theme and ask for confirmation before proceeding.

### Step 2 — Create notebook and add sources

After user confirmation:

```bash
just notebook {DATE} {FLAGS}
```

Where FLAGS includes `--audio` if the user requested podcast generation.

### Step 3 — Report

Display a summary:
- Notebook name and ID
- Number of sources added (success/fail)
- Audio generation status (if requested)
