---
name: generate
description: Generate the daily tech watch article (filter, write, push to Notion)
context: fork
argument-hint: "[date]"
---

# /generate — Generate the daily tech watch article

Read the writing guide and template carefully before starting:
- `${CLAUDE_SKILL_DIR}/writing-guide.md` — persona, style, strict rules, structure
- `${CLAUDE_SKILL_DIR}/article-template.md` — output structure template

Target date is `$ARGUMENTS` if provided, otherwise today's date (YYYY-MM-DD).

Follow these steps in order:

## 0.5 Metrics feedback

Check if there's a recent article without metrics:

```bash
just metrics-untracked
```

If an article without metrics is found (`date` field is not null):
- Display: "📊 Ton post du {DATE} ({TITLE}) — combien de likes, commentaires, reposts ?"
- Wait for user response
- Record the metrics:

```bash
just metrics {DATE} {LIKES} {COMMENTS} {REPOSTS}
```

Then display engagement insights:

```bash
just insights-for-generate
```

If the script returns text, display it. These insights guide the narrative angle selection in step 3.

If no article without metrics (`date` field is null), skip to step 1.

## 1. Load and filter sources

```bash
just sources {DATE}
```

This script returns JSON with filtered sources (sponsors removed, duplicates eliminated, grouped by theme).

Display a summary of kept and filtered sources, then ask for confirmation before continuing.

## 1.5 Trend detection

```bash
just detect-trends {DATE}
```

If trends are detected (clusters with score > 0), display clusters with scores and newsletters.
Use these trends to guide narrative angle selection in step 3.
If no trends (e.g. single newsletter), skip to step 2.

## 2. Read selected source content

```bash
just read-content {DATE} 0 1 2 3 ...
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

### {DATE}-post.md
The LinkedIn post text (see "Texte du post LinkedIn" section in the guide).

### {DATE}-image-prompt.md
The image prompt (see "Prompt image" section in the guide).

## 5. Write to disk

Write all three files to `data/output/`.
Create `data/output/` directory if it doesn't exist.

## 5.5 Generate image

```bash
just generate-image {DATE}
```

Non-blocking: if image generation fails (missing API key, safety filter, API error), display a warning and continue.

## 5.6 Index to history

```bash
just index {DATE}
```

Non-blocking: if indexing fails, display a warning and continue to step 6.

## 6. Push to Notion

Via the Notion MCP, create a page in the "Veille LinkedIn" database with:
- Title = article title
- Date = target date
- Status = "À relire"
- Content = article.md
- A callout "📝 Post LinkedIn" with post.md content
- A callout "🎨 Prompt Image" with image-prompt.md content

Confirm the URL of the created Notion page.
