from agents.content_agent import content_agent

def main():
    result = content_agent.invoke(
        {
            "messages": [
                (
                    "user",
                    "Genera una idea viral para una barbería"
                )
            ]
        }
    )
    
    # Extraer solo el contenido del último mensaje
    ultimo_mensaje = result['messages'][-1]
    
    # Si el contenido es una lista (como en Gemini)
    if isinstance(ultimo_mensaje.content, list):
        contenido = ultimo_mensaje.content[0]['text']
    else:
        contenido = ultimo_mensaje.content
    
    print(contenido)

if __name__ == "__main__":
    main()