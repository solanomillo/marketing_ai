"""
Persistencia de conversaciones.
"""

import sqlite3
from pathlib import Path

DB_PATH = (
    Path(__file__).parent.parent
    / "marketing.db"
)


def initialize_conversations_table():
    """
    Crea tabla conversaciones.
    """

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversations (
            thread_id TEXT PRIMARY KEY,
            user_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def create_conversation(
    thread_id: str,
    user_id: int,
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
            user_id,
            title
        )
        VALUES (?, ?, ?)
    """, (
        thread_id,
        user_id,
        title,
    ))

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
    """, (
        title,
        thread_id,
    ))

    conn.commit()
    conn.close()


def get_conversations(
    user_id: int,
):
    """
    Obtiene conversaciones del usuario.
    """

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            thread_id,
            title
        FROM conversations
        WHERE user_id = ?
        ORDER BY created_at DESC
    """, (user_id,))

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