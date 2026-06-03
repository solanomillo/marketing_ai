"""
Pantalla de autenticación.
"""
import sys
import os

sys.path.insert(
    0,
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)
import streamlit as st

from memory.user_memory import (
    create_user,
    get_user_by_username,
)

from services.auth_service import (
    hash_password,
    verify_password,
)


def show_auth_page():
    """
    Login y registro.
    """

    st.title(
        "🔐 Marketing AI"
    )

    tab_login, tab_register = st.tabs(
        [
            "Iniciar sesión",
            "Registrarse",
        ]
    )

    # ==========================
    # LOGIN
    # ==========================

    with tab_login:

        username = st.text_input(
            "Usuario",
            key="login_user",
        )

        password = st.text_input(
            "Contraseña",
            type="password",
            key="login_pass",
        )

        if st.button(
            "Ingresar",
            use_container_width=True,
        ):

            user = get_user_by_username(
                username
            )

            if not user:

                st.error(
                    "Usuario no encontrado"
                )

            elif not verify_password(
                password,
                user["password_hash"],
            ):

                st.error(
                    "Contraseña incorrecta"
                )

            else:

                st.session_state.user_id = (
                    user["id"]
                )

                st.session_state.username = (
                    user["username"]
                )

                st.session_state.authenticated = (
                    True
                )

                st.rerun()

    # ==========================
    # REGISTRO
    # ==========================

    with tab_register:

        username = st.text_input(
            "Nuevo usuario",
            key="register_user",
        )

        password = st.text_input(
            "Nueva contraseña",
            type="password",
            key="register_pass",
        )

        if st.button(
            "Crear cuenta",
            use_container_width=True,
        ):

            existing = (
                get_user_by_username(
                    username
                )
            )

            if existing:

                st.error(
                    "El usuario ya existe"
                )

            elif len(password) < 6:

                st.error(
                    "La contraseña debe tener al menos 6 caracteres"
                )

            else:

                create_user(
                    username,
                    hash_password(
                        password
                    ),
                )

                st.success(
                    "Usuario creado correctamente"
                )
                
