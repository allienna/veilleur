# /generate — Generate today's tech watch article

Follow these steps in order:

## 1. Load sources

Read all `newsletter-*.json` files in `../data/$ARGUMENTS/raw/` (or today's date if no argument).

If the folder doesn't exist or is empty, notify and stop.

## 2. Filtering

From all collected links:
- Remove marketing, sponsored, and promotional links (detect by URL or content)
- Remove duplicates
- Rank remaining links by relevance (AI > Leadership > Data > Tech > Other)
- Display the filter results and ask for confirmation before continuing

## 3. Selection and narrative thread

- Identify the narrative thread connecting the best sources together
- Select 5 to 8 main sources + 3 to 5 "further reading" sources
- Propose the narrative thread and the article's angle, ask for validation

## 4. Generation

Generate three files:

### article.md
The full article following CLAUDE.md rules (structure, inline refs, style, etc.)

### post.md
The LinkedIn post companion text:
- 3-5 lines max
- Catchy, makes people want to click
- 2-3 hashtags
- Question or call to action at the end

### image-prompt.md
A prompt in English for Gemini (Nano Banana):
- Conceptual visual description related to the theme
- No text in the image
- Modern, clean style

## 5. Local write

Write the three files to `../data/$DATE/`.

## 6. Push to Notion

Via the Notion MCP, create a page in the "Veille LinkedIn" database with:
- Title = article title
- Date = today's date
- Status = "À relire"
- Content = article.md
- A "📝 Post LinkedIn" callout with post.md content
- A "🎨 Prompt Image" callout with image-prompt.md content

Confirm the URL of the created Notion page.
