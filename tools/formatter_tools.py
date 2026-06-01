from langchain_core.tools import tool


@tool
def format_for_platform(
    content: str,
    platform: str
) -> str:
    """
    Adapta contenido para TikTok, Instagram,
    Facebook o WhatsApp.
    """

    platform = platform.lower().strip()

    templates = {
        "tiktok": f"""
🎵 TikTok Version

{content}

👉 Hook corto
👉 CTA rápido
👉 Estilo viral
""",
        "instagram": f"""
📸 Instagram Version

{content}

✨ Visual
✨ Estético
✨ Emocional
""",
        "facebook": f"""
📘 Facebook Version

{content}

📝 Más descriptivo
📝 Más contexto
""",
        "whatsapp": f"""
💬 WhatsApp Version

{content}

✅ Directo
✅ Corto
✅ Conversacional
"""
    }

    return templates.get(platform, content)