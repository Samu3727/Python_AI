from fastapi import APIRouter
from models import Message, ChatResponse
from services import get_chat_service
import logging

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/chat",
    tags=["chat"]
)


@router.post("/", response_model=ChatResponse)
async def chat(message: Message) -> ChatResponse:
    """
    Endpoint para enviar mensajes al chatbot.
    Implementa Single Responsibility: solo maneja la ruta, delega lógica al servicio.
    
    Args:
        message: Mensaje del usuario
        
    Returns:
        ChatResponse con la respuesta del bot
    """
    logger.info(f"=== Nueva petición de chat ===")
    logger.info(f"Usuario: {message.user_id}, Mensaje: {message.message}")
    
    # Obtener servicio de chat
    chat_service = get_chat_service()
    
    # Procesar mensaje
    response = await chat_service.send_message(message)
    
    logger.info(f"Respuesta enviada: success={response.success}")
    logger.info(f"=== Fin petición ===\n")
    
    return response
