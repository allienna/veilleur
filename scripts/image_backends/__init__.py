"""Image generation backend registry."""


def get_backend(name: str):
    """Return the appropriate image generation backend.

    Args:
        name: Backend name, either "local" or "gemini".

    Returns:
        A backend module with a `generate(prompt, output_path)` function.
    """
    if name == "local":
        from . import local_backend

        return local_backend
    elif name == "gemini":
        from . import gemini_backend

        return gemini_backend
    else:
        raise ValueError(f"Unknown backend: {name!r}. Choose 'local' or 'gemini'.")
