"""
Gestión de conversaciones.
"""

import uuid

from memory.conversation_memory import (
    initialize_conversations_table,
    create_conversation,
    get_conversations,
    delete_conversation,
    update_title,
)


def initialize_threads():

    initialize_conversations_table()

    conversations = get_conversations()

    if not conversations:

        thread_id = str(uuid.uuid4())

        create_conversation(
            thread_id,
            "Nueva conversación"
        )

        return thread_id

    return conversations[0][0]


def create_new_thread():

    thread_id = str(uuid.uuid4())

    create_conversation(
        thread_id,
        "Nueva conversación"
    )

    return thread_id


def load_threads():

    conversations = get_conversations()

    return {
        title: thread_id
        for thread_id, title
        in conversations
    }


def remove_thread(
    thread_id: str
):
    """
    Elimina conversación.
    """

    delete_conversation(
        thread_id
    )


def generate_title(
    text: str
):
    """
    Primeros 20 caracteres.
    """

    text = text.strip()

    if len(text) <= 20:
        return text

    return text[:20] + "..."