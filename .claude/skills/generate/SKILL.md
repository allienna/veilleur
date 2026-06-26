---
name: generate
description: Generate the daily tech watch article (filter, write, publish to site)
context: fork
argument-hint: "[date]"
---

# /generate — Generate the daily tech watch article

Read the writing guide and template carefully before starting:
- `${CLAUDE_SKILL_DIR}/writing-guide.md` — persona, style, strict rules, structure
- `${CLAUDE_SKILL_DIR}/article-template.md` — output structure template

Target date is `$ARGUMENTS` if provided, otherwise today's date (YYYY-MM-DD).

Follow these steps in order:

## Mode autonome

If the prompt contains "autonomous mode", apply these overrides:
- Step 1: Execute but DO NOT ask for confirmation — continue directly
- Step 1.5: Execute but DO NOT ask for confirmation
- Step 3: Select the narrative AUTONOMOUSLY:
  - Prioritize trend clusters (score > 0.5)
  - Then theme priority: IA > Leadership > Data > Tech
  - Select 6-7 main sources + 3-4 "pour aller plus loin"
  - DO NOT ask for validation
- Step 6: Copy files to site but DO NOT propose /ship

## 1. Load and filter sources

```bash
just sources {DATE} 3
```

This script returns JSON with filtered sources (sponsors removed, duplicates eliminated, grouped by theme).
The `3` enables carry-forward: sources from late-arriving newsletters (up to 3 days back) that weren't included in previous generations are automatically included.

Display a summary of kept and filtered sources, then ask for confirmation before continuing.

If carry-forward sources are present (`carryforward_count > 0` in the JSON output), display:
> 📦 {N} sources tardives du {DATE_PRECEDENT} incluses (arrivées après la génération)

## 1.5 Trend detection

```bash
just detect-trends {DATE} 3
```

If trends are detected (clusters with score > 0), display clusters with scores and newsletters.
Use these trends to guide narrative angle selection in step 3.
If no trends (e.g. single newsletter), skip to step 2.

## 2. Read selected source content

```bash
just read-content {DATE} 0 1 2 3 ... --carry-forward 3
```

Pass the `index` field values from each kept source (from the `just sources` JSON output). The script returns the first 3000 characters of each source.

## 3. Narrative selection

- Identify the narrative thread connecting the best sources
- Select 5 to 8 main sources + 3 to 5 "pour aller plus loin" sources
- Propose the narrative thread and article angle, ask for validation

## 4. Generation

Generate three files following the writing guide (`writing-guide.md`):

### {DATE}-article.md
The full article following the template structure (`article-template.md`).

The file MUST start with the YAML front matter block:
```yaml
---
title: "{Article title}"
date: {DATE}
themes: [{comma-separated list of main themes, e.g. IA, Leadership}]
sources: {number of sources used}
image: {DATE}.png
---
```
Then the full article body.

### {DATE}-post.md
The LinkedIn post text (see "Texte du post LinkedIn" section in the guide).

### {DATE}-image-prompt.md
The image prompt (see "Prompt image" section in the guide).

## 4.5 Fiches de lecture

For each of the 3 to 5 main sources used in the article (not "pour aller plus loin"), generate a reading fiche and write it to `data/fiches/`.

Create `data/fiches/` if it doesn't exist.

For each source:
- Derive a slug from the title: kebab-case, ASCII only, max 60 characters
- Write file: `data/fiches/{DATE}-{slug}.md`

Format:
```yaml
---
title: "{Original title of the source}"
date: {DATE}
url: {source URL}
authors: [{domain or author name extracted from URL or content}]
keywords: [{3-5 keywords from the content}]
theme: {main theme: IA | Leadership | Data | Tech}
tone: {opinion | tutorial | research | news}
used_in: ["{DATE}"]
---

## Résumé

{3-4 sentence summary of the source in French. Concise, captures the key thesis and main facts.}

## Points clés

- {key point 1}
- {key point 2}
- {key point 3}
...

## Analyse approfondie

{Full translation of the source article into French. Use the full content already read in step 2. Be thorough — this is a reference document. Preserve the original structure (sections, lists, quotes).}

## Pourquoi ça compte

{1-2 sentences on why this source matters for tech watch.}
```

## 5. Write to disk

Write all three article files to `data/output/`.
Create `data/output/` directory if it doesn't exist.
Fiches are written to `data/fiches/` (already handled in step 4.5).

## 5.1 Record processed files

Save the list of raw files that contributed to this article (enables carry-forward for late-arriving newsletters):

```bash
just save-processed {DATE} {files_loaded_paths from step 1 JSON output}
```

The `files_loaded_paths` field from the step 1 JSON output contains the list of raw file basenames to pass here.

## 5.5 Index to history

```bash
just index {DATE}
```

Non-blocking: if indexing fails, display a warning and continue to step 6.

## 6. Publish to site

Copy the reviewed files to the Astro site structure:

1. **Article**: Copy `data/output/{DATE}-article.md` to `site/src/content/articles/{DATE}.md`
2. **Fiches**: Copy all `data/fiches/{DATE}-*.md` files to `site/src/content/fiches/`

Display a summary of files copied, then ask: "Tu veux lancer /ship pour créer la PR ?"
