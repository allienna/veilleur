# veilleur — Roadmap v2

## Phase 1 — Foundations (now → 2 weeks)
*Goal: stabilize the existing pipeline and build the data layer*

### 1.1 History & vector search
- Index every generated article + its sources into a vector database (ChromaDB locally or Qdrant in Docker)
- On each `/generate`, the pipeline can search "what have I written about recently on this topic" to avoid duplicates and enrich transitions
- `/search [query]` command in Claude Code to query the history
- Stack: ChromaDB (Python, zero config, local files) + embeddings via Claude API or a local model

### 1.2 Multi-newsletter intelligence
- After scraping, a `detect_trends.py` script cross-references all sources of the day
- Trend detection: when 2+ newsletters mention the same topic/URL/entity → strong signal
- Output: a "trend score" per source, used by Claude Code to guide the narrative thread
- `/generate` displays trend clusters before proposing the angle

### 1.3 LinkedIn metrics
- `linkedin_metrics.py` script that scrapes post stats (likes, comments, reposts)
- Storage in a local JSON or SQLite, per article/date
- Theme × engagement correlation to identify what resonates
- Feedback loop: `/generate` can say "AI agent articles get 3x more engagement than data articles"

---

## Phase 2 — Talk & article (week 3-4)
*Goal: capitalize on the use case*

### 2.1 Meta LinkedIn article
- Use veilleur to write the article about veilleur
- Angle: "I automated my tech watch end-to-end — here's what I learned"
- Include the architecture diagram, metrics (time saved, number of sources processed)
- Tease the GitHub repo

### 2.2 Talk (DevFest Lille, Meetup)
- 20-30 min format: "From newsletter to LinkedIn post in 15 minutes — n8n, Claude Code, and a bit of glue"
- Live demo of the pipeline
- Lessons learned (NotebookLM ignoring instructions, Docker/n8n pitfalls, flat structure)

---

## Phase 3 — Lightweight SaaS (month 2-3)
*Goal: open the project to other users*

### 3.1 Target architecture

```
┌─────────────────────────────────────────────────────┐
│                    Frontend (Next.js)                │
│  Dashboard: daily sources, article preview,         │
│  LinkedIn metrics, history                          │
└──────────────┬──────────────────────────┬───────────┘
               │                          │
    ┌──────────▼──────────┐    ┌─────────▼──────────┐
    │   Backend API       │    │   n8n (ingestion)   │
    │   (Next.js API /    │    │   Gmail → scraping  │
    │    FastAPI)          │    │   → storage         │
    └──────────┬──────────┘    └────────────────────┘
               │
    ┌──────────▼──────────┐
    │   Claude Code       │
    │   (CLI, driven by   │
    │   the backend API)  │
    └──────────┬──────────┘
               │
    ┌──────────▼──────────┐
    │   Storage            │
    │   - SQLite/Postgres  │
    │   - ChromaDB (vecs)  │
    │   - Output files     │
    └──────────────────────┘
```

### 3.2 Claude Code as AI engine
The key point: keep Claude Code (not the API directly) for generation.
- The backend API calls Claude Code as a subprocess: `claude --print --allowedTools "..." -p "generate article for 2026-03-15"`
- Claude Code has access to the filesystem, scripts, Notion MCP → all the richness we've built
- The frontend simply orchestrates and displays results
- Advantage: no API key to manage, included in the Max subscription

### 3.3 Lightweight multi-tenant
- Each user connects their Gmail (OAuth) + their Notion
- One profile per user: writing style, priority themes, custom prompt
- CLAUDE.md is templated per user
- n8n manages N workflows (one per user) or a shared workflow with routing

### 3.4 Integrated LinkedIn metrics
- Dashboard with engagement stats per article
- Trend charts (which themes perform best)
- Automatic suggestions: "This week, AI articles outperformed → favor this angle"

---

## Backlog — ideas to explore

- **Automatic image generation**: Gemini API call (Imagen) instead of manually copying the prompt
- **Automatic LinkedIn scheduling**: use the LinkedIn API to schedule the post directly
- **Personal newsletter**: generate a personal newsletter from veilleur (Substack, Buttondown)
- **Collaborative watch**: multiple contributors add sources, a shared article is generated
- **Style fine-tuning**: after 50+ articles, fine-tune a lightweight model on your writing style so the first draft is closer to the final result
