#!/usr/bin/env python3
"""Generate Instagram carousel (PNG) and teaser reel (MP4) from daily article.

Usage:
    python3 scripts/generate_instagram.py DATE
    python3 scripts/generate_instagram.py DATE --carousel-only
    python3 scripts/generate_instagram.py DATE --reel-only
    python3 scripts/generate_instagram.py --install-browser   # one-time setup

Output:
    data/output/{DATE}-instagram/
        carousel/slide-01.png ... slide-10.png  (1080x1350, 4:5)
        teaser/slide-01.png ... slide-04.png    (1080x1920, 9:16) — teaser reel
        teaser.mp4                              (~12s teaser pointing to carousel)
"""

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Slide dimensions
REEL_W, REEL_H = 1080, 1920       # 9:16 for Reels
FEED_W, FEED_H = 1080, 1350       # 4:5 for carousel
CROP_TOP = (REEL_H - FEED_H) // 2  # 285px from top

# Colors
NAVY = "#162d60"
AMBER = "#f59f0a"
AMBER_DARK = "#d97706"
WHITE = "#ffffff"
WHITE_DIM = "rgba(255,255,255,0.75)"
WHITE_FAINT = "rgba(255,255,255,0.35)"
AMBER_BG = "rgba(245,159,10,0.15)"
AMBER_BORDER = "rgba(245,159,10,0.35)"
WHITE_BG = "rgba(255,255,255,0.06)"

SLIDE_DURATION = 2.5  # seconds per slide in reel


# ── Data structures ────────────────────────────────────────────────────────────

@dataclass
class Slide:
    type: str           # hook | insight | brief | summary | cta
    title: str = ""
    body: str = ""
    tag: str = ""
    bullets: list[str] = field(default_factory=list)
    index: int = 0
    total: int = 10


# ── Content extraction ─────────────────────────────────────────────────────────

def _clean_md(text: str) -> str:
    """Strip markdown syntax for plain display."""
    text = re.sub(r'\*+([^*]+)\*+', r'\1', text)          # bold/italic
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)  # links
    text = re.sub(r'^[>#-]+ ', '', text, flags=re.MULTILINE)
    text = re.sub(r'\n+', ' ', text).strip()
    return text


def parse_front_matter(text: str) -> dict:
    """Parse YAML front matter without external dependencies."""
    m = re.match(r'^---\n(.*?)\n---\n', text, re.DOTALL)
    if not m:
        return {}
    result = {}
    for line in m.group(1).split('\n'):
        if ':' in line:
            key, _, val = line.partition(':')
            val = val.strip()
            if val.startswith('[') and val.endswith(']'):
                result[key.strip()] = [v.strip().strip('"\'') for v in val[1:-1].split(',')]
            else:
                result[key.strip()] = val.strip('"\'')
    return result


def parse_post(date_str: str) -> str:
    """First paragraph of the LinkedIn post = hook text."""
    path = PROJECT_ROOT / "data" / "output" / f"{date_str}-post.md"
    if not path.exists():
        return ""
    text = path.read_text().strip()
    return text.split("\n\n")[0].strip()


def parse_article(date_str: str) -> dict | None:
    """Extract structured content from article markdown."""
    path = PROJECT_ROOT / "data" / "output" / f"{date_str}-article.md"
    if not path.exists():
        return None

    text = path.read_text()
    fm = parse_front_matter(text)

    # Remove front matter
    body = re.sub(r'^---\n.*?\n---\n', '', text, flags=re.DOTALL).strip()
    # Remove h1 title line
    body = re.sub(r'^# .+\n', '', body).strip()

    # Extract intro (text before first ### section)
    intro_match = re.match(r'^(.*?)(?=\n###|\n##)', body, re.DOTALL)
    intro = _clean_md(intro_match.group(1).strip()) if intro_match else ""
    if len(intro) > 300:
        intro = intro[:297] + "…"

    # Extract ### sections
    raw_sections = re.split(r'\n### ', body)
    sections = []
    brief = ""

    for sec in raw_sections[1:]:
        lines = sec.strip().split('\n')
        title = lines[0].strip()
        body_text = '\n'.join(lines[1:]).strip()

        if title.lower() in ('sources', 'références', 'pour aller plus loin'):
            continue

        clean = _clean_md(body_text)
        if len(clean) > 320:
            clean = clean[:317] + "…"

        if title.lower() == 'en bref':
            brief = clean
        else:
            sections.append({'title': title, 'body': clean})

    # Extract sources from ## Sources
    sources = []
    src_match = re.search(r'\n## Sources\n(.*?)(?=\n##|$)', text, re.DOTALL)
    if src_match:
        for line in src_match.group(1).split('\n'):
            m = re.match(r'\d+\.\s+\[([^\]]+)\]', line)
            if m:
                sources.append(m.group(1)[:60])

    return {
        'title': str(fm.get('title', '')).strip('"'),
        'date': str(fm.get('date', date_str)),
        'themes': fm.get('themes', []),
        'intro': intro,
        'sections': sections[:5],    # max 5 insight slides
        'brief': brief,
        'sources': sources[:5],
    }


def extract_stats(article: dict) -> list[str]:
    """Pull provocative numbers/percentages from article sections."""
    stats = []
    number_re = re.compile(r'[^.!?]*(?:\d[\d\s]*[\%x]|\d{2,}[\s][a-zA-ZÀ-ÿ]+)[^.!?]*[.!?]')
    for sec in article.get('sections', []):
        for m in number_re.finditer(sec.get('body', '')):
            s = m.group(0).strip()
            if 30 < len(s) < 180:
                stats.append(s)
    if article.get('intro'):
        for m in number_re.finditer(article['intro']):
            s = m.group(0).strip()
            if 30 < len(s) < 180:
                stats.append(s)
    return stats[:2]


def build_teaser_slides(article: dict, hook: str) -> list[Slide]:
    """4-slide teaser: hook → stat → cliffhanger → CTA."""
    slides: list[Slide] = []
    stats = extract_stats(article)

    # Slide 1 — hook (same stop-the-scroll opening)
    slides.append(Slide(type='hook', title=article['title'], body=hook or article['title']))

    # Slide 2 — most provocative stat
    if stats:
        slides.append(Slide(
            type='teaser_stat',
            body=stats[0],
        ))
    elif article.get('intro'):
        slides.append(Slide(type='teaser_stat', body=article['intro'][:200]))

    # Slide 3 — second stat or a section title as a question
    if len(stats) >= 2:
        slides.append(Slide(type='teaser_stat', body=stats[1]))
    elif article.get('sections'):
        sec = article['sections'][0]
        slides.append(Slide(type='teaser_stat', body=f"{sec['title']} — {sec['body'][:160]}…"))

    # Slide 4 — CTA pointing to carousel
    slides.append(Slide(type='teaser_cta'))

    total = len(slides)
    for i, s in enumerate(slides):
        s.index = i + 1
        s.total = total
    return slides


def build_slides(article: dict, hook: str) -> list[Slide]:
    """Assemble ordered slide list."""
    slides: list[Slide] = []
    themes = article.get('themes', [])
    tag = themes[0] if themes else ""

    # Slide 1 — Hook (stop the scroll)
    slides.append(Slide(type='hook', title=article['title'], body=hook or article['title']))

    # Slide 2 — Intro / context
    if article.get('intro'):
        slides.append(Slide(type='insight', title="Le contexte", body=article['intro'], tag=tag))

    # Slides 3-7 — Key sections
    for sec in article['sections']:
        slides.append(Slide(type='insight', title=sec['title'], body=sec['body'], tag=tag))

    # Slide N-2 — En bref (if exists)
    if article.get('brief'):
        slides.append(Slide(type='brief', title="En bref", body=article['brief']))

    # Slide N-1 — Ce qu'il faut retenir
    bullets = [s['title'] for s in article['sections'][:3]]
    slides.append(Slide(type='summary', title="Ce qu'il faut retenir", bullets=bullets))

    # Slide N — CTA
    slides.append(Slide(type='cta'))

    total = len(slides)
    for i, s in enumerate(slides):
        s.index = i + 1
        s.total = total

    return slides


# ── HTML generation ────────────────────────────────────────────────────────────

def _progress_bar(slide: Slide) -> str:
    dots = ""
    for i in range(slide.total):
        if i == slide.index - 1:
            style = f"background:{AMBER}; width:28px;"
        else:
            style = f"background:{WHITE_FAINT}; width:12px;"
        dots += f'<div style="height:6px; border-radius:3px; {style} margin:0 3px;"></div>'
    return f'<div style="display:flex; align-items:center; padding-top:20px;">{dots}</div>'


def _header(slide: Slide) -> str:
    return f"""
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;">
        <span style="font-size:20px; font-weight:700; color:{WHITE_FAINT}; letter-spacing:3px; text-transform:uppercase;">Le Veilleur</span>
        <span style="font-size:20px; color:{WHITE_FAINT}; font-weight:600;">{slide.index}/{slide.total}</span>
    </div>"""


def _slide_content(slide: Slide) -> str:
    if slide.type == 'hook':
        lines = slide.body.strip().split('\n')
        hook_html = '<br>'.join(lines[:3])
        return f"""
        <div style="flex:1; display:flex; flex-direction:column; justify-content:center; gap:40px;">
            <div style="display:flex; align-items:center; gap:16px;">
                <div style="background:{AMBER}; height:6px; width:64px; border-radius:3px;"></div>
                <span style="font-size:22px; color:{AMBER}; font-weight:700; letter-spacing:1px; text-transform:uppercase;">Veille tech</span>
            </div>
            <div style="font-size:62px; font-weight:800; line-height:1.1; color:{WHITE};">
                {hook_html}
            </div>
            <div style="font-size:26px; color:{WHITE_DIM}; font-weight:400; line-height:1.5; border-left:4px solid {AMBER}; padding-left:24px;">
                {slide.title[:120]}
            </div>
        </div>"""

    elif slide.type == 'insight':
        tag_html = ""
        if slide.tag:
            tag_html = f'<div style="display:inline-block; background:{AMBER_BG}; color:{AMBER}; padding:10px 24px; border-radius:24px; font-size:20px; font-weight:600; border:1px solid {AMBER_BORDER}; margin-bottom:24px;">{slide.tag}</div>'
        return f"""
        <div style="flex:1; display:flex; flex-direction:column; justify-content:center; gap:28px;">
            {tag_html}
            <div style="font-size:46px; font-weight:700; line-height:1.2; color:{WHITE};">{slide.title}</div>
            <div style="width:56px; height:4px; background:{AMBER}; border-radius:2px;"></div>
            <div style="font-size:29px; color:{WHITE_DIM}; line-height:1.65; font-weight:400;">{slide.body}</div>
        </div>"""

    elif slide.type == 'brief':
        return f"""
        <div style="flex:1; display:flex; flex-direction:column; justify-content:center; gap:32px;">
            <div style="font-size:20px; font-weight:700; color:{AMBER}; letter-spacing:2px; text-transform:uppercase;">En bref</div>
            <div style="font-size:46px; font-weight:700; color:{WHITE};">{slide.title}</div>
            <div style="background:{WHITE_BG}; border-radius:20px; padding:40px; border-left:6px solid {AMBER};">
                <div style="font-size:28px; color:{WHITE_DIM}; line-height:1.6;">{slide.body}</div>
            </div>
        </div>"""

    elif slide.type == 'summary':
        bullets_html = ""
        for b in slide.bullets:
            bullets_html += f"""
            <div style="display:flex; align-items:flex-start; gap:20px; margin-bottom:24px;">
                <div style="min-width:10px; height:10px; background:{AMBER}; border-radius:50%; margin-top:16px; flex-shrink:0;"></div>
                <div style="font-size:30px; color:{WHITE_DIM}; line-height:1.45;">{b}</div>
            </div>"""
        return f"""
        <div style="flex:1; display:flex; flex-direction:column; justify-content:center; gap:36px;">
            <div style="font-size:50px; font-weight:800; color:{WHITE};">
                {slide.title} <span style="color:{AMBER}">→</span>
            </div>
            <div style="background:{WHITE_BG}; border-radius:20px; padding:44px; border-left:6px solid {AMBER};">
                {bullets_html}
            </div>
        </div>"""

    elif slide.type == 'cta':
        return f"""
        <div style="flex:1; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; gap:36px;">
            <div style="font-size:88px; line-height:1;">🦉</div>
            <div>
                <div style="font-size:60px; font-weight:800; color:{WHITE}; line-height:1.1;">Le</div>
                <div style="font-size:60px; font-weight:800; color:{AMBER}; line-height:1.1;">Veilleur</div>
            </div>
            <div style="background:{AMBER}; height:4px; width:72px; border-radius:2px;"></div>
            <div style="font-size:26px; color:{WHITE_DIM}; line-height:1.55; max-width:800px;">
                Chaque jour, je décrypte les tendances tech pour les Engineering Directors.
            </div>
            <div style="background:{WHITE_BG}; border-radius:20px; padding:28px 52px; border:1px solid rgba(255,255,255,0.15); margin-top:8px;">
                <div style="font-size:28px; color:{AMBER}; font-weight:700;">👉 Suivez Aurélien Allienne</div>
                <div style="font-size:22px; color:{WHITE_FAINT}; margin-top:10px;">Veille quotidienne sur LinkedIn</div>
            </div>
        </div>"""

    elif slide.type == 'teaser_stat':
        return f"""
        <div style="flex:1; display:flex; flex-direction:column; justify-content:center; gap:36px;">
            <div style="background:{AMBER}; height:6px; width:80px; border-radius:3px;"></div>
            <div style="font-size:48px; font-weight:700; color:{WHITE}; line-height:1.3;">
                {slide.body}
            </div>
        </div>"""

    elif slide.type == 'teaser_cta':
        return f"""
        <div style="flex:1; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; gap:44px;">
            <div style="font-size:88px; line-height:1;">🦉</div>
            <div style="font-size:52px; font-weight:800; color:{WHITE}; line-height:1.2;">
                La suite ?<br><span style="color:{AMBER}">Dans le carousel</span><br>ci-dessus 👆
            </div>
            <div style="background:{AMBER}; height:4px; width:72px; border-radius:2px;"></div>
            <div style="font-size:26px; color:{WHITE_DIM}; line-height:1.5;">
                Swipe sur le post pour lire<br>l'analyse complète.
            </div>
        </div>"""

    return "<div></div>"


def render_html(slide: Slide, w: int, h: int) -> str:
    padding = max(64, h // 18)
    return f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ width:{w}px; height:{h}px; background:{NAVY}; font-family:'Poppins',-apple-system,sans-serif; color:{WHITE}; overflow:hidden; }}
  .slide {{ width:{w}px; height:{h}px; padding:{padding}px; display:flex; flex-direction:column; }}
</style></head>
<body><div class="slide">
  {_header(slide)}
  {_slide_content(slide)}
  {_progress_bar(slide)}
</div></body></html>"""


# ── Screenshot & export ────────────────────────────────────────────────────────

def screenshot_slides(slides: list[Slide], reel_dir: Path, w: int, h: int) -> list[Path]:
    """Screenshot all slides at reel size, return paths."""
    from playwright.sync_api import sync_playwright

    reel_dir.mkdir(parents=True, exist_ok=True)
    paths = []

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={'width': w, 'height': h})
        for slide in slides:
            html = render_html(slide, w, h)
            out = reel_dir / f"slide-{slide.index:02d}.png"
            page.set_content(html, wait_until='networkidle')
            page.screenshot(path=str(out), type='png')
            paths.append(out)
            print(f"  [{slide.index}/{slide.total}] {slide.type}: {slide.title[:50]}")
        browser.close()

    return paths


def crop_to_feed(reel_paths: list[Path], feed_dir: Path) -> list[Path]:
    """Center-crop reel slides (1080x1920) to feed format (1080x1350)."""
    from PIL import Image

    feed_dir.mkdir(parents=True, exist_ok=True)
    paths = []
    for reel_path in reel_paths:
        img = Image.open(reel_path)
        cropped = img.crop((0, CROP_TOP, FEED_W, CROP_TOP + FEED_H))
        out = feed_dir / reel_path.name
        cropped.save(out, 'PNG')
        paths.append(out)
    return paths


def build_reel(reel_paths: list[Path], output: Path, duration: float = SLIDE_DURATION) -> bool:
    """Assemble slide PNGs into MP4 using ffmpeg (simple cut)."""
    concat_file = output.parent / "_concat.txt"
    try:
        with open(concat_file, 'w') as f:
            for path in reel_paths:
                f.write(f"file '{path.resolve()}'\n")
                f.write(f"duration {duration}\n")
            f.write(f"file '{reel_paths[-1].resolve()}'\n")

        cmd = [
            "ffmpeg", "-y",
            "-f", "concat", "-safe", "0",
            "-i", str(concat_file),
            "-vf", f"scale={REEL_W}:{REEL_H}:force_original_aspect_ratio=decrease,"
                   f"pad={REEL_W}:{REEL_H}:(ow-iw)/2:(oh-ih)/2:color={NAVY.replace('#', '0x')}",
            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "30",
            str(output)
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.returncode == 0
    finally:
        concat_file.unlink(missing_ok=True)


def build_teaser_reel(slide_paths: list[Path], output: Path, duration: float = 3.0) -> bool:
    """Assemble teaser slides with Ken Burns zoom effect via ffmpeg."""
    fps = 30
    frames = int(duration * fps)
    # zoompan: slow zoom in (1.0 → 1.08) over the slide duration
    zoom_filter = (
        f"zoompan=z='min(zoom+0.0008,1.08)':d={frames}:s={REEL_W}x{REEL_H}:fps={fps},"
        f"scale={REEL_W}:{REEL_H}"
    )

    # Build one clip per slide, then concatenate
    clips = []
    tmp_dir = output.parent / "_tmp_clips"
    tmp_dir.mkdir(parents=True, exist_ok=True)

    for i, path in enumerate(slide_paths):
        clip = tmp_dir / f"clip_{i:02d}.mp4"
        cmd = [
            "ffmpeg", "-y",
            "-loop", "1", "-t", str(duration),
            "-i", str(path),
            "-vf", zoom_filter,
            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", str(fps),
            str(clip)
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"  WARNING: ffmpeg clip {i} failed: {result.stderr[-500:]}", file=sys.stderr)
            return False
        clips.append(clip)

    if not clips:
        print("  WARNING: no clips generated", file=sys.stderr)
        return False

    # Concatenate clips
    tmp_dir.mkdir(parents=True, exist_ok=True)  # ensure dir still exists
    concat_file = tmp_dir / "concat.txt"
    with open(concat_file, 'w') as f:
        for clip in clips:
            f.write(f"file '{clip.resolve()}'\n")

    cmd = [
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0",
        "-i", str(concat_file),
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        str(output)
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)

    # Cleanup tmp clips
    import shutil
    shutil.rmtree(tmp_dir, ignore_errors=True)

    return result.returncode == 0


# ── Main ───────────────────────────────────────────────────────────────────────

def generate_instagram(
    date_str: str,
    carousel: bool = True,
    reel: bool = True,
    teaser: bool = True,
) -> bool:
    print(f"Generating Instagram content for {date_str}...")

    # Parse content
    hook = parse_post(date_str)
    article = parse_article(date_str)
    if not article:
        print(f"ERROR: Article not found for {date_str}", file=sys.stderr)
        return False

    slides = build_slides(article, hook)
    print(f"  {len(slides)} carousel slides prepared")

    # Output dirs
    out_dir = PROJECT_ROOT / "data" / "output" / f"{date_str}-instagram"
    reel_dir = out_dir / "reel"
    feed_dir = out_dir / "carousel"

    # ── Carousel pipeline ───────────────────────────────────────────────────────
    # Screenshot at reel size (1080x1920) then crop
    print(f"\nScreenshotting carousel slides ({REEL_W}x{REEL_H})...")
    reel_paths = screenshot_slides(slides, reel_dir, REEL_W, REEL_H)

    if carousel:
        print(f"\nCropping to carousel format ({FEED_W}x{FEED_H})...")
        feed_paths = crop_to_feed(reel_paths, feed_dir)
        print(f"  {len(feed_paths)} carousel slides → {feed_dir}")

    if reel:
        reel_mp4 = out_dir / "reel.mp4"
        print(f"\nAssembling carousel reel ({len(reel_paths)} slides × {SLIDE_DURATION}s)...")
        if build_reel(reel_paths, reel_mp4):
            print(f"  Reel → {reel_mp4}")
        else:
            print("  WARNING: ffmpeg reel assembly failed", file=sys.stderr)

    # ── Teaser reel pipeline ────────────────────────────────────────────────────
    if teaser:
        teaser_slides = build_teaser_slides(article, hook)
        print(f"\n{len(teaser_slides)} teaser slides prepared")
        teaser_dir = out_dir / "teaser"
        print(f"Screenshotting teaser slides ({REEL_W}x{REEL_H})...")
        teaser_paths = screenshot_slides(teaser_slides, teaser_dir, REEL_W, REEL_H)
        teaser_mp4 = out_dir / "teaser.mp4"
        print(f"\nAssembling teaser reel with Ken Burns ({len(teaser_paths)} slides × 3s)...")
        if build_teaser_reel(teaser_paths, teaser_mp4):
            print(f"  Teaser → {teaser_mp4}")
        else:
            print("  WARNING: teaser reel assembly failed", file=sys.stderr)

    print(f"\nDone → {out_dir}")
    return True


def main():
    parser = argparse.ArgumentParser(description="Generate Instagram carousel + reel")
    parser.add_argument("date", nargs="?", default=date.today().isoformat(), help="Date YYYY-MM-DD")
    parser.add_argument("--carousel-only", action="store_true", help="Skip reel and teaser")
    parser.add_argument("--reel-only", action="store_true", help="Skip carousel export")
    parser.add_argument("--teaser-only", action="store_true", help="Generate only the teaser reel")
    parser.add_argument("--no-teaser", action="store_true", help="Skip teaser reel generation")
    parser.add_argument("--install-browser", action="store_true", help="Install Playwright Chromium (one-time)")
    args = parser.parse_args()

    if args.install_browser:
        subprocess.run(["playwright", "install", "chromium"], check=True)
        print("Chromium installed.")
        return

    if args.teaser_only:
        carousel = reel = False
        teaser = True
    else:
        carousel = not args.reel_only
        reel = not args.carousel_only
        teaser = not args.no_teaser and not args.carousel_only

    success = generate_instagram(args.date, carousel=carousel, reel=reel, teaser=teaser)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
