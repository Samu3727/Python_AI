from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import chat_router, health_router
from config import settings
import logging
import sys

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Información de inicio
logger.info("=== Iniciando servidor ===")
logger.info(f"Python version: {sys.version}")
logger.info(f"OPENAI_API_KEY configurada: {settings.is_openai_configured()}")

# Crear aplicación FastAPI
app = FastAPI(
    title="Chatbot API",
    description="API REST para chatbot con soporte múltiple de proveedores IA",
    version="2.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=settings.CORS_CREDENTIALS,
    allow_methods=settings.CORS_METHODS,
    allow_headers=settings.CORS_HEADERS,
)

# Registrar routers
app.include_router(chat_router)
app.include_router(health_router)


@app.get("/")
async def root():
    """Endpoint raíz con información básica del servidor"""
    return {
        "message": "Chatbot API v2.0 - Refactorizado con principios SOLID",
        "docs": "/docs",
        "health": "/health"
    }


if __name__ == "__main__":
    import uvicorn
    logger.info(f"Iniciando uvicorn en {settings.HOST}:{settings.PORT}")
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)