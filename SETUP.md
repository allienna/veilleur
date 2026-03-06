# veilleur — Setup Guide

## Prerequisites

- [x] Mac with Docker installed
- [x] Claude Max subscription (Claude Code included)
- [x] Notion account with a workspace
- [ ] Claude Code installed (`npm install -g @anthropic-ai/claude-code`)

---

## Step 1 — Local Structure

```bash
# Clone the repo
git clone https://github.com/allienna/veilleur.git
cd veilleur

# Create the data folder
mkdir -p data
```

---

## Step 2 — Start n8n

```bash
cd n8n
docker-compose up -d
```

Access: http://localhost:5678
Login: `admin` / `veille2026` (change this)

---

## Step 3 — Configure the n8n Workflow

Create a new workflow with the following nodes:

### Node 1: Gmail Trigger
- **Type**: Gmail Trigger
- **Action**: Message Received
- **Filters**: filter by sender (your newsletter list)
- **Format**: RAW (to get the HTML)

### Node 2: Extract Links (Code node)

```javascript
// Parse the email HTML and extract links
const cheerio = require('cheerio');
const html = $input.first().json.raw; // Adapt based on Gmail structure

// If content is base64-encoded (raw Gmail format)
const body = Buffer.from(html, 'base64').toString('utf-8');
const $ = cheerio.load(body);

const links = [];
const seen = new Set();

$('a[href]').each((i, el) => {
  const url = $(el).attr('href');
  const text = $(el).text().trim();

  // Basic filters: remove tracking, unsubscribe, images, etc.
  if (!url || seen.has(url)) return;
  if (url.includes('unsubscribe')) return;
  if (url.includes('mailto:')) return;
  if (url.includes('list-manage.com')) return;
  if (url.includes('tracking')) return;
  if (url.match(/\.(png|jpg|gif|svg)$/)) return;

  seen.add(url);
  links.push({ url, title: text || 'Untitled' });
});

return links.map(link => ({ json: link }));
```

### Node 3: Scrape Content (HTTP Request, looped)

For each extracted link:
- **URL**: `https://r.jina.ai/{{ $json.url }}`
- **Method**: GET
- **Headers**: `Accept: text/markdown`

This returns the article content in markdown, for free.

### Node 4: Aggregate & Save (Code node)

```javascript
// Aggregate all results and write the JSON file
const fs = require('fs');
const date = new Date().toISOString().split('T')[0]; // YYYY-MM-DD
const dir = `/data/veille/${date}/raw`;

// Create the folder if needed
fs.mkdirSync(dir, { recursive: true });

// Count existing files for naming
const existing = fs.readdirSync(dir).filter(f => f.startsWith('newsletter-'));
const index = existing.length + 1;

const newsletter = {
  newsletter: $input.first().json.newsletter_name || 'Newsletter',
  received_at: new Date().toISOString(),
  links: $input.all().map(item => ({
    url: item.json.url,
    title: item.json.title,
    content: item.json.data || item.json.body || ''
  }))
};

const filename = `newsletter-${String(index).padStart(2, '0')}.json`;
fs.writeFileSync(`${dir}/${filename}`, JSON.stringify(newsletter, null, 2));

return [{ json: { saved: `${dir}/${filename}`, links: newsletter.links.length } }];
```

> **Note**: The Docker volume mounts `~/veille` to `/data/veille`, so files
> written by n8n in `/data/veille/` appear in `/Users/sn0rks/Code/github.com/allienna/veilleur/data/` on your Mac.

---

## Step 4 — Set Up Notion

### Create the "LinkedIn Watch" Database

In your Notion workspace, create a database with these properties:
- **Title** (title): article title
- **Date** (date): publication date
- **Status** (select): "To Review", "Approved", "Published"
- **Topic** (select): "AI", "Leadership", "Data", "Tech"

### Connect the Notion MCP to Claude Code

```bash
# In the claude-code project, add the Notion MCP server
claude mcp add notion -- npx -y @notionhq/notion-mcp-server
```

Then follow the Notion authentication instructions (OAuth).

---

## Step 5 — Use Claude Code

```bash
# Navigate to the project
cd claude-code

# Launch Claude Code
claude

# View today's sources
/sources

# Generate the article (defaults to today's date)
/generate

# Or for a specific date
/generate 2026-03-06
```

Claude Code will:
1. Read the scraped files
2. Show you the filtered sources → you approve
3. Suggest the angle → you approve
4. Generate article + post + image prompt
5. Push to Notion
6. Give you the link

---

## Step 6 — Publishing (you, ~10 min)

1. Open the Notion page, review the article
2. Copy the image prompt → Gemini in your browser → generate the image
3. Create the article on LinkedIn, paste the content + image
4. Share the article with the post text
5. Schedule for 8:45 AM

---

## Daily Workflow Summary

| When | What | Who |
|------|------|-----|
| Throughout the day | Newsletters arrive → n8n scrapes automatically | 🤖 n8n |
| ~7 PM | `claude` → `/generate` | 🧠 Claude Code + you (2 approvals) |
| ~7:15 PM | Notion review + Gemini image + LinkedIn publishing | 👤 You (~10 min) |

**Estimated daily time: 15–20 minutes** (vs ~1h+ previously)

---

## Troubleshooting

### n8n won't start
```bash
docker-compose logs -f
```

### Jina Reader rate-limited
Jina offers ~200 free requests/day. If you exceed this, add a delay between scrapes (use a "Wait" node in n8n, 1s between each).

### Claude Code can't find the files
Check that the Docker volume is properly mounted:
```bash
ls /Users/sn0rks/Code/github.com/allienna/veilleur/data/$(date +%Y-%m-%d)/raw/
```

### The Notion MCP isn't responding
```bash
claude mcp list   # Check that the server is active
claude mcp logs notion   # Check the logs
```
