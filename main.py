"""
Prueba de modelos Pydantic.
"""

from schemas.responses import (
    ContentResponse
)


def main():

    response = ContentResponse(
        hook="El secreto de barbería que nadie conoce",
        caption="Transforma tu estilo hoy",
        hashtags=[
            "#barberia",
            "#viral",
            "#fyp"
        ],
        call_to_action="Reserva tu turno ahora"
    )

    print("\nRESPUESTA ESTRUCTURADA:\n")

    print(response.model_dump())


if __name__ == "__main__":
    main()