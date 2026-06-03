"""
Utilidades de streaming para LangGraph.
"""


AGENT_LABELS = {
    "supervisor": "🧠 Supervisor",
    "content_agent": "✍️ Content Agent",
    "social_agent": "📱 Social Agent",
    "seo_agent": "🔍 SEO Agent",
    "ads_agent": "📢 Ads Agent",
}


def get_agent_label(
    node_name: str,
) -> str:
    """
    Retorna nombre amigable.
    """

    return AGENT_LABELS.get(
        node_name,
        f"⚙️ {node_name}"
    )