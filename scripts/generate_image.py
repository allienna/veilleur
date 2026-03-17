#!/usr/bin/env python3
"""Generate article image via Gemini Imagen 4 Fast API.

Usage:
    python3 scripts/generate_image.py DATE
    python3 scripts/generate_image.py --test
"""

import argparse
import os
import sys
from pathlib import Path


def load_api_key() -> str:
    """Load Gemini API key from env or config file."""
    key = os.environ.get("GEMINI_API_KEY")
    if key:
        return key
    config_file = Path.home() / ".config" / "veilleur" / ".env"
    if config_file.exists():
        for line in config_file.read_text().splitlines():
            line = line.strip()
            if line.startswith("GEMINI_API_KEY="):
                return line.split("=", 1)[1].strip().strip("\"'")
    print("ERROR: GEMINI_API_KEY not found in env or ~/.config/veilleur/.env", file=sys.stderr)
    sys.exit(1)


def generate_image(prompt: str, output_path: Path, api_key: str) -> bool:
    """Generate image via Imagen 4 Fast ($0.02/image)."""
    from google import genai

    client = genai.Client(api_key=api_key)
    response = client.models.generate_images(
        model="imagen-4.0-fast-generate-001",
        prompt=prompt,
        config=genai.types.GenerateImagesConfig(
            number_of_images=1,
            aspect_ratio="16:9",
        ),
    )

    if not response.generated_images:
        print("WARNING: Imagen returned no images", file=sys.stderr)
        return False

    image = response.generated_images[0]
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(image.image.image_bytes)
    print(f"Image saved to {output_path}")
    return True


def main():
    parser = argparse.ArgumentParser(description="Generate article image via Gemini Imagen API")
    parser.add_argument("date", nargs="?", help="Date (YYYY-MM-DD)")
    parser.add_argument("--test", action="store_true", help="Generate a test image")
    args = parser.parse_args()

    api_key = load_api_key()

    if args.test:
        prompt = "A cute cartoon owl with amber eyes wearing a navy blue scarf, reading a newspaper, wide 16:9 aspect ratio, Pixar style"
        output = Path("data/output/test-image.png")
        success = generate_image(prompt, output, api_key)
        sys.exit(0 if success else 1)

    if not args.date:
        print("Usage: python3 scripts/generate_image.py DATE", file=sys.stderr)
        sys.exit(1)

    prompt_file = Path(f"data/output/{args.date}-image-prompt.md")
    if not prompt_file.exists():
        print(f"ERROR: Prompt file not found: {prompt_file}", file=sys.stderr)
        sys.exit(1)

    prompt = prompt_file.read_text().strip()
    output = Path(f"site/public/images/{args.date}.png")
    success = generate_image(prompt, output, api_key)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
