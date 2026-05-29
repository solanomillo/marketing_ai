"""
Herramienta de búsqueda web con Tavily.
"""

from langchain_tavily import TavilySearch

from config.settings import settings


# Tool oficial Tavily para LangChain
tavily_tool = TavilySearch(
    tavily_api_key=settings.TAVILY_API_KEY,
    max_results=5,
    topic="general",
)