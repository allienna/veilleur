# Show available recipes (default)
default:
    @just --list

# ── Infrastructure ────────────────────────────────────────────────

# Start n8n in background (starts Colima if needed)
start-n8n:
    @if ! colima status 2>/dev/null | grep -q "Running"; then \
        echo "Starting Colima..."; \
        colima start --memory 8; \
    fi
    cd n8n && docker-compose up -d

# Restart n8n
restart-n8n:
    cd n8n && docker-compose down && docker-compose up -d

# ── Sources & generation ──────────────────────────────────────────

# Load and filter sources for a given date (DATE=YYYY-MM-DD, defaults to today)
sources DATE="":
    uv run python3 scripts/load_sources.py {{ if DATE == "" { `date +%Y-%m-%d` } else { DATE } }}

# Read full content of sources at given indices (e.g. just read-content 2026-03-07 0 1 2)
read-content DATE +INDICES:
    uv run python3 scripts/read_content.py {{ DATE }} {{ INDICES }}

# ── History & search ──────────────────────────────────────────────

# Index an article into ChromaDB (DATE=YYYY-MM-DD, defaults to today)
index DATE="":
    uv run python3 scripts/index_article.py {{ if DATE == "" { `date +%Y-%m-%d` } else { DATE } }}

# Index all existing articles into ChromaDB (backfill)
index-all:
    uv run python3 scripts/index_all.py

# Semantic search across article history
search QUERY LIMIT="5":
    uv run python3 scripts/search_history.py "{{ QUERY }}" --limit {{ LIMIT }}

# ── LinkedIn metrics ──────────────────────────────────────────────

# Record metrics for a post (e.g. just metrics 2026-03-07 42 8 3)
metrics DATE LIKES COMMENTS REPOSTS:
    uv run python3 scripts/track_metrics.py {{ DATE }} --likes {{ LIKES }} --comments {{ COMMENTS }} --reposts {{ REPOSTS }}

# Show metrics for a given article date
metrics-show DATE:
    uv run python3 scripts/track_metrics.py {{ DATE }} --show

# List recent metrics
metrics-list:
    uv run python3 scripts/track_metrics.py --list

# Find the latest article without recorded metrics
metrics-untracked:
    uv run python3 scripts/track_metrics.py --latest-untracked

# Import metrics from a CSV file
metrics-import CSV:
    uv run python3 scripts/track_metrics.py --import-csv {{ CSV }}

# Show engagement insights report (themes, trends, recommendations)
insights:
    uv run python3 scripts/metrics_insights.py

# ── Tests ─────────────────────────────────────────────────────────

# Run all tests
test:
    uv run python3 -m pytest tests/ -v

# Run tests for a specific file
test-file FILE:
    uv run python3 -m pytest {{ FILE }} -v
