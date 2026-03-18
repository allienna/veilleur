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

# Load and filter sources for a given date (DATE=YYYY-MM-DD, defaults to today, CARRY=N days carry-forward)
sources DATE="" CARRY="0":
    uv run python3 scripts/load_sources.py {{ if DATE == "" { `date +%Y-%m-%d` } else { DATE } }} {{ if CARRY != "0" { "--carry-forward " + CARRY } else { "" } }}

# Add a manually found link to the day's sources (fetches via Jina Reader)
add-link DATE URL:
    uv run python3 scripts/add_link.py {{ DATE }} "{{ URL }}"

# Read full content of sources at given indices (e.g. just read-content 2026-03-07 0 1 2, CARRY=N for carry-forward)
read-content DATE +INDICES_AND_OPTS:
    uv run python3 scripts/read_content.py {{ DATE }} {{ INDICES_AND_OPTS }}

# Detect cross-newsletter trends for a given date (DATE=YYYY-MM-DD, defaults to today, CARRY=N days carry-forward)
detect-trends DATE="" CARRY="0":
    uv run python3 scripts/detect_trends.py {{ if DATE == "" { `date +%Y-%m-%d` } else { DATE } }} {{ if CARRY != "0" { "--carry-forward " + CARRY } else { "" } }}

# Save the list of processed raw files after article generation
save-processed DATE +FILES:
    uv run python3 scripts/save_processed_files.py {{ DATE }} {{ FILES }}

# Add an image for a given date (copies to site/public/images/DATE.png)
add-image DATE FILE:
    mkdir -p site/public/images
    cp "{{ FILE }}" "site/public/images/{{ DATE }}.png"
    @echo "Image saved to site/public/images/{{ DATE }}.png"

# Add an image for a blog post (copies to site/public/images/SLUG.png)
add-blog-image SLUG FILE:
    mkdir -p site/public/images
    cp "{{ FILE }}" "site/public/images/{{ SLUG }}.png"
    @echo "Image saved to site/public/images/{{ SLUG }}.png"

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

# Show engagement insights formatted for /generate injection
insights-for-generate:
    uv run python3 scripts/metrics_insights.py --for-generate

# ── Site ──────────────────────────────────────────────────────────

# Start the Astro site locally (dev server)
site:
    cd site && npm install && npm run dev

# Export ChromaDB + SQLite data to JSON for the Astro site
export-site-data:
    uv run python3 scripts/export_site_data.py

# ── NotebookLM ──────────────────────────────────────────────────────

# Create a NotebookLM notebook from daily sources (DATE=YYYY-MM-DD, defaults to today)
notebook DATE="" *FLAGS="":
    uv run python3 scripts/create_notebook.py {{ if DATE == "" { `date +%Y-%m-%d` } else { DATE } }} {{ FLAGS }}

# ── Sentinel (automation) ──────────────────────────────────────────

# Install sentinel and autopublish launchd agents
sentinel-install:
    mkdir -p data/logs
    cp launchd/com.veilleur.sentinel.plist ~/Library/LaunchAgents/
    cp launchd/com.veilleur.autopublish.plist ~/Library/LaunchAgents/
    launchctl load ~/Library/LaunchAgents/com.veilleur.sentinel.plist
    launchctl load ~/Library/LaunchAgents/com.veilleur.autopublish.plist
    @echo "Sentinel (20h) and autopublish (23h) installed"

# Check sentinel status
sentinel-status:
    @echo "=== Sentinel (20h) ==="
    @launchctl list | grep com.veilleur.sentinel || echo "Not loaded"
    @echo "=== Autopublish (23h) ==="
    @launchctl list | grep com.veilleur.autopublish || echo "Not loaded"
    @echo "=== Recent logs ==="
    @ls -la data/logs/*-sentinel.log 2>/dev/null | tail -3 || echo "No sentinel logs"
    @ls -la data/logs/*-autopublish.log 2>/dev/null | tail -3 || echo "No autopublish logs"

# Show sentinel logs for a date (defaults to today)
sentinel-logs DATE="":
    @cat data/logs/{{ if DATE == "" { `date +%Y-%m-%d` } else { DATE } }}-sentinel.log 2>/dev/null || echo "No sentinel log"
    @echo "---"
    @cat data/logs/{{ if DATE == "" { `date +%Y-%m-%d` } else { DATE } }}-autopublish.log 2>/dev/null || echo "No autopublish log"

# Stop all sentinel agents
sentinel-stop:
    launchctl unload ~/Library/LaunchAgents/com.veilleur.sentinel.plist 2>/dev/null || true
    launchctl unload ~/Library/LaunchAgents/com.veilleur.autopublish.plist 2>/dev/null || true
    @echo "Sentinel agents stopped"

# Run sentinel manually for a specific date (for testing)
sentinel-run DATE="":
    uv run python3 scripts/sentinel.py {{ if DATE == "" { "" } else { "--date " + DATE } }}

# Generate image from prompt file via Gemini API
generate-image DATE:
    uv run python3 scripts/generate_image.py {{ DATE }}

# Generate Instagram carousel + reel from article
instagram DATE="":
    uv run python3 scripts/generate_instagram.py {{ if DATE == "" { `date +%Y-%m-%d` } else { DATE } }}

# Generate Instagram carousel only (no reel)
instagram-carousel DATE="":
    uv run python3 scripts/generate_instagram.py {{ if DATE == "" { `date +%Y-%m-%d` } else { DATE } }} --carousel-only

# Install Playwright browser (one-time setup)
instagram-setup:
    uv run playwright install chromium

# ── Tests ─────────────────────────────────────────────────────────

# Run all tests
test:
    uv run python3 -m pytest tests/ -v

# Run tests for a specific file
test-file FILE:
    uv run python3 -m pytest {{ FILE }} -v
