from .ai_provider import AIProvider
from .openrouter_provider import OpenRouterProvider
from .smart_provider import SmartProvider
import logging

logger = logging.getLogger(__name__)


def get_ai_provider() -> AIProvider:
    """
    Factory para obtener un proveedor de IA.
    Implementa Dependency Inversion: retorna la abstracción, no la implementación concreta.
    
    Intenta usar OpenRouter primero, si falla usa SmartProvider como fallback.
    
    Returns:
        AIProvider: Instancia del proveedor disponible
    """
    # Intentar con OpenRouter
    openrouter = OpenRouterProvider()
    if openrouter.is_available():
        logger.info(f"Usando proveedor: {openrouter.get_name()}")
        return openrouter
    
    # Fallback a SmartProvider
    logger.warning("OpenRouter no disponible, usando SmartProvider como fallback")
    smart = SmartProvider()
    logger.info(f"Usando proveedor: {smart.get_name()}")
    return smart
