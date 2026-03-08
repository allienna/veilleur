#!/usr/bin/env python3
"""
veilleur — Load and filter today's sources.

Usage:
    python3 scripts/load_sources.py 2026-03-07
    python3 scripts/load_sources.py  # defaults to today's date

Output: JSON on stdout with filtered and ranked sources.
"""

import json
import glob
import re
import sys
from datetime import date
from pathlib import Path

# Domains to filter out (marketing, sponsors, tracking)
SKIP_DOMAINS = [
    'plaid.com', 'go.clerk.com', 'webinars.atlassian.com',
    'advertise.tldr.tech', 'refer.tldr.tech', 'hub.sparklp.co',
    'email.beehiivstatus.com', 'beehiivstatus.com',
]

# Keywords in URL or title indicating sponsored/promotional content
SPONSOR_KEYWORDS = ['sponsor', 'Sponsor', 'paid', 'whitepaper', 'webinar']

# Keywords in content indicating a meta/promo page (not a real article)
META_KEYWORDS = [
    'hidden tracker', 'tracking pixel',
    'the newsletter platform built for',
    'subscribe to our newsletter',
]

# Themes in priority order — more specific keywords listed first
THEME_KEYWORDS = {
    'IA': [
        ' ai ', 'llm', 'gpt', 'claude', 'anthropic', 'openai', 'gemini',
        'machine learning', 'deep learning', 'neural', 'transformer',
        'language model', 'generative ai', 'gen ai', 'genai',
        'copilot', 'chatbot', 'prompt', 'fine-tun', 'rag ',
        'artificial intelligence', 'diffusion',
    ],
    'Leadership': [
        'leadership', 'engineering manager', 'tech lead', 'staff engineer',
        'principal engineer', 'director of engineering', 'vp of engineering',
        'team culture', 'hiring', 'one-on-one', '1:1', 'career growth',
        'mentoring', 'org design', 'management', 'asynchronous work',
        'remote work', 'developer productivity', 'developer experience',
        'tech specs', 'engineering team',
    ],
    'Data': [
        'database', 'sql', 'analytics', 'data pipeline', 'data warehouse',
        'bigquery', 'snowflake', 'dbt', 'spark', 'kafka', 'etl',
        'data engineering', 'data science', 'postgresql', 'mongodb',
    ],
    'Tech': [
        'rust', 'golang', 'typescript', 'kubernetes', 'docker',
        'microservice', 'architecture', 'open source', 'devops',
        'ci/cd', 'terraform', 'infrastructure', 'performance',
        'scalability', 'distributed system', 'system design',
    ],
}

# Minimum content length to be considered a real article
MIN_CONTENT_LENGTH = 500


def extract_title(title: str, content: str) -> str:
    """Extract the title from the title field or from the content."""
    if title and title.strip():
        return title.strip()

    if not content:
        return 'Sans titre'

    # Look for "Title: ..." in content (Jina Reader format)
    match = re.search(r'^Title:\s*(.+)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip()

    # Look for a markdown heading
    match = re.search(r'^#{1,3}\s+(.+)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip()

    # First non-empty line
    for line in content.split('\n'):
        line = line.strip()
        if line and not line.startswith('http') and len(line) > 10:
            return line[:120]

    return 'Sans titre'


def detect_theme(title: str, content: str) -> str:
    """Detect the main theme of a link (title + content, not the URL)."""
    # Clean content: strip URLs to avoid false positives
    clean_content = re.sub(r'https?://\S+', '', content[:1500])
    text = f" {title} {clean_content} ".lower()
    for theme, keywords in THEME_KEYWORDS.items():
        if any(kw in text for kw in keywords):
            return theme
    return 'Autre'


def is_filtered(url: str, title: str, content: str) -> tuple[bool, str]:
    """Check whether a link should be filtered out. Returns (filtered, reason)."""
    # Blocked domains
    if any(domain in url for domain in SKIP_DOMAINS):
        return True, 'domaine bloqué'

    # Sponsor keywords in URL or title
    text = f"{url} {title}"
    if any(kw in text for kw in SPONSOR_KEYWORDS):
        return True, 'sponsor'

    # Meta/promo content
    content_lower = content[:500].lower()
    if any(kw in content_lower for kw in META_KEYWORDS):
        return True, 'meta/promo'

    # Content too short (tracking pixel, redirects, etc.)
    if len(content) < MIN_CONTENT_LENGTH:
        return True, f'contenu trop court ({len(content)} chars)'

    return False, ''


def load_sources(target_date: str) -> dict:
    """Load and filter sources for a given date."""
    data_dir = Path(__file__).parent.parent / 'data' / 'raw'
    pattern = str(data_dir / f"{target_date}-newsletter-*.json")
    files = sorted(glob.glob(pattern))

    if not files:
        return {"date": target_date, "error": f"Aucun fichier trouvé pour {target_date}", "sources": []}

    all_links = []
    seen_urls = set()

    for filepath in files:
        with open(filepath, 'r') as f:
            data = json.load(f)

        newsletter = data.get('newsletter', 'unknown')
        for link in data.get('links', []):
            url = link.get('url', '')
            if url in seen_urls:
                continue
            seen_urls.add(url)

            raw_title = link.get('title', '')
            content = link.get('content', '')
            title = extract_title(raw_title, content)
            filtered, reason = is_filtered(url, title, content)
            theme = detect_theme(title, content)
            index = len(all_links)

            all_links.append({
                'index': index,
                'url': url,
                'title': title,
                'newsletter': newsletter,
                'theme': theme,
                'filtered': filtered,
                'filter_reason': reason,
                'content_length': len(content),
                'has_content': len(content) >= MIN_CONTENT_LENGTH,
            })

    # Separate kept and filtered sources
    kept = [l for l in all_links if not l['filtered']]
    filtered = [l for l in all_links if l['filtered']]

    # Sort by theme (IA first)
    theme_order = {'IA': 0, 'Leadership': 1, 'Data': 2, 'Tech': 3, 'Autre': 4}
    kept.sort(key=lambda x: theme_order.get(x['theme'], 99))

    return {
        "date": target_date,
        "files_loaded": len(files),
        "total_links": len(all_links),
        "kept": len(kept),
        "filtered": len(filtered),
        "sources": kept,
        "filtered_sources": filtered,
    }


if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else date.today().isoformat()
    result = load_sources(target)
    print(json.dumps(result, indent=2, ensure_ascii=False))
