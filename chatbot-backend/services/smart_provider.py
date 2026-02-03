from .ai_provider import AIProvider
import random
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class SmartProvider(AIProvider):
    """
    Proveedor de IA con respuestas predefinidas inteligentes.
    No requiere API key externa, siempre disponible como fallback.
    """
    
    def __init__(self):
        """Inicializa el proveedor de respuestas inteligentes"""
        logger.info("SmartProvider inicializado")
    
    async def get_response(self, message: str) -> str:
        """
        Genera una respuesta inteligente basada en patrones.
        
        Args:
            message: Mensaje del usuario
            
        Returns:
            Respuesta generada
        """
        message_lower = message.lower()
        
        # Saludos
        if any(word in message_lower for word in ['hola', 'buenos dias', 'buenas tardes', 'hey', 'hi']):
            responses = [
                "¡Hola! ¿En qué puedo ayudarte hoy?",
                "¡Hola! ¿Cómo estás?",
                "¡Hey! ¿Qué tal?",
            ]
            return random.choice(responses)
        
        # Estado/cómo estás
        if any(word in message_lower for word in ['como estas', 'cómo estás', 'que tal', 'qué tal']):
            responses = [
                "¡Estoy muy bien, gracias! ¿Y tú?",
                "Genial, listo para ayudarte. ¿Qué necesitas?",
                "Todo bien por aquí. ¿En qué puedo asistirte?",
            ]
            return random.choice(responses)
        
        # Fecha/hora
        if any(word in message_lower for word in ['fecha', 'dia', 'día', 'hoy']):
            now = datetime.now()
            dias_semana = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
            dia_semana = dias_semana[now.weekday()]
            return f"Hoy es {dia_semana}, {now.strftime('%d de %B de %Y')}."
        
        if any(word in message_lower for word in ['hora', 'tiempo']):
            now = datetime.now()
            return f"Son las {now.strftime('%H:%M')}."
        
        # Ayuda
        if any(word in message_lower for word in ['ayuda', 'help', 'que puedes hacer', 'qué puedes hacer']):
            return "Puedo responder preguntas, conversar contigo y ayudarte con información básica. ¿Qué te gustaría saber?"
        
        # Nombre
        if any(word in message_lower for word in ['como te llamas', 'cómo te llamas', 'tu nombre', 'quien eres', 'quién eres']):
            return "Soy un asistente virtual creado para ayudarte. ¿En qué puedo asistirte?"
        
        # Despedida
        if any(word in message_lower for word in ['adios', 'adiós', 'chao', 'bye', 'hasta luego']):
            responses = [
                "¡Hasta luego! Que tengas un excelente día.",
                "¡Adiós! Vuelve cuando necesites ayuda.",
                "¡Nos vemos! Cuídate.",
            ]
            return random.choice(responses)
        
        # Gracias
        if any(word in message_lower for word in ['gracias', 'thanks', 'thank you']):
            responses = [
                "¡De nada! Estoy aquí para ayudarte.",
                "¡Con gusto! ¿Necesitas algo más?",
                "¡No hay de qué! 😊",
            ]
            return random.choice(responses)
        
        # Respuesta por defecto
        default_responses = [
            f"Interesante que menciones '{message}'. ¿Podrías contarme más?",
            f"Entiendo. ¿Hay algo específico sobre '{message}' que quieras saber?",
            "Hmm, déjame pensar... ¿Podrías darme más detalles?",
            "Es una buena pregunta. ¿Qué aspecto específico te interesa?",
        ]
        return random.choice(default_responses)
    
    def is_available(self) -> bool:
        """Este proveedor siempre está disponible"""
        return True
    
    def get_name(self) -> str:
        """Retorna el nombre del proveedor"""
        return "Smart"
