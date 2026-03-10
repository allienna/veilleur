#!/usr/bin/env python3
"""
veilleur — Save the list of processed raw files after article generation.

Usage:
    python3 scripts/save_processed_files.py 2026-03-09 file1.json file2.json ...

Output: JSON on stdout confirming the manifest was saved.
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path


def save_manifest(target_date: str, files: list[str]) -> None:
    """Write a manifest of processed raw files for carry-forward detection."""
    output_dir = Path(__file__).parent.parent / 'data' / 'output'
    output_dir.mkdir(parents=True, exist_ok=True)
    manifest = {
        "date": target_date,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "files": [Path(f).name for f in files],
    }
    path = output_dir / f"{target_date}-processed-files.json"
    with open(path, 'w') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    print(json.dumps({"saved": str(path), "count": len(files)}))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 save_processed_files.py DATE [FILE ...]", file=sys.stderr)
        sys.exit(1)
    target_date = sys.argv[1]
    files = sys.argv[2:]
    save_manifest(target_date, files)
