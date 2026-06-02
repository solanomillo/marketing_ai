"""
Interfaz principal de Marketing AI.
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

from services.graph_service import get_graph

from services.chat_service import (
    load_chat_history,
)

from services.thread_service import (
    initialize_threads,
    create_new_thread,
    load_threads,
)


# ==================================================
# CONFIG
# ==================================================

st.set_page_config(
    page_title="Marketing AI",
    page_icon="🚀",
    layout="wide",
)


# ==================================================
# THREADS
# ==================================================

if "thread_id" not in st.session_state:

    st.session_state.thread_id = (
        initialize_threads()
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

if "loaded_thread" not in st.session_state:
    st.session_state.loaded_thread = None


# ==================================================
# SIDEBAR
# ==================================================

threads = load_threads()

with st.sidebar:

    st.title("⚙️ Marketing AI")

    if threads:

        selected = st.radio(
            "Conversaciones",
            options=list(
                threads.keys()
            )
        )

        st.session_state.thread_id = (
            threads[selected]
        )

    if st.button(
        "➕ Nueva conversación",
        use_container_width=True,
    ):

        st.session_state.thread_id = (
            create_new_thread()
        )

        st.session_state.messages = []

        st.session_state.loaded_thread = None

        st.rerun()

    st.divider()

    st.code(
        st.session_state.thread_id
    )


# ==================================================
# GRAPH
# ==================================================

graph = get_graph()


# ==================================================
# CARGAR HISTORIAL
# ==================================================

if (
    st.session_state.loaded_thread
    != st.session_state.thread_id
):

    st.session_state.messages = (
        load_chat_history(
            graph,
            st.session_state.thread_id,
        )
    )

    st.session_state.loaded_thread = (
        st.session_state.thread_id
    )


# ==================================================
# UI
# ==================================================

st.title(
    "🚀 Marketing AI Multiagente"
)

for msg in st.session_state.messages:

    with st.chat_message(
        msg["role"]
    ):
        st.markdown(
            msg["content"]
        )


# ==================================================
# CHAT
# ==================================================

prompt = st.chat_input(
    "Escribe tu solicitud..."
)

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    config = {
        "configurable": {
            "thread_id":
            st.session_state.thread_id
        }
    }

    with st.chat_message(
        "assistant"
    ):

        with st.spinner(
            "Analizando..."
        ):

            result = graph.invoke(
                {
                    "messages": [
                        (
                            "user",
                            prompt
                        )
                    ]
                },
                config=config,
            )

            last_message = (
                result["messages"][-1]
            )

            if isinstance(
                last_message.content,
                list
            ):

                answer = "\n".join(
                    item.get(
                        "text",
                        ""
                    )
                    for item in last_message.content
                    if isinstance(
                        item,
                        dict
                    )
                )

            else:

                answer = (
                    last_message.content
                )

            st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
        }
    )