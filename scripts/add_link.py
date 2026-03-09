"""Add a manually found link to the day's sources.

Fetches content via Jina Reader and appends to a manual newsletter JSON file
that is automatically picked up by load_sources.py.

Usage:
    python3 scripts/add_link.py DATE URL [--title "Optional title"]
"""

import argparse
import json
import sys
import urllib.request
from pathlib import Path

DATA_RAW = Path(__file__).parent.parent / "data" / "raw"
JINA_BASE = "https://r.jina.ai/"
NEWSLETTER_NAME = "Manuel"


def fetch_content(url: str) -> str:
    """Fetch page content via Jina Reader."""
    jina_url = JINA_BASE + url
    req = urllib.request.Request(
        jina_url,
        headers={"Accept": "text/markdown", "User-Agent": "veilleur/1.0"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8")


def main():
    parser = argparse.ArgumentParser(
        description="Add a manually found link to the day's sources."
    )
    parser.add_argument("date", help="Target date (YYYY-MM-DD)")
    parser.add_argument("url", help="URL to add")
    parser.add_argument("--title", default="", help="Optional title override")
    args = parser.parse_args()

    manual_path = DATA_RAW / f"{args.date}-newsletter-manual.json"

    # Load existing manual file or start fresh
    if manual_path.exists():
        with open(manual_path) as f:
            data = json.load(f)
    else:
        data = {
            "newsletter": NEWSLETTER_NAME,
            "received_at": f"{args.date}T00:00:00Z",
            "links": [],
        }

    # Check for duplicate URL
    existing_urls = {link["url"] for link in data["links"]}
    if args.url in existing_urls:
        print(json.dumps({"status": "skipped", "message": "URL already added", "url": args.url}))
        return

    # Fetch content
    print(f"Fetching {args.url} ...", file=sys.stderr)
    try:
        content = fetch_content(args.url)
    except Exception as e:
        print(json.dumps({"error": f"Failed to fetch content: {e}", "url": args.url}))
        sys.exit(1)

    link = {
        "url": args.url,
        "title": args.title,
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
                "url": args.url,
                "file": str(manual_path),
                "total_manual_links": len(data["links"]),
                "content_length": len(content),
            }
        )
    )


if __name__ == "__main__":
    main()
