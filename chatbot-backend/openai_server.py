from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import os
import sys

print("Iniciando servidor...")
print(f"Python version: {sys.version}")
print(f"OPENAI_API_KEY configurada: {bool(os.getenv('OPENAI_API_KEY'))}")

app = FastAPI()

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuración del OpenAI (usando OpenRouter)
try:
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url="https://openrouter.ai/api/v1"
    )
    print("Cliente OpenAI inicializado correctamente (usando OpenRouter)")
except Exception as e:
    print(f"Error al inicializar OpenAI: {e}")
    client = None

class Message(BaseModel):
    message: str
    user_id: str = "default"
    
@app.post("/chat")
async def chat(msg: Message):
    print(f"\n=== Nueva petición ===")
    print(f"Mensaje recibido: '{msg.message}'")
    print(f"User ID: {msg.user_id}")
    
    if not client:
        print("ERROR: Cliente OpenAI no inicializado")
        return {"error": "OpenAI client not initialized", "success": False}
    
    try:
        print("Llamando a OpenAI...")
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un asistente útil y amigable."},
                {"role": "user", "content": msg.message}
            ]
        )
        
        bot_response = response.choices[0].message.content
        print(f"Respuesta de OpenAI: '{bot_response}'")
        print(f"=== Fin petición ===\n")
        
        return {
            "response": bot_response,
            "success": True
        }
        
    except Exception as e:
        print(f"ERROR en chat: {type(e).__name__}: {str(e)}")
        import traceback
        traceback.print_exc()
        return {"error": str(e), "success": False}
    
@app.get("/")
async def root():
    return {"message": "API del chatbot funcionando con OpenAI"}

@app.get("/health")
async def health():
    return {
        "status": "ok",
        "openai_configured": bool(client)
    }

if __name__ == "__main__":
    import uvicorn
    print("Iniciando uvicorn...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
