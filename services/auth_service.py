"""
Servicios de autenticación.
"""

import bcrypt


def hash_password(
    password: str,
) -> str:
    """
    Genera hash seguro.
    """

    return bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt(),
    ).decode()


def verify_password(
    password: str,
    password_hash: str,
) -> bool:
    """
    Verifica contraseña.
    """

    return bcrypt.checkpw(
        password.encode(),
        password_hash.encode(),
    )