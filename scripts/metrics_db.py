#!/usr/bin/env python3
"""
veilleur — Data access layer for the LinkedIn metrics database.
"""

import sqlite3
from datetime import datetime
from pathlib import Path

DEFAULT_DB_PATH = Path(__file__).parent.parent / 'data' / 'metrics.db'

def get_db(db_path=None):
    """Open the SQLite connection and create the table if needed."""
    db = str(db_path or DEFAULT_DB_PATH)
    Path(db).parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    conn.execute("""
        CREATE TABLE IF NOT EXISTS metrics (
            date TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            themes TEXT NOT NULL,
            likes INTEGER DEFAULT 0,
            comments INTEGER DEFAULT 0,
            reposts INTEGER DEFAULT 0,
            impressions INTEGER DEFAULT 0,
            recorded_at TEXT NOT NULL,
            updated_at TEXT
        )
    """)
    conn.commit()
    return conn


def upsert_metrics(date, title, themes, likes=0, comments=0, reposts=0, impressions=0, db_path=None):
    """Insert or update the metrics for an article."""
    conn = get_db(db_path)
    now = datetime.now().isoformat()

    existing = conn.execute("SELECT date FROM metrics WHERE date = ?", (date,)).fetchone()

    if existing:
        conn.execute("""
            UPDATE metrics SET title=?, themes=?, likes=?, comments=?, reposts=?,
            impressions=?, updated_at=? WHERE date=?
        """, (title, themes, likes, comments, reposts, impressions, now, date))
    else:
        conn.execute("""
            INSERT INTO metrics (date, title, themes, likes, comments, reposts, impressions, recorded_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (date, title, themes, likes, comments, reposts, impressions, now))

    conn.commit()
    conn.close()

    return {
        "status": "updated" if existing else "created",
        "date": date,
        "likes": likes,
        "comments": comments,
        "reposts": reposts,
        "impressions": impressions,
    }


def get_metrics(date, db_path=None):
    """Return the metrics for an article by date, or None."""
    conn = get_db(db_path)
    row = conn.execute("SELECT * FROM metrics WHERE date = ?", (date,)).fetchone()
    conn.close()
    if row:
        return dict(row)
    return None


def get_all_metrics(limit=30, db_path=None):
    """Return recent metrics, ordered by descending date."""
    conn = get_db(db_path)
    rows = conn.execute(
        "SELECT * FROM metrics ORDER BY date DESC LIMIT ?", (limit,)
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_latest_without_metrics(db_path=None, collection=None):
    """Return the date of the most recent indexed article with no recorded metrics.

    Looks in ChromaDB for articles that have no row in the metrics table,
    or whose metrics are all zero.

    A ChromaDB collection object can be passed in (for tests);
    otherwise the collection is retrieved via index_article.get_collection().
    """
    if collection is None:
        import sys
        sys.path.insert(0, str(Path(__file__).parent))
        from index_article import get_collection
        collection = get_collection()

    if collection.count() == 0:
        return None

    # Get all indexed article dates
    all_articles = collection.get(include=['metadatas'])
    dates = sorted([m['date'] for m in all_articles['metadatas']], reverse=True)

    conn = get_db(db_path)
    for date in dates:
        row = conn.execute("SELECT * FROM metrics WHERE date = ?", (date,)).fetchone()
        if not row or (
            row['likes'] == 0
            and row['comments'] == 0
            and row['reposts'] == 0
            and row['impressions'] == 0
        ):
            conn.close()
            return date

    conn.close()
    return None
