"""
Inicialización de la base de datos.
"""

from memory.user_memory import (
    create_users_table,
)

from memory.conversation_memory import (
    initialize_conversations_table,
)


def initialize_database():
    """
    Crea todas las tablas necesarias.
    """

    create_users_table()

    initialize_conversations_table()