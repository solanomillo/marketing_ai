"""
Persistencia de conversaciones.
"""

import sqlite3

DB_PATH = "marketing.db"


def initialize_conversations_table():
    """
    Crea tabla de conversaciones.
    """

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversations (
            thread_id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def create_conversation(
    thread_id: str,
    title: str,
):
    """
    Guarda conversación.
    """

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO conversations (
            thread_id,
            title
        )
        VALUES (?, ?)
    """, (thread_id, title))

    conn.commit()
    conn.close()


def update_title(
    thread_id: str,
    title: str,
):
    """
    Actualiza título.
    """

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
        UPDATE conversations
        SET title = ?
        WHERE thread_id = ?
    """, (title, thread_id))

    conn.commit()
    conn.close()


def get_conversations(
    user_id=None
):
    """
    Obtiene conversaciones.
    """

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            thread_id,
            title
        FROM conversations
        ORDER BY created_at DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def delete_conversation(
    thread_id: str,
):
    """
    Elimina conversación.
    """

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM conversations
        WHERE thread_id = ?
    """, (thread_id,))

    conn.commit()
    conn.close()