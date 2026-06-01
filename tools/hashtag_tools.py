"""
Herramientas para generación de hashtags.
"""
from langchain_core.tools import tool


@tool
def generate_hashtags(topic: str) -> str:
    """
    Genera hashtags optimizados para marketing.
    """

    hashtags = [
        f"#{topic.replace(' ', '')}",
        f"#viral{topic.replace(' ', '')}",
        f"#trend{topic.replace(' ', '')}",
        "#fyp",
        "#viral",
        "#parati",
        "#marketing",
    ]

    return " ".join(hashtags)