import os
from typing import List


class Settings:
    """Configuración centralizada de la aplicación"""
    
    # API Keys
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    
    # OpenRouter Configuration
    OPENROUTER_BASE_URL: str = "https://openrouter.ai/api/v1"
    MODEL_NAME: str = "gpt-3.5-turbo"
    
    # CORS Configuration
    CORS_ORIGINS: List[str] = ["*"]
    CORS_CREDENTIALS: bool = True
    CORS_METHODS: List[str] = ["*"]
    CORS_HEADERS: List[str] = ["*"]
    
    # Server Configuration
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    def is_openai_configured(self) -> bool:
        """Verifica si la API key está configurada"""
        return bool(self.OPENAI_API_KEY)
