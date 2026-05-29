"""
Formateador de contenido según plataforma.
"""


def format_for_platform(
    content: str,
    platform: str
) -> str:
    """
    Adapta contenido según red social.
    """

    platform = platform.lower()

    if platform == "tiktok":
        return f"""
🎵 TikTok Version:

{content}

👉 Hook corto
👉 CTA rápido
👉 Estilo viral
"""

    if platform == "instagram":
        return f"""
📸 Instagram Version:

{content}

✨ Visual
✨ Estético
✨ Emocional
"""

    if platform == "facebook":
        return f"""
📘 Facebook Version:

{content}

📝 Más descriptivo
📝 Más contexto
"""

    if platform == "whatsapp":
        return f"""
💬 WhatsApp Version:

{content}

✅ Directo
✅ Corto
✅ Conversacional
"""

    return content