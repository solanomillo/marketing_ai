"""
Utilidades de memoria.
"""

from langchain_core.messages import trim_messages

from config.llm import get_llm


def trim_chat_history(messages):
    """
    Reduce historial para ahorrar tokens.
    """

    llm = get_llm()

    return trim_messages(
        messages=messages,
        max_tokens=4000,
        strategy="last",
        token_counter=llm,
        start_on="human",
        include_system=True,
        allow_partial=False,
    )