
from harness.context.builder import build_messages
from harness.llm import get_llm


def main():
    task = "Explain the responsibilities of the harness/llm.py module."

    messages = build_messages(task)

    print("Loaded message count:", len(messages))
    print("\nSending project context to OpenAI...")

    llm = get_llm()
    response = llm.invoke(messages)

    print("\nLLM Response:\n")
    print(response.content)

    print("\nToken Usage:")
    print(response.usage_metadata)


if __name__ == "__main__":
    main()
