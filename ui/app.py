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
from graph.marketing_graph import build_marketing_graph
from memory.sqlite_memory import get_checkpointer

st.set_page_config(
    page_title="Marketing AI",
    page_icon="🚀",
    layout="wide",
)

# Inicializar el grafo UNA SOLA VEZ (usando cache de Streamlit)
@st.cache_resource
def get_graph():
    """Carga el grafo una sola vez y lo reutiliza"""
    memory = get_checkpointer()
    return build_marketing_graph(checkpointer=memory)

# Inicializar session state
if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

if "graph" not in st.session_state:
    st.session_state.graph = get_graph()

with st.sidebar:
    st.title("⚙️ Marketing AI")
    st.write(f"Thread: {st.session_state.thread_id[:8]}...")  # Mostrar solo parte del ID
    
    if st.button("🔄 Nueva conversación", use_container_width=True):
        # Generar nuevo thread_id
        st.session_state.thread_id = str(uuid.uuid4())
        # Limpiar mensajes mostrados
        st.session_state.messages = []
        # Forzar recarga de la página
        st.rerun()
    
    st.divider()
    st.caption("Consejo: Cada conversación tiene un ID único")

st.title("🚀 Marketing AI Multiagente")

# Mostrar mensajes existentes
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input del usuario
prompt = st.chat_input("Escribe tu solicitud...")

if prompt:
    # Agregar mensaje del usuario al estado
    st.session_state.messages.append({
        "role": "user",
        "content": prompt,
    })
    
    # Mostrar mensaje del usuario
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Preparar configuración para el grafo
    config = {
        "configurable": {
            "thread_id": st.session_state.thread_id
        }
    }
    
    # Invocar al grafo (usando el cacheado)
    with st.spinner("Procesando tu solicitud..."):
        try:
            result = st.session_state.graph.invoke(
                {"messages": [("user", prompt)]},
                config=config,
            )
            
            # Extraer la respuesta
            messages = result["messages"]
            answer = messages[-1].content[0]['text'] if isinstance(messages[-1].content, list) else messages[-1].content
            
            # Mostrar respuesta
            with st.chat_message("assistant"):
                st.markdown(answer)
            
            # Guardar en el historial
            st.session_state.messages.append({
                "role": "assistant",
                "content": answer,
            })
            
        except Exception as e:
            st.error(f"Error al procesar: {str(e)}")