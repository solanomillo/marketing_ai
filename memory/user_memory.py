"""
Gestión de usuarios.
"""

import sqlite3

from pathlib import Path


DB_PATH = (
    Path(__file__).parent.parent
    / "marketing.db"
)


def get_connection():
    """
    Retorna conexión SQLite.
    """

    return sqlite3.connect(
        DB_PATH
    )


def create_users_table():
    """
    Crea tabla usuarios.
    """

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    conn.commit()
    conn.close()


def create_user(
    username: str,
    password_hash: str,
):
    """
    Crea usuario.
    """

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO users (
            username,
            password_hash
        )
        VALUES (?, ?)
        """,
        (
            username,
            password_hash,
        ),
    )

    conn.commit()

    user_id = cursor.lastrowid

    conn.close()

    return user_id


def get_user_by_username(
    username: str,
):
    """
    Busca usuario por username.
    """

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            id,
            username,
            password_hash
        FROM users
        WHERE username = ?
        """,
        (username,),
    )

    row = cursor.fetchone()

    conn.close()

    if not row:
        return None

    return {
        "id": row[0],
        "username": row[1],
        "password_hash": row[2],
    }


def get_user_by_id(
    user_id: int,
):
    """
    Busca usuario por ID.
    """

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            id,
            username
        FROM users
        WHERE id = ?
        """,
        (user_id,),
    )

    row = cursor.fetchone()

    conn.close()

    if not row:
        return None

    return {
        "id": row[0],
        "username": row[1],
    }