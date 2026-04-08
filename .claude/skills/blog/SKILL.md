---
name: blog
description: Publish a personal blog post to the site
argument-hint: "<slug>"
---

# /blog — Publish a personal blog post

Target slug is `$ARGUMENTS`. Required — used as the filename and URL path.

## 1. Check if the post already exists

Look for `site/src/content/blog/{SLUG}.md`.

If it exists, display the current frontmatter and ask: "Ce billet existe déjà. Tu veux l'éditer ou repartir de zéro ?"

## 2. Collect post content

Ask for the content if not already provided in the conversation. The user may:
- Paste raw text directly
- Reference a file path to read

## 3. Structure the post

From the raw content, produce a well-structured markdown post:

### Frontmatter

```yaml
---
title: "{Title — derived from the content or first sentence}"
date: {TODAY in YYYY-MM-DD}
description: "{1-2 sentence summary for cards and OG meta}"
themes: [{relevant themes from: IA, Data, Leadership, Architecture, Tech, Sécurité, DevOps}]
---
```

### Body rules

- Keep the author's voice and style intact — do NOT rewrite or polish
- Add `## ` headings to structure if the text is long (>5 paragraphs) and doesn't have them
- Use markdown formatting: `**bold**` for emphasis, `code` for technical terms, `> blockquote` for citations
- Separate the closing reference/inspiration note with `---` in italics
- The first paragraph serves as the lead (styled via `article-intro` CSS)

Present the structured post and ask for validation before writing.

## 4. Image prompt

Generate an image prompt for the blog post, following the mascot bible below.

### Mascot bible — Le Veilleur

> An expressive cartoon owl mascot called "Le Veilleur": deep navy blue body, large expressive amber eyes, small antenna on top of the head, white chest feathers. Animated cartoon style — think Pixar short or Saturday morning cartoon, colorful, dynamic, full of personality. The character is always the protagonist of the scene.

### Prompt rules

- In English, for Gemini (Nano Banana)
- No text in the image
- Always feature the owl mascot in a scene illustrating the post's main theme
- The scene must visually represent 2-3 key ideas from the post simultaneously
- Tell a story without words — action, posture, and setting carry the message
- Dynamic and expressive, not static
- **Always specify `wide 16:9 aspect ratio`**

### Theme examples

- Data / pipelines → the owl surfing a wave of charts and pipelines
- Architecture / agents → the owl as a conductor directing small robots
- Leadership → the owl in a meeting room facing a whiteboard full of arrows and questions
- Security → the owl as a detective or ethical hacker, magnifying glass in hand

Display the generated prompt and ask: "Tu veux que je génère l'image ou tu as déjà un fichier ?"

If the user provides a file:

```bash
just add-blog-image {SLUG} {FILE_PATH}
```

Add `image: {SLUG}.png` to the frontmatter.

If the user wants to generate the image themselves, just display the prompt for copy-paste and move on. They can add the image later with `just add-blog-image`.

## 5. Write to site

Write the final markdown to `site/src/content/blog/{SLUG}.md`.

## 6. Verify build

```bash
cd site && npm run build 2>&1 | tail -5
```

Confirm the build succeeds and the post is rendered.

## 7. Publish

Ask: "Tu veux lancer /claude-feature-flow:ship pour créer la PR ?"
