#!/usr/bin/env python3
"""
veilleur — Cross-newsletter trend detection.

Usage:
    python3 scripts/detect_trends.py 2026-03-07
    python3 scripts/detect_trends.py  # defaults to today's date

Output: JSON on stdout with trend clusters and scores.
"""

import glob as globmod
import json
import re
import sys
from collections import Counter, deque
from datetime import date
from pathlib import Path
from urllib.parse import urlparse, parse_qs, urlencode

# Import filtering functions from sibling script
sys.path.insert(0, str(Path(__file__).parent))
from load_sources import extract_title, detect_theme, is_filtered

STOPWORDS = {
    # English
    'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
    'of', 'with', 'by', 'from', 'is', 'it', 'as', 'be', 'was', 'are',
    'been', 'has', 'have', 'had', 'do', 'does', 'did', 'will', 'would',
    'could', 'should', 'may', 'might', 'can', 'this', 'that', 'these',
    'those', 'not', 'no', 'so', 'if', 'than', 'too', 'very', 'just',
    'about', 'up', 'out', 'how', 'what', 'when', 'where', 'who', 'which',
    'why', 'all', 'each', 'every', 'both', 'more', 'most', 'other', 'some',
    'such', 'into', 'over', 'after', 'before', 'between', 'under', 'again',
    'then', 'here', 'there', 'new', 'also', 'its', 'your', 'you', 'we',
    'our', 'their', 'they', 'he', 'she', 'his', 'her', 'my', 'me',
    # French
    'le', 'la', 'les', 'un', 'une', 'des', 'du', 'de', 'et', 'ou', 'mais',
    'dans', 'sur', 'pour', 'par', 'avec', 'est', 'sont', 'être', 'avoir',
    'pas', 'plus', 'ce', 'cette', 'ces', 'qui', 'que', 'quoi', 'comment',
    'nous', 'vous', 'ils', 'elles', 'son', 'sa', 'ses', 'aux', 'en',
}

# UTM and tracking parameters to strip from URLs
UTM_PARAMS = {'utm_source', 'utm_medium', 'utm_campaign', 'utm_term',
              'utm_content', 'ref', 'source', 'mc_cid', 'mc_eid'}


def normalize_url(url: str) -> str:
    """Normalize URL: strip UTM params, www, trailing slash, force https."""
    parsed = urlparse(url)
    host = parsed.hostname or ''
    host = re.sub(r'^www\.', '', host)
    # Strip tracking query params
    params = parse_qs(parsed.query, keep_blank_values=True)
    cleaned = {k: v for k, v in params.items() if k.lower() not in UTM_PARAMS}
    query = urlencode(cleaned, doseq=True) if cleaned else ''
    path = parsed.path.rstrip('/')
    return f"https://{host}{path}{'?' + query if query else ''}"


def tokenize(text: str) -> list[str]:
    """Extract lowercase word tokens from text."""
    return re.findall(r'[a-zA-ZÀ-ÿ0-9]{3,}', text.lower())


def extract_keywords(title: str, content: str, top_n: int = 15) -> set[str]:
    """Extract top N keywords from title + content, excluding stopwords."""
    # Use title (weighted x3) + first 2000 chars of content
    text = (title + ' ') * 3 + (content[:2000] if content else '')
    words = [w for w in tokenize(text) if w not in STOPWORDS and len(w) > 2]
    counts = Counter(words)
    return {word for word, _ in counts.most_common(top_n)}


def compute_title_similarity(title_a: str, title_b: str) -> float:
    """Jaccard similarity on word sets of two titles."""
    words_a = set(tokenize(title_a)) - STOPWORDS
    words_b = set(tokenize(title_b)) - STOPWORDS
    if not words_a or not words_b:
        return 0.0
    intersection = words_a & words_b
    union = words_a | words_b
    return len(intersection) / len(union)


def compute_keyword_overlap(kw_a: set[str], kw_b: set[str]) -> float:
    """Overlap ratio between two keyword sets."""
    if not kw_a or not kw_b:
        return 0.0
    overlap = len(kw_a & kw_b)
    min_size = min(len(kw_a), len(kw_b))
    return overlap / min_size


def build_similarity_graph(sources: list[dict], contents: dict[int, str]) -> dict[int, set[int]]:
    """Build adjacency graph with edges between cross-publisher similar sources."""
    n = len(sources)
    graph: dict[int, set[int]] = {i: set() for i in range(n)}

    # Precompute normalized URLs and keywords
    norm_urls = [normalize_url(s['url']) for s in sources]
    keywords = [extract_keywords(s['title'], contents.get(s['index'], '')) for s in sources]

    for i in range(n):
        for j in range(i + 1, n):
            # Only cross-publisher comparisons (same publisher = not a real trend)
            if sources[i]['publisher'] == sources[j]['publisher']:
                continue

            # Layer 1: URL match
            url_match = 1.0 if norm_urls[i] == norm_urls[j] else 0.0

            # Layer 2: Title similarity (Jaccard)
            title_sim = compute_title_similarity(sources[i]['title'], sources[j]['title'])

            # Layer 3: Keyword overlap count
            kw_common = len(keywords[i] & keywords[j])

            # Check thresholds — any layer above threshold creates an edge
            if url_match > 0 or title_sim >= 0.4 or kw_common >= 5:
                graph[i].add(j)
                graph[j].add(i)

    return graph


def find_clusters(graph: dict[int, set[int]]) -> list[set[int]]:
    """Find connected components via BFS."""
    visited = set()
    clusters = []
    for node in graph:
        if node in visited or not graph[node]:
            continue
        # BFS
        cluster = set()
        queue = deque([node])
        while queue:
            current = queue.popleft()
            if current in visited:
                continue
            visited.add(current)
            cluster.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)
        if len(cluster) > 1:
            clusters.append(cluster)
    return clusters


def generate_cluster_label(cluster_sources: list[dict]) -> str:
    """Generate a label from the most frequent title terms across cluster sources."""
    all_words = []
    for s in cluster_sources:
        words = [w for w in tokenize(s['title']) if w not in STOPWORDS and len(w) > 2]
        all_words.extend(words)
    counts = Counter(all_words)
    top = [word for word, _ in counts.most_common(3)]
    return ' '.join(top) if top else 'trend'


def compute_trend_score(source_idx: int, sources: list[dict],
                        cluster: set[int],
                        norm_urls: list[str],
                        keywords: list[set[str]]) -> float:
    """Compute trend score for a source within its cluster."""
    src = sources[source_idx]

    best_url = 0.0
    best_title = 0.0
    best_kw = 0.0

    for other_idx in cluster:
        if other_idx == source_idx:
            continue
        other = sources[other_idx]
        if other['publisher'] == src['publisher']:
            continue

        if norm_urls[other_idx] == norm_urls[source_idx]:
            best_url = 1.0

        title_sim = compute_title_similarity(src['title'], other['title'])
        best_title = max(best_title, title_sim)

        kw_ov = compute_keyword_overlap(keywords[source_idx], keywords[other_idx])
        best_kw = max(best_kw, kw_ov)

    return min(1.0, best_url * 0.5 + best_title * 0.3 + best_kw * 0.2)


def extract_publisher(filepath: str, target_date: str) -> str:
    """Extract publisher name from filename, e.g. 'tldrnewsletter' from
    '2026-03-09-newsletter-tldrnewsletter-1009.json'."""
    stem = Path(filepath).stem  # e.g. '2026-03-09-newsletter-tldrnewsletter-1009'
    prefix = f"{target_date}-newsletter-"
    rest = stem[len(prefix):]  # e.g. 'tldrnewsletter-1009' or 'manual'
    # Strip trailing 4-digit time suffix if present
    parts = rest.rsplit('-', 1)
    if len(parts) == 2 and parts[1].isdigit() and len(parts[1]) == 4:
        return parts[0]
    return rest


def load_all_sources(target_date: str) -> tuple[list[dict], dict[int, str]]:
    """Load sources per-newsletter WITHOUT cross-newsletter URL dedup.

    Returns (sources, contents) where each source keeps its newsletter origin.
    Same URL in different newsletters = separate entries (needed for trend detection).
    Intra-newsletter dedup and filtering are still applied.
    """
    data_dir = Path(__file__).parent.parent / 'data' / 'raw'
    pattern = str(data_dir / f"{target_date}-newsletter-*.json")
    files = sorted(globmod.glob(pattern))

    sources: list[dict] = []
    contents: dict[int, str] = {}

    for filepath in files:
        with open(filepath, 'r') as f:
            data = json.load(f)

        newsletter = data.get('newsletter', 'unknown')
        publisher = extract_publisher(filepath, target_date)
        seen_in_newsletter: set[str] = set()

        for link in data.get('links', []):
            url = link.get('url', '')
            norm = normalize_url(url)
            if norm in seen_in_newsletter:
                continue
            seen_in_newsletter.add(norm)

            raw_title = link.get('title', '')
            content = link.get('content', '')
            title = extract_title(raw_title, content)
            filtered, _ = is_filtered(url, title, content)
            if filtered:
                continue

            idx = len(sources)
            theme = detect_theme(title, content)
            sources.append({
                'index': idx,
                'url': url,
                'title': title,
                'newsletter': newsletter,
                'publisher': publisher,
                'theme': theme,
            })
            contents[idx] = content

    return sources, contents


def detect_trends(target_date: str) -> dict:
    """Main orchestrator: load sources, detect trends, output structured JSON."""
    sources, contents = load_all_sources(target_date)

    if not sources:
        return {
            "date": target_date,
            "sources_analyzed": 0,
            "newsletters_count": 0,
            "trends": [],
            "unclustered": [],
        }

    newsletters = sorted({s['newsletter'] for s in sources})

    # Precompute normalized URLs and keywords for reuse
    norm_urls = [normalize_url(s['url']) for s in sources]
    keywords = [extract_keywords(s['title'], contents.get(s['index'], '')) for s in sources]

    # Build similarity graph and find clusters
    graph = build_similarity_graph(sources, contents)
    clusters = find_clusters(graph)

    # Filter clusters: must span 2+ newsletters
    trends = []
    clustered_indices = set()

    for cluster_id, cluster in enumerate(clusters):
        cluster_sources = [sources[i] for i in cluster]
        cluster_publishers = sorted({s['publisher'] for s in cluster_sources})
        if len(cluster_publishers) < 2:
            continue
        cluster_newsletters = sorted({s['newsletter'] for s in cluster_sources})

        clustered_indices.update(cluster)
        label = generate_cluster_label(cluster_sources)

        # Determine theme from majority
        theme_counts = Counter(s['theme'] for s in cluster_sources)
        theme = theme_counts.most_common(1)[0][0]

        # Compute per-source trend scores
        source_entries = []
        scores = []
        for i in cluster:
            score = compute_trend_score(i, sources, cluster, norm_urls, keywords)
            scores.append(score)
            source_entries.append({
                "index": sources[i]['index'],
                "title": sources[i]['title'],
                "newsletter": sources[i]['newsletter'],
                "trend_score": round(score, 2),
            })

        cluster_score = round(max(scores) if scores else 0.0, 2)
        trends.append({
            "id": cluster_id,
            "label": label,
            "theme": theme,
            "score": cluster_score,
            "publishers": cluster_publishers,
            "newsletters": cluster_newsletters,
            "sources": source_entries,
        })

    # Sort trends by score descending
    trends.sort(key=lambda t: t['score'], reverse=True)
    # Re-number IDs after sorting
    for i, t in enumerate(trends):
        t['id'] = i

    # Unclustered sources
    unclustered = []
    for i, s in enumerate(sources):
        if i not in clustered_indices:
            unclustered.append({
                "index": s['index'],
                "title": s['title'],
                "newsletter": s['newsletter'],
                "theme": s['theme'],
                "trend_score": 0.0,
            })

    return {
        "date": target_date,
        "sources_analyzed": len(sources),
        "newsletters_count": len(newsletters),
        "trends": trends,
        "unclustered": unclustered,
    }


if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else date.today().isoformat()
    output = detect_trends(target)
    print(json.dumps(output, indent=2, ensure_ascii=False))
