"""Gemini API image generation backend."""

import os
import sys

MODEL = "gemini-3.1-flash-image-preview"
ASPECT_RATIO = "16:9"


def generate(prompt: str, output_path: str) -> dict:
    """Generate an image using the Gemini API.

    Args:
        prompt: Image generation prompt text.
        output_path: Path where the generated PNG will be saved.

    Returns:
        dict with generation metadata (model, aspect_ratio).

    Raises:
        SystemExit: If API key is missing or generation fails.
    """
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GOOGLE_API_KEY environment variable is not set. "
            "Get your key at https://aistudio.google.com/apikey"
        )

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

    candidates = getattr(response, "candidates", None)
    if not candidates:
        raise RuntimeError(
            "No candidates in response (possibly blocked by safety filters)"
        )

    content = getattr(candidates[0], "content", None)
    parts = getattr(content, "parts", None) if content is not None else None
    if not parts:
        raise RuntimeError(
            "No content parts in response (possibly blocked by safety filters)"
        )

    image_saved = False
    for part in parts:
        if part.inline_data is not None:
            image = part.as_image()
            image.save(str(output_path))
            image_saved = True
            break

    if not image_saved:
        raise RuntimeError(
            "No image in response (possibly blocked by safety filters)"
        )

    return {"model": MODEL, "aspect_ratio": ASPECT_RATIO}
