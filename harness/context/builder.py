
from langchain_core.messages import SystemMessage, HumanMessage

from harness.context.loader import load_project_context


def build_messages(task: str) -> list:
    """
    Build LLM messages using project context and user task.
    """

    context = load_project_context()

    system_prompt = f"""
    You are an AI software engineering assistant.

    Follow these repository instructions:

    {context["instructions"]}

    Understand the project architecture:

    {context["architecture"]}

    Use this information when responding to the user's task.
"""

    return [
        SystemMessage(content=system_prompt),
        HumanMessage(content=task),
    ]
