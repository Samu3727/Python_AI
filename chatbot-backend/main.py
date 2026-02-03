from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI()

#Configuarción del CORS.

app.add_middleware(
    
    CORSMiddleware, 
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Configuración del OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class Message(BaseModel):
    message: str
    user_id: str = "default"
    
@app.post("/chat")
async def chat(msg: Message):
    try:
        response = client.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = [
                {"role": "system", "content": "Eres un asistente útil y amigable."},
                {"role": "user", "content": msg.message}
            ]
        )
        return {
            "response": response.choices[0].message.content,
            "success": True
        }
        
    except Exception as e:
        
        return {"error": str(e), "success": False}
    
@app.get("/")
async def root():
    
    return {"message": "API del chatboy funcionando correctamente."}