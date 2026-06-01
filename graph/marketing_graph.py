"""
Graph principal del sistema.
"""

from agents.supervisor import build_supervisor


def build_marketing_graph(
    checkpointer=None
):
    """
    Construye el graph principal.
    """

    supervisor = build_supervisor()

    return supervisor