---
name: fiches
description: Generate source fiches for an article and publish to the site
argument-hint: "<date>"
---

# /fiches — Generate source fiches for a published article

Target date is `$ARGUMENTS` if provided, otherwise today's date (YYYY-MM-DD).

## 1. Parse article sources

Read `site/src/content/articles/{DATE}.md` and extract the `## Sources` section.
Each source is a numbered markdown link: `1. [Title](URL)`.

If the article doesn't exist, stop and notify.

## 2. Match raw content

For each source URL, search through `data/raw/{DATE}-newsletter-*.json` files to find matching scraped content.

Match by comparing URLs (normalize trailing slashes, ignore query params and tracking redirects).
Also check files from adjacent dates (DATE-1, DATE+1) in case of carry-forward.

For sources with no raw match, note them — they'll get shorter fiches.

Display a summary:
- Number of sources found in article
- Number matched with raw content
- Number without raw content

Ask for confirmation before generating.

## 3. Read matched content

For each matched source, read the full `content` field from the raw JSON.
This is the Jina Reader scraped content that will be used for translation and analysis.

## 4. Generate fiches

For each source (both main `## Sources` and `## Pour aller plus loin`), generate a fiche markdown file.

### Slug convention

Derive slug from the source title: kebab-case, ASCII only, max 60 characters.
Filename: `{DATE}-{slug}.md`

### Fiche format

```yaml
---
title: "{Original title of the source}"
date: {DATE}
url: "{source URL}"
authors: ["{author or domain name}"]
keywords: [{3-5 relevant keywords}]
theme: "{IA | Leadership | Data | Tech | Sécurité | Géopolitique}"
tone: "{opinion | tutorial | research | news}"
used_in: ["{DATE}"]
---

## Résumé

{2-3 sentence summary of what the source covers and its main argument.}

## Points clés

- {key point 1}
- {key point 2}
- {key point 3}
- ...

## Analyse approfondie

{Deep dive into the source content. Expand on the key arguments with specific data points,
quotes, and examples from the original article. Structure with sub-headings (###) when the
content warrants it. Typical length: 3-8 paragraphs depending on source richness.
This section is only generated when raw content is available — skip for sources without raw match.}

## Pourquoi ça compte

{1-2 sentences on why this source matters for tech watch.}
```

### Frontmatter keys — IMPORTANT

Use **exactly** the English key names shown in the template above: `authors`, `keywords`, `theme`, `tone`, `used_in`. Never use French equivalents (`auteurs`, `mots_cles`, `tonalite`, `articles`) — the Astro content schema expects the English keys and fiches will not render otherwise.

### Enrichment rules

- **theme**: Match the themes used in the article frontmatter when relevant. Use the source content to determine the best fit.
- **keywords**: Extract 3-5 specific, meaningful keywords from the content (not generic terms like "technology").
- **tone**: Classify as `opinion` (editorial, personal take), `tutorial` (how-to, guide), `research` (academic, data-driven), or `news` (announcement, reporting).
- **authors**: Extract from the content if visible (byline, author tag). Fallback to the domain name.
- **Résumé**: Concise and factual. In French.
- **Points clés**: In French. 3-5 bullet points capturing the essential takeaways.
- **Analyse approfondie**: In French. Deep dive with specific data, quotes, examples from the original. Use ### sub-headings for structure. Only when raw content is available.
- **Pourquoi ça compte**: In French. Connect the source to the broader tech watch narrative.

For sources without raw content, generate a shorter fiche based on the title and URL only (skip Points clés, Analyse approfondie, keep Résumé brief).

## 5. Write to site

Write all fiche files to `site/src/content/fiches/`.

Display the list of generated files.

## 6. Verify build

```bash
cd site && npm run build 2>&1 | tail -5
```

Confirm the build succeeds and fiches are rendered.
