from langchain_core.messages import AIMessage, HumanMessage


def extract_content(message):
    """
    Extrae texto independientemente
    del formato devuelto por Gemini.
    """

    content = message.content

    if isinstance(content, str):
        return content

    if isinstance(content, list):

        texts = []

        for item in content:

            if isinstance(item, dict):

                if item.get("type") == "text":
                    texts.append(
                        item.get("text", "")
                    )

        return "\n".join(texts)

    return str(content)

def format_message(message):
    """
    Convierte mensajes LangChain
    a formato Streamlit.
    """

    if isinstance(message, HumanMessage):
        return {
            "role": "user",
            "content": extract_content(message),
        }

    if isinstance(message, AIMessage):
        return {
            "role": "assistant",
            "content": extract_content(message),
        }

def load_chat_history(
    graph,
    thread_id: str,
):
    """
    Recupera historial desde SQLite.
    """

    config = {
        "configurable": {
            "thread_id": thread_id
        }
    }

    state = graph.get_state(config)

    if not state:
        return []

    if not state.values:
        return []

    messages = state.values.get(
        "messages",
        []
    )

    history = []

    for msg in messages:

        parsed = format_message(msg)

        if parsed:
            history.append(parsed)

    return history