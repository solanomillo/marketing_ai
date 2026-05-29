"""
Prueba de herramientas.
"""

from tools.tavily_tools import tavily_tool


def main():

    response = tavily_tool.invoke(
        "Tendencias de marketing para TikTok 2026"
    )

    print("\nRESULTADOS:\n")
    print(response)


if __name__ == "__main__":
    main()