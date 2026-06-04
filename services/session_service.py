"""
Gestión de sesión.
"""

import streamlit as st


def initialize_session():
    """
    Inicializa variables.
    """

    if (
        "authenticated"
        not in st.session_state
    ):
        st.session_state.authenticated = False

    if (
        "user_id"
        not in st.session_state
    ):
        st.session_state.user_id = None

    if (
        "username"
        not in st.session_state
    ):
        st.session_state.username = None


def logout():
    """
    Cierra sesión.
    """

    keys = list(
        st.session_state.keys()
    )

    for key in keys:

        del st.session_state[key]