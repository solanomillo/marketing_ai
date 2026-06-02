import streamlit as st

from graph.marketing_graph import (
    build_marketing_graph
)

from memory.sqlite_memory import (
    get_checkpointer
)

@st.cache_resource
def get_graph():

    memory = get_checkpointer()

    return build_marketing_graph(
        checkpointer=memory
    )