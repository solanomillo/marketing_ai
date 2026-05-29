"""
Punto de entrada principal.
"""

from config.llm import get_llm


def main():

    llm = get_llm()

    response = llm.invoke(
        "Dame una idea viral para TikTok sobre barbería"
    )

    print("\nRESPUESTA:\n")
    print(response.content)


if __name__ == "__main__":
    main()