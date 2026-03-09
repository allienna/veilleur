"""Local FLUX.1-schnell image generation backend using diffusers + MPS."""

MODEL_ID = "black-forest-labs/FLUX.1-schnell"
WIDTH = 1344
HEIGHT = 768
NUM_STEPS = 4
GUIDANCE_SCALE = 0.0
MAX_SEQUENCE_LENGTH = 256


def generate(prompt: str, output_path: str) -> dict:
    """Generate an image locally using FLUX.1-schnell on Apple Silicon (MPS).

    Uses CPU offloading to fit the ~12GB model within 16GB unified memory.

    Args:
        prompt: Image generation prompt text.
        output_path: Path where the generated PNG will be saved.

    Returns:
        dict with generation metadata (model, resolution, steps).

    Raises:
        ImportError: If torch/diffusers are not installed.
    """
    try:
        import torch
        from diffusers import FluxPipeline
    except ImportError:
        raise ImportError(
            "Local image generation requires extra dependencies. "
            "Install them with: uv sync --extra image"
        )

    pipe = FluxPipeline.from_pretrained(
        MODEL_ID,
        torch_dtype=torch.bfloat16,
    )
    pipe.enable_model_cpu_offload()

    result = pipe(
        prompt=prompt,
        width=WIDTH,
        height=HEIGHT,
        num_inference_steps=NUM_STEPS,
        guidance_scale=GUIDANCE_SCALE,
        max_sequence_length=MAX_SEQUENCE_LENGTH,
    )

    result.images[0].save(str(output_path))

    return {
        "model": MODEL_ID,
        "resolution": f"{WIDTH}x{HEIGHT}",
        "steps": NUM_STEPS,
        "device": "mps+cpu_offload",
    }


def download_model():
    """Pre-download the FLUX.1-schnell model to the local HuggingFace cache."""
    try:
        import torch
        from diffusers import FluxPipeline
    except ImportError:
        raise ImportError(
            "Local image generation requires extra dependencies. "
            "Install them with: uv sync --extra image"
        )

    print(f"Downloading {MODEL_ID}...")
    FluxPipeline.from_pretrained(
        MODEL_ID,
        torch_dtype=torch.bfloat16,
    )
    print(f"Model {MODEL_ID} downloaded successfully.")
