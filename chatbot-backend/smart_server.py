from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    message: str
    user_id: str = "default"

# Respuestas inteligentes simuladas
def get_smart_response(message: str) -> str:
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

@app.post("/chat")
async def chat(msg: Message):
    print(f"Received message: {msg.message}")
    response_text = get_smart_response(msg.message)
    print(f"Sending response: {response_text}")
    return {
        "response": response_text,
        "success": True
    }
    
@app.get("/")
async def root():
    return {"message": "Smart chatbot server is running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
