from openai import OpenAI
from .ai_provider import AIProvider
from config import settings
import logging

logger = logging.getLogger(__name__)


class OpenRouterProvider(AIProvider):
    """
    Proveedor de IA usando OpenRouter.
    Implementa la interfaz AIProvider para cumplir con Dependency Inversion.
    """
    
    def __init__(self):
        """Inicializa el cliente de OpenAI con configuración de OpenRouter"""
        self.client = None
        self.model = settings.MODEL_NAME
        
        try:
            if not settings.OPENAI_API_KEY:
                logger.warning("OPENAI_API_KEY no configurada")
                return
                
            self.client = OpenAI(
                api_key=settings.OPENAI_API_KEY,
                base_url=settings.OPENROUTER_BASE_URL
            )
            logger.info("OpenRouterProvider inicializado correctamente")
        except Exception as e:
            logger.error(f"Error al inicializar OpenRouterProvider: {e}")
            self.client = None
    
    async def get_response(self, message: str) -> str:
        """
        Obtiene respuesta de OpenRouter.
        
        Args:
            message: Mensaje del usuario
            
        Returns:
            Respuesta generada por el modelo
            
        Raises:
            Exception: Si el cliente no está disponible o hay error en la API
        """
        if not self.client:
            raise Exception("OpenRouter client not initialized")
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "Eres un asistente útil y amigable."},
                    {"role": "user", "content": message}
                ]
            )
            
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Error en OpenRouter API: {e}")
            raise
    
    def is_available(self) -> bool:
        """Verifica si el proveedor está disponible"""
        return self.client is not None
    
    def get_name(self) -> str:
        """Retorna el nombre del proveedor"""
        return "OpenRouter"
