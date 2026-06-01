"""
Factory para creación de agentes
"""

from langchain.agents import create_agent
from config.llm import get_llm

def build_agents(name:str, system_prompt:str, tools:list):
    """
    Crea un agente reutilizable con el modelo de lenguaje especificado en la configuración
    y las herramientas proporcionadas.
    """
    llm = get_llm()
    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=system_prompt,
        name=name        
    )
    return agent
    