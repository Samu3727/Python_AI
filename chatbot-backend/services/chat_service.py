from models import Message, ChatResponse
from .ai_provider import AIProvider
import logging

logger = logging.getLogger(__name__)


class ChatService:
    """
    Servicio para manejar la lógica de chat.
    Implementa Single Responsibility: solo maneja lógica de negocio del chat.
    Implementa Dependency Inversion: depende de AIProvider (abstracción), no de implementaciones concretas.
    """
    
    def __init__(self, ai_provider: AIProvider):
        """
        Inicializa el servicio con un proveedor de IA.
        
        Args:
            ai_provider: Proveedor de IA a utilizar
        """
        self.ai_provider = ai_provider
        logger.info(f"ChatService inicializado con proveedor: {ai_provider.get_name()}")
    
    async def send_message(self, message: Message) -> ChatResponse:
        """
        Procesa un mensaje y obtiene una respuesta.
        
        Args:
            message: Mensaje del usuario
            
        Returns:
            ChatResponse con la respuesta o error
        """
        try:
            # Validar que el proveedor esté disponible
            if not self.ai_provider.is_available():
                logger.error("Proveedor de IA no disponible")
                return ChatResponse(
                    response="",
                    success=False,
                    error="AI provider not available"
                )
            
            # Log del mensaje entrante
            logger.info(f"Procesando mensaje de usuario '{message.user_id}': {message.message}")
            
            # Obtener respuesta del proveedor
            response_text = await self.ai_provider.get_response(message.message)
            
            # Log de la respuesta
            logger.info(f"Respuesta generada: {response_text}")
            
            return ChatResponse(
                response=response_text,
                success=True
            )
            
        except Exception as e:
            logger.error(f"Error al procesar mensaje: {type(e).__name__}: {str(e)}")
            return ChatResponse(
                response="",
                success=False,
                error=str(e)
            )
    
    def get_provider_info(self) -> dict:
        """
        Obtiene información del proveedor actual.
        
        Returns:
            Diccionario con información del proveedor
        """
        return {
            "provider": self.ai_provider.get_name(),
            "available": self.ai_provider.is_available()
        }


def get_chat_service() -> ChatService:
    """
    Factory para obtener una instancia de ChatService.
    Útil para dependency injection en FastAPI.
    
    Returns:
        ChatService configurado con el proveedor apropiado
    """
    from .provider_factory import get_ai_provider
    provider = get_ai_provider()
    return ChatService(provider)
