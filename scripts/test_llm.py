
from harness.llm import get_llm


def main():
    llm = get_llm()

    response = llm.invoke(
        """
        You are an AI coding assistant.

        Explain the following:
        1. What is the responsibility of a Python function?
        """
    )

    print("\nLLM response:\n")
    print(response.content)

    print("\nToken usage:")
    print(response.usage_metadata)


if __name__ == "__main__":
    main()
