# veilleur

Automated tech watch pipeline → daily LinkedIn article.

**n8n** ingests and scrapes newsletters, **Claude Code** generates the article, **Notion** serves as the review room.

## Architecture

```
📧 Gmail (newsletters)
    ↓ n8n (automatic trigger)
🔗 Link extraction + scraping (Jina Reader)
    ↓ /Users/sn0rks/Code/github.com/allienna/veilleur/data/YYYY-MM-DD/raw/
🧠 Claude Code (/generate)
    ↓ Filtering → Writing → Formatting
📋 Notion (review)
    ↓ You (~10 min)
📰 LinkedIn (article + post scheduled at 8:45 AM)
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
cd ../claude-code
claude
/sources          # View today's watch
/generate         # Generate article → Notion
```

## Structure

```
veilleur/
├── README.md
├── SETUP.md                          # Detailed setup guide
├── n8n/
│   └── docker-compose.yml            # n8n running locally
├── claude-code/
│   ├── CLAUDE.md                     # Claude Code project instructions
│   └── .claude/
│       └── commands/
│           ├── generate.md           # /generate — article generation
│           └── sources.md            # /sources — daily watch overview
└── data/                             # Automatically created by n8n
    └── YYYY-MM-DD/
        └── raw/
            └── newsletter-*.json
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
