#!/usr/bin/env python3
"""
veilleur — Analyse des métriques LinkedIn et insights d'engagement.

Usage:
    python3 scripts/metrics_insights.py
    python3 scripts/metrics_insights.py --themes
    python3 scripts/metrics_insights.py --for-generate

Sortie:
    - Par défaut et avec --themes: JSON sur stdout.
    - Avec --for-generate: texte brut sur stdout (rien si vide).
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from metrics_db import get_all_metrics


def compute_engagement_score(likes=0, comments=0, reposts=0):
    """Score d'engagement pondéré. Comments et reposts pèsent plus."""
    return likes + comments * 3 + reposts * 5


def theme_performance(db_path=None, _metrics=None):
    """Agrège l'engagement par thème."""
    all_metrics = _metrics or get_all_metrics(limit=1000, db_path=db_path)

    if not all_metrics:
        return []

    theme_data = {}
    for m in all_metrics:
        score = compute_engagement_score(m['likes'], m['comments'], m['reposts'])
        themes = m['themes'].split(',')
        for theme in themes:
            theme = theme.strip()
            if not theme:
                continue
            if theme not in theme_data:
                theme_data[theme] = {'scores': [], 'likes': [], 'comments': [], 'reposts': []}
            theme_data[theme]['scores'].append(score)
            theme_data[theme]['likes'].append(m['likes'])
            theme_data[theme]['comments'].append(m['comments'])
            theme_data[theme]['reposts'].append(m['reposts'])

    results = []
    for theme, data in theme_data.items():
        count = len(data['scores'])
        avg_engagement = round(sum(data['scores']) / count, 1)
        results.append({
            "theme": theme,
            "total_articles": count,
            "avg_engagement": avg_engagement,
            "avg_likes": round(sum(data['likes']) / count, 1),
            "avg_comments": round(sum(data['comments']) / count, 1),
            "avg_reposts": round(sum(data['reposts']) / count, 1),
        })

    results.sort(key=lambda x: x['avg_engagement'], reverse=True)
    return results


def top_performing_articles(limit=5, db_path=None, _metrics=None):
    """Retourne les articles les plus performants par engagement."""
    all_metrics = _metrics or get_all_metrics(limit=1000, db_path=db_path)

    if not all_metrics:
        return []

    scored = []
    for m in all_metrics:
        score = compute_engagement_score(m['likes'], m['comments'], m['reposts'])
        scored.append({
            "date": m['date'],
            "title": m['title'],
            "themes": m['themes'],
            "engagement": score,
            "likes": m['likes'],
            "comments": m['comments'],
            "reposts": m['reposts'],
        })

    scored.sort(key=lambda x: x['engagement'], reverse=True)
    return scored[:limit]


def generate_insights(db_path=None):
    """Produit un rapport d'insights structuré."""
    all_metrics = get_all_metrics(limit=1000, db_path=db_path)

    if not all_metrics:
        return {"total_articles_tracked": 0, "theme_ranking": [], "recommendations": []}

    themes = theme_performance(_metrics=all_metrics)
    top = top_performing_articles(limit=1, _metrics=all_metrics)

    # Calculate overall average engagement
    scores = [compute_engagement_score(m['likes'], m['comments'], m['reposts']) for m in all_metrics]
    overall_avg = sum(scores) / len(scores) if scores else 0

    # Add multiplier vs average to theme ranking
    # Use unrounded multiplier for threshold logic, round only for display
    theme_ranking = []
    for t in themes:
        multiplier_raw = t['avg_engagement'] / overall_avg if overall_avg > 0 else 0
        theme_ranking.append({**t, "multiplier_vs_avg": round(multiplier_raw, 1)})

    # Generate recommendations
    recommendations = []
    for t in theme_ranking:
        raw = t['avg_engagement'] / overall_avg if overall_avg > 0 else 0
        if raw >= 1.5:
            recommendations.append(f"Les articles {t['theme']} obtiennent {t['multiplier_vs_avg']}x plus d'engagement que la moyenne")
        elif raw <= 0.5 and t['total_articles'] >= 2:
            recommendations.append(f"Les articles {t['theme']} sous-performent — considérer un angle différent")

    # Trend: compare last 7 vs previous 7
    trend = {}
    sorted_by_date = sorted(all_metrics, key=lambda x: x['date'], reverse=True)
    if len(sorted_by_date) >= 4:
        mid = min(7, len(sorted_by_date) // 2)
        recent = sorted_by_date[:mid]
        previous = sorted_by_date[mid:mid*2]

        recent_avg = sum(compute_engagement_score(m['likes'], m['comments'], m['reposts']) for m in recent) / len(recent)
        previous_avg = sum(compute_engagement_score(m['likes'], m['comments'], m['reposts']) for m in previous) / len(previous)

        trend = {
            "direction": "up" if recent_avg > previous_avg else "down" if recent_avg < previous_avg else "stable",
            "recent_avg": round(recent_avg, 1),
            "previous_avg": round(previous_avg, 1),
        }

    result = {
        "total_articles_tracked": len(all_metrics),
        "overall_avg_engagement": round(overall_avg, 1),
        "theme_ranking": theme_ranking,
        "recommendations": recommendations,
    }

    if top:
        result["best_article"] = top[0]
    if trend:
        result["trend"] = trend

    return result


def format_insights_for_generate(db_path=None):
    """Retourne un texte lisible pour injection dans /generate."""
    insights = generate_insights(db_path)

    if insights['total_articles_tracked'] == 0:
        return ""

    lines = [f"📊 Insights basés sur {insights['total_articles_tracked']} articles trackés:"]

    if insights.get('theme_ranking'):
        lines.append("\nPerformance par thème:")
        for t in insights['theme_ranking'][:5]:
            lines.append(f"  - {t['theme']}: engagement moyen {t['avg_engagement']} ({t['multiplier_vs_avg']}x vs moyenne)")

    if insights.get('recommendations'):
        lines.append("\nRecommandations:")
        for r in insights['recommendations']:
            lines.append(f"  → {r}")

    if insights.get('trend'):
        trend = insights['trend']
        arrow = "↑" if trend['direction'] == "up" else "↓" if trend['direction'] == "down" else "→"
        lines.append(f"\nTendance: {arrow} récent={trend['recent_avg']} vs précédent={trend['previous_avg']}")

    return "\n".join(lines)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Insights engagement LinkedIn')
    parser.add_argument('--themes', action='store_true', help='Performance par thème uniquement')
    parser.add_argument('--for-generate', action='store_true', help='Format texte pour /generate')
    args = parser.parse_args()

    if args.for_generate:
        text = format_insights_for_generate()
        if text:
            print(text)
    elif args.themes:
        result = theme_performance()
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        result = generate_insights()
        print(json.dumps(result, indent=2, ensure_ascii=False))
