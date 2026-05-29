"""
Herramientas relacionadas con TikTok.
"""


def get_tiktok_trends(topic: str) -> str:
    """
    Simula tendencias virales de TikTok.
    """

    trends = [
        f"Hook viral sobre {topic}",
        f"Storytime relacionado con {topic}",
        f"Antes y después de {topic}",
        f"Errores comunes en {topic}",
        f"Top 3 secretos sobre {topic}",
    ]

    return "\n".join(trends)