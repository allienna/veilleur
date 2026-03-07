# veilleur

Automated tech watch pipeline → daily LinkedIn article.

**n8n** ingests and scrapes newsletters, **Claude Code** generates the article, **Notion** serves as the review room.

## Architecture

```
Gmail (newsletters)
    ↓ n8n (automatic trigger)
Link extraction + scraping (Jina Reader)
    ↓ data/raw/
Claude Code (/generate)
    ↓ Filtering → Writing → Formatting
Notion (review)
    ↓ You (~10 min)
LinkedIn (article + post scheduled at 8:45 AM)
```

## Quickstart

```bash
# 1. Clone
git clone https://github.com/allienna/veilleur.git
cd veilleur

# 2. Start n8n
cd n8n && docker-compose up -d
# → http://localhost:5678

# 3. Configure the n8n workflow (see SETUP.md step 3)

# 4. Use Claude Code
claude
/sources          # View today's watch
/generate         # Generate article → Notion
```

## Structure

```
veilleur/
├── README.md
├── SETUP.md                          # Detailed setup guide
├── CLAUDE.md                         # Claude Code project instructions
├── .claude/
│   └── commands/
│       ├── generate.md               # /generate — article generation
│       └── sources.md                # /sources — daily watch overview
├── scripts/
│   ├── load_sources.py               # Load & filter sources (JSON output)
│   └── read_content.py               # Read full content of selected sources
├── docs/
│   ├── n8n-google-cloud-setup.md     # n8n & Google Cloud OAuth2 setup
│   └── workflow-n8n.md               # n8n workflow documentation
├── n8n/
│   ├── docker-compose.yml            # n8n running locally
│   └── workflow-veilleur.json        # n8n workflow export
└── data/                             # Scraped data and generated articles
    ├── raw/                          # Raw newsletter files from n8n
    │   └── YYYY-MM-DD-newsletter-*.json
    └── output/                       # Generated articles
        ├── YYYY-MM-DD-article.md
        ├── YYYY-MM-DD-post.md
        └── YYYY-MM-DD-image-prompt.md
```

## Stack

| Component | Role | Cost |
|-----------|------|------|
| n8n (Docker) | Newsletter ingestion + scraping | Free |
| Jina Reader | Web scraping → markdown | Free (~200 req/day) |
| Claude Code (Max) | Sorting, writing, formatting, Notion push | Included in subscription |
| Notion | Review + validation | Free |
| Gemini (Nano Banana) | Image generation | Included in Workspace |

## License

MIT
