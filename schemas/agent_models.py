"""
Schemas internos de agentes.
"""

from pydantic import BaseModel, Field
from typing import List


class ContentTask(BaseModel):
    """
    Tarea para agente de contenido.
    """

    topic: str

    platform: str

    target_audience: str


class SEOTask(BaseModel):
    """
    Tarea SEO.
    """

    topic: str

    competitors: List[str] = []


class AdsTask(BaseModel):
    """
    Tarea publicitaria.
    """

    platform: str

    budget: float

    audience: str