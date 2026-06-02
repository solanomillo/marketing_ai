"""
Gestión de memoria SQLite.
"""

import sqlite3

from langgraph.checkpoint.sqlite import (
    SqliteSaver
)


def get_checkpointer(
    db_path: str = "marketing.db"
):

    conn = sqlite3.connect(
        db_path,
        check_same_thread=False
    )

    return SqliteSaver(conn)