from pydantic import BaseModel
from typing import Optional


class Message(BaseModel):
    """Modelo para mensajes entrantes del chat"""
    message: str
    user_id: str = "default"


class ChatResponse(BaseModel):
    """Modelo para respuestas del chatbot"""
    response: str
    success: bool
    error: Optional[str] = None