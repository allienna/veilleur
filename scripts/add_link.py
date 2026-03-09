"""Add a manually found link to the day's sources.

Fetches content via Jina Reader and appends to a manual newsletter JSON file
that is automatically picked up by load_sources.py.

Usage:
    python3 scripts/add_link.py DATE URL [--title "Optional title"]
"""

import json
import sys
import urllib.request
from datetime import date
from pathlib import Path

DATA_RAW = Path("data/raw")
JINA_BASE = "https://r.jina.ai/"
NEWSLETTER_NAME = "Manuel"


def fetch_content(url: str) -> str:
    """Fetch page content via Jina Reader."""
    jina_url = JINA_BASE + url
    req = urllib.request.Request(
        jina_url,
        headers={"Accept": "text/plain", "User-Agent": "veilleur/1.0"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8")


def main():
    args = sys.argv[1:]

    # Parse --title flag
    title_override = None
    filtered_args = []
    i = 0
    while i < len(args):
        if args[i] == "--title" and i + 1 < len(args):
            title_override = args[i + 1]
            i += 2
        else:
            filtered_args.append(args[i])
            i += 1

    if len(filtered_args) < 2:
        print(
            json.dumps(
                {"error": "Usage: add_link.py DATE URL [--title 'Optional title']"}
            )
        )
        sys.exit(1)

    target_date = filtered_args[0]
    url = filtered_args[1]

    manual_path = DATA_RAW / f"{target_date}-newsletter-manual.json"

    # Load existing manual file or start fresh
    if manual_path.exists():
        with open(manual_path) as f:
            data = json.load(f)
    else:
        data = {
            "newsletter": NEWSLETTER_NAME,
            "received_at": f"{target_date}T00:00:00Z",
            "links": [],
        }

    # Check for duplicate URL
    existing_urls = {link["url"] for link in data["links"]}
    if url in existing_urls:
        print(json.dumps({"status": "skipped", "message": "URL already added", "url": url}))
        return

    # Fetch content
    print(f"Fetching {url} ...", file=sys.stderr)
    try:
        content = fetch_content(url)
    except Exception as e:
        print(json.dumps({"error": f"Failed to fetch content: {e}", "url": url}))
        sys.exit(1)

    link = {
        "url": url,
        "title": title_override or "",
        "content": content,
    }
    data["links"].append(link)

    DATA_RAW.mkdir(parents=True, exist_ok=True)
    with open(manual_path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(
        json.dumps(
            {
                "status": "added",
                "url": url,
                "file": str(manual_path),
                "total_manual_links": len(data["links"]),
                "content_length": len(content),
            }
        )
    )


if __name__ == "__main__":
    main()
