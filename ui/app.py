"""
Interfaz principal.
"""
# ui/app.py
import sys
import os
# Agregar el directorio raíz al path de Python
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import uuid
import streamlit as st
from services.graph_service import (
    get_graph
)

st.set_page_config(
    page_title="Marketing AI",
    page_icon="🚀",
    layout="wide",
)

if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(
        uuid.uuid4()
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:

    st.title("⚙️ Marketing AI")

    st.write(
        f"Thread: {st.session_state.thread_id}"
    )

    if st.button(
        "Nueva conversación"
    ):

        st.session_state.thread_id = str(
            uuid.uuid4()
        )

        st.session_state.messages = []

        st.rerun()
        
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

    with st.chat_message(
        "user"
    ):
        st.markdown(prompt)

    graph = get_graph()

    config = {
        "configurable": {
            "thread_id":
            st.session_state.thread_id
        }
    }
    
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
    
    messages = result["messages"]

    answer = messages[-1].content[0]['text'] if isinstance(messages[-1].content, list) else messages[-1].content
    
    with st.chat_message(
        "assistant"
    ):
        st.markdown(answer)
    
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
        }
    )