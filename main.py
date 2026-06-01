from agents.supervisor import build_supervisor

def main():
    app = build_supervisor()

    response = app.invoke(
        {
            "messages": [
                (
                    "user",
                    """
                    Quiero una campaña para TikTok
                    para una barbería premium.
                    """
                )
            ]
        }
    )
    
    # Extraer el último mensaje (respuesta final)
    ultimo_mensaje = response['messages'][-1]
    
    # Obtener el contenido
    if isinstance(ultimo_mensaje.content, list):
        contenido = ultimo_mensaje.content[0]['text']
    else:
        contenido = ultimo_mensaje.content
    
    print(contenido)

if __name__ == "__main__":
    main()