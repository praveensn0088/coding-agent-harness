
import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


def get_llm() -> ChatOpenAI:
    """Create and return the configured OpenAI chat model."""

    api_key = os.getenv("OPENAI_API_KEY")
    model_name = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY is missing. Check your .env file."
        )

    return ChatOpenAI(
        model=model_name,
        api_key=api_key,
        temperature=0,
        timeout=60,
        max_retries=2,
    )
