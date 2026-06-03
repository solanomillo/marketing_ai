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
    remove_thread,
    generate_title,
)

from memory.conversation_memory import (
    update_title,
)

from services.streaming_service import get_agent_label

# ==================================================
# CONFIG
# ==================================================

st.set_page_config(
    page_title="Marketing AI",
    page_icon="🚀",
    layout="wide",
)


# ==================================================
# SESSION
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
            ),
            key="conversation_selector"
        )

        st.session_state.thread_id = (
            threads[selected]
        )

        if st.button(
            "🗑 Eliminar conversación",
            use_container_width=True,
        ):

            remove_thread(
                st.session_state.thread_id
            )

            st.session_state.loaded_thread = None
            st.session_state.messages = []

            st.rerun()

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


# ==================================================
# GRAPH
# ==================================================

graph = get_graph()


# ==================================================
# HISTORIAL
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
# TITULO
# ==================================================

st.title(
    "🚀 Marketing AI Multiagente"
)


# ==================================================
# CHAT HISTORY
# ==================================================

for msg in st.session_state.messages:

    with st.chat_message(
        msg["role"]
    ):

        st.markdown(
            msg["content"]
        )


# ==================================================
# INPUT
# ==================================================

prompt = st.chat_input(
    "Escribe tu solicitud..."
)

if prompt:

    # --------------------------------
    # Título automático
    # --------------------------------

    if len(
        st.session_state.messages
    ) == 0:

        title = generate_title(
            prompt
        )

        update_title(
            st.session_state.thread_id,
            title,
        )

    # --------------------------------
    # Usuario
    # --------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message(
        "user"
    ):
        st.markdown(prompt)

    config = {
        "configurable": {
            "thread_id":
            st.session_state.thread_id
        }
    }

    # --------------------------------
    # Streaming
    # --------------------------------

    answer = ""

    with st.chat_message(
        "assistant"
    ):

        status_box = st.empty()

        final_box = st.empty()

        events = graph.stream(
            {
                "messages": [
                    (
                        "user",
                        prompt
                    )
                ]
            },
            config=config,
            stream_mode="updates",
        )

        for event in events:

            for node_name in event.keys():

                if node_name in [
                    "supervisor",
                    "content_agent",
                    "social_agent",
                    "seo_agent",
                    "ads_agent",
                ]:

                    label = get_agent_label(
                        node_name
                    )

                    status_box.info(
                        f"{label} trabajando..."
                    )

        status_box.success(
            "✅ Proceso completado"
        )

        # --------------------------------
        # Obtener respuesta final REAL
        # --------------------------------

        state = graph.get_state(
            config
        )

        messages = state.values.get(
            "messages",
            []
        )

        if messages:

            last_message = messages[-1]

            content = (
                last_message.content
            )

            if isinstance(
                content,
                list
            ):

                answer = "\n".join(
                    item.get(
                        "text",
                        ""
                    )
                    for item in content
                    if isinstance(
                        item,
                        dict
                    )
                )

            else:

                answer = str(
                    content
                )

        final_box.markdown(
            answer
        )
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
        }
    )

    st.rerun()