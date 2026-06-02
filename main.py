from graph.marketing_graph import (
    build_marketing_graph
)

from memory.sqlite_memory import (
    get_checkpointer
)


def main():

    memory = get_checkpointer()

    graph = build_marketing_graph(
        checkpointer=memory
    )

    config = {
        "configurable": {
            "thread_id": "usuario_1"
        }
    }

    result = graph.invoke(
        {
            "messages": [
                (
                    "user",
                    """
                    De qué es mi negocio?.
                    """
                )
            ]
        },
        config=config,
    )
        
    
    # Extraer el último mensaje (respuesta final)
    ultimo_mensaje = result['messages'][-1]
    
    # Obtener el contenido
    if isinstance(ultimo_mensaje.content, list):
        contenido = ultimo_mensaje.content[0]['text']
    else:
        contenido = ultimo_mensaje.content
    
    print(contenido)

if __name__ == "__main__":
    main()