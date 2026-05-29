"""
Configuración central del proyecto.
"""
from dotenv import load_dotenv
import os

# Cargar variables entorno
load_dotenv()


class Settings:
    """
    Configuración global del sistema.
    """

    GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY", "")

    TAVILY_API_KEY: str = os.getenv("TAVILY_API_KEY", "")

    MODEL_NAME: str = os.getenv(
        "MODEL_NAME",
        "gemini-3.5-flash"
    )

    TEMPERATURE: float = float(
        os.getenv("TEMPERATURE", 0.7)
    )

    DEBUG: bool = os.getenv(
        "DEBUG",
        "True"
    ).lower() == "true"


settings = Settings()