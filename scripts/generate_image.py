"""Generate an article image from the daily image prompt using Gemini image generation."""

import json
import os
import sys
from pathlib import Path

DATA_OUTPUT = Path("data/output")
MODEL = "gemini-3.1-flash-image-preview"
ASPECT_RATIO = "16:9"


def list_available_models(api_key):
    """List available Gemini image models via the API."""
    try:
        from google import genai

        client = genai.Client(api_key=api_key)
        models = client.models.list()
        image_models = [m for m in models if "imagen" in m.name or "image" in m.name]
        print(
            json.dumps(
                {
                    "models": [m.name for m in image_models],
                    "all_models": [m.name for m in models],
                },
                indent=2,
            )
        )
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)


def main():

    if "--list-models" in sys.argv:
        api_key = os.environ.get("GOOGLE_API_KEY")
        if not api_key:
            print(
                json.dumps(
                    {
                        "error": "GOOGLE_API_KEY environment variable is not set. Get your key at https://aistudio.google.com/apikey"
                    }
                )
            )
            sys.exit(1)
        list_available_models(api_key)
        return

    date = sys.argv[1] if len(sys.argv) > 1 else None
    force = "--force" in sys.argv

    if not date:
        print(
            json.dumps(
                {"error": "Usage: generate_image.py DATE [--force] [--list-models]"}
            )
        )
        sys.exit(1)

    prompt_path = DATA_OUTPUT / f"{date}-image-prompt.md"
    output_path = DATA_OUTPUT / f"{date}-image.png"

    if output_path.exists() and not force:
        print(
            json.dumps(
                {
                    "status": "skipped",
                    "message": f"Image already exists: {output_path}",
                    "path": str(output_path),
                    "date": date,
                }
            )
        )
        return

    if not prompt_path.exists():
        print(
            json.dumps(
                {
                    "error": f"Prompt file not found: {prompt_path}",
                    "date": date,
                }
            )
        )
        sys.exit(1)

    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print(
            json.dumps(
                {
                    "error": "GOOGLE_API_KEY environment variable is not set. "
                    "Get your key at https://aistudio.google.com/apikey",
                    "date": date,
                }
            )
        )
        sys.exit(1)

    prompt = prompt_path.read_text().strip()

    try:
        from google import genai
        from google.genai import types

        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model=MODEL,
            contents=f"Generate an image based on this description: {prompt}",
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE"],
                image_config=types.ImageConfig(
                    aspect_ratio=ASPECT_RATIO,
                ),
            ),
        )

        image_saved = False
        for part in response.candidates[0].content.parts:
            if part.inline_data is not None:
                image = part.as_image()
                image.save(str(output_path))
                image_saved = True
                break

        if not image_saved:
            print(
                json.dumps(
                    {
                        "error": "No image in response (possibly blocked by safety filters)",
                        "date": date,
                        "model": MODEL,
                    }
                )
            )
            sys.exit(1)

        print(
            json.dumps(
                {
                    "status": "generated",
                    "path": str(output_path),
                    "date": date,
                    "model": MODEL,
                    "aspect_ratio": ASPECT_RATIO,
                }
            )
        )

    except Exception as e:
        print(
            json.dumps(
                {
                    "error": str(e),
                    "date": date,
                    "model": MODEL,
                }
            )
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
