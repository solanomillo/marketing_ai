"""
Gestión de conversaciones.
"""

import uuid

from memory.conversation_memory import (
    initialize_conversations_table,
    create_conversation,
    get_conversations,
    delete_conversation,
)


def initialize_threads(
    user_id: int,
):
    """
    Inicializa conversaciones
    del usuario.
    """

    initialize_conversations_table()

    conversations = get_conversations(
        user_id
    )

    if not conversations:

        thread_id = str(
            uuid.uuid4()
        )

        create_conversation(
            thread_id=thread_id,
            user_id=user_id,
            title="Nueva conversación",
        )

        return thread_id

    return conversations[0][0]


def create_new_thread(
    user_id: int,
):
    """
    Crea conversación.
    """

    thread_id = str(
        uuid.uuid4()
    )

    create_conversation(
        thread_id=thread_id,
        user_id=user_id,
        title="Nueva conversación",
    )

    return thread_id


def load_threads(
    user_id: int,
):
    """
    Obtiene conversaciones
    del usuario.
    """

    conversations = get_conversations(
        user_id
    )

    return {
        title: thread_id
        for thread_id, title
        in conversations
    }


def remove_thread(
    thread_id: str,
):
    """
    Elimina conversación.
    """

    delete_conversation(
        thread_id
    )


def generate_title(
    text: str,
):
    """
    Genera título corto.
    """

    text = text.strip()

    if len(text) <= 20:
        return text

    return text[:20] + "..."