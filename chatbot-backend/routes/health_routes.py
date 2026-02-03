from fastapi import APIRouter
from services import get_chat_service
from config import settings

router = APIRouter(
    prefix="/health",
    tags=["health"]
)


@router.get("/")
async def health_check():
    """
    Endpoint para verificar el estado del servidor y del proveedor de IA.
    
    Returns:
        Estado del servidor y información del proveedor
    """
    chat_service = get_chat_service()
    provider_info = chat_service.get_provider_info()
    
    return {
        "status": "ok",
        "provider": provider_info["provider"],
        "provider_available": provider_info["available"],
        "openai_configured": settings.is_openai_configured()
    }
