"""
Estado global del sistema multiagente.
"""

from typing import TypedDict, List, Optional


class MarketingState(TypedDict):
    """
    State compartido entre nodos y agentes.
    """

    user_input: str

    messages: List[str]

    active_agent: Optional[str]

    content_output: Optional[str]

    seo_output: Optional[str]

    ads_output: Optional[str]

    final_response: Optional[str]