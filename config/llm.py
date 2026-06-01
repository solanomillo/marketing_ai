"""
Inicialización centralizada del medelo LLM
"""
from langchain_google_genai import ChatGoogleGenerativeAI
from config.settings import settings

def get_llm():
    """
    Retorna instancia configurada del modelo Gemini
    """
    llm = ChatGoogleGenerativeAI(
        model=settings.MODEL_NAME,
        temperature=settings.TEMPERATURE,
        api_key=settings.GOOGLE_API_KEY
    )
    
    return llm
    
