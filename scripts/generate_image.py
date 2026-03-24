"""Generate an article image from the daily image prompt.

Supports local generation (SDXL-Turbo) and Gemini API as a fallback.
"""

import json
import sys
from pathlib import Path

DATA_OUTPUT = Path(__file__).parent.parent / "data" / "output"
DEFAULT_BACKEND = "local"


def main():
    # Parse --backend flag
    backend_name = DEFAULT_BACKEND
    args = sys.argv[1:]
    filtered_args = []
    i = 0
    while i < len(args):
        if args[i] == "--backend" and i + 1 < len(args):
            backend_name = args[i + 1]
            i += 2
        elif args[i] == "--download-model":
            from image_backends.local_backend import download_model

            download_model()
            return
        else:
            filtered_args.append(args[i])
            i += 1

    force = "--force" in filtered_args
    date = next((a for a in filtered_args if not a.startswith("--")), None)

    if not date:
        print(
            json.dumps(
                {
                    "error": "Usage: generate_image.py DATE [--force] [--backend local|gemini] [--download-model]"
                }
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

    prompt = prompt_path.read_text().strip()

    try:
        from image_backends import get_backend

        backend = get_backend(backend_name)
        metadata = backend.generate(prompt, str(output_path))

        print(
            json.dumps(
                {
                    "status": "generated",
                    "path": str(output_path),
                    "date": date,
                    "backend": backend_name,
                    **metadata,
                }
            )
        )

    except Exception as e:
        print(
            json.dumps(
                {
                    "error": str(e),
                    "date": date,
                    "backend": backend_name,
                }
            )
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
