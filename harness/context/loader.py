
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def load_markdown_context(filename: str) -> str:
    """
    Load a Markdown context file from the project root.
    """

    file_path = PROJECT_ROOT / filename

    if not file_path.exists():
        raise FileNotFoundError(
            f"Context file not found: {file_path}"
        )

    return file_path.read_text(encoding="utf-8")


def load_project_context() -> dict[str, str]:
    """
    Load the core project instructions and architecture.
    """

    return {
        "instructions": load_markdown_context("AGENTS.md"),
        "architecture": load_markdown_context("ARCHITECTURE.md"),
    }
