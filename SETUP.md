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
mkdir -p data/raw data/output
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

Import the workflow from `n8n/workflow-veilleur.json` or create manually with the following nodes.

See `docs/workflow-n8n.md` for detailed node descriptions.

### Node 1: Gmail Trigger
- **Type**: Gmail Trigger
- **Action**: Message Received
- **Filters**: filter by sender (your newsletter list)
- **Format**: RAW (to get the HTML)

### Node 2: Extract Links (Code node)

```javascript
// Parse the email HTML and extract links
const cheerio = require('cheerio');
const html = $input.first().json.raw;

const body = Buffer.from(html, 'base64').toString('utf-8');
const $ = cheerio.load(body);

const links = [];
const seen = new Set();

$('a[href]').each((i, el) => {
  const url = $(el).attr('href');
  const text = $(el).text().trim();

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

### Node 4: Prepare Output & Save (Code node)

```javascript
// Flatten output: data/raw/YYYY-MM-DD-newsletter-NN.json
const date = new Date().toISOString().split('T')[0];
const newsletter_name = $input.first().json.newsletter_name || 'Newsletter';

const output = {
  newsletter: newsletter_name,
  received_at: new Date().toISOString(),
  links: $input.all().map(item => ({
    url: item.json.url,
    title: item.json.title,
    content: item.json.data || item.json.body || ''
  }))
};

// n8n Write File node handles the actual write
return [{ json: { content: JSON.stringify(output, null, 2), date, newsletter_name } }];
```

### Node 5: Write File
- **File Path**: `/data/veille/raw/{{ $json.date }}-newsletter-01.json`
- **Content**: `{{ $json.content }}`

> **Note**: The Docker volume mounts the data directory so files written by n8n
> appear in `data/raw/` on your Mac. See `n8n/docker-compose.yml` for volume config.

---

## Step 4 — Set Up Notion

### Create the "Veille LinkedIn" Database

In your Notion workspace, create a database with these properties:
- **Titre** (title): article title
- **Date** (date): publication date
- **Status** (select): "A relire", "Valide", "Publie"
- **Theme** (select): "IA", "Leadership", "Data", "Tech"

### Connect the Notion MCP to Claude Code

The Notion MCP is available via Claude.ai's built-in integration. No additional setup needed if using Claude Max.

---

## Step 5 — Use Claude Code

```bash
# Navigate to the project
cd veilleur

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
1. Run `scripts/load_sources.py` to filter sources → you approve
2. Run `scripts/read_content.py` to read selected content
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
| Throughout the day | Newsletters arrive → n8n scrapes automatically | n8n |
| ~7 PM | `claude` → `/generate` | Claude Code + you (2 approvals) |
| ~7:15 PM | Notion review + Gemini image + LinkedIn publishing | You (~10 min) |

**Estimated daily time: 15-20 minutes** (vs ~1h+ previously)

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
ls data/raw/$(date +%Y-%m-%d)-newsletter-*.json
```

### The Notion MCP isn't responding
Check that the Notion integration is connected in your Claude.ai settings.
