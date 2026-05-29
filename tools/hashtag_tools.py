"""
Herramientas para generación de hashtags.
"""


def generate_hashtags(topic: str) -> str:
    """
    Genera hashtags optimizados.
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