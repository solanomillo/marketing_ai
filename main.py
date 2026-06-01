from graph.marketing_graph import (
    build_marketing_graph
)


def main():

    graph = build_marketing_graph()

    result = graph.invoke(
        {
            "messages": [
                (
                    "user",
                    """
                    Genera hashtags para barbería.
                    """
                )
            ]
        }
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