"""
Herramientas SEO.
"""
from langchain_core.tools import tool


@tool
def generate_seo_keywords(topic: str) -> str:
    """
    Genera keywords SEO básicas.
    """

    keywords = [
        f"{topic} tips",
        f"mejor {topic}",
        f"{topic} marketing",
        f"{topic} viral",
        f"{topic} para negocios",
    ]

    return "\n".join(keywords)