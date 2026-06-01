"""
Schemas de respuestas estructuradas.
"""

from pydantic import BaseModel, Field
from typing import List


class HashtagResponse(BaseModel):
    """
    Respuesta de hashtags.
    """

    hashtags: List[str] = Field(
        description="Lista de hashtags optimizados"
    )


class SEOResponse(BaseModel):
    """
    Respuesta SEO.
    """

    keywords: List[str] = Field(
        description="Keywords SEO"
    )

    meta_description: str = Field(
        description="Meta descripción optimizada"
    )

    seo_title: str = Field(
        description="Título SEO"
    )


class ContentResponse(BaseModel):
    """
    Respuesta de contenido.
    """

    hook: str = Field(
        description="Hook viral"
    )

    caption: str = Field(
        description="Caption principal"
    )

    hashtags: List[str] = Field(
        description="Hashtags sugeridos"
    )

    call_to_action: str = Field(
        description="CTA del contenido"
    )


class AdsResponse(BaseModel):
    """
    Respuesta publicitaria.
    """

    platform: str = Field(
        description="Plataforma publicitaria"
    )

    target_audience: str = Field(
        description="Audiencia objetivo"
    )

    ad_copy: str = Field(
        description="Texto del anuncio"
    )

    call_to_action: str = Field(
        description="CTA"
    )


class FinalMarketingResponse(BaseModel):
    """
    Respuesta final consolidada.
    """

    user_request: str

    content_strategy: str

    seo_strategy: str

    ads_strategy: str

    recommended_platforms: List[str]