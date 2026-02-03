from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

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
    
@app.post("/chat")
async def chat(msg: Message):
    print(f"Received message: {msg.message}")
    response_text = f"Echo: {msg.message}"
    print(f"Sending response: {response_text}")
    return {
        "response": response_text,
        "success": True
    }
    
@app.get("/")
async def root():
    return {"message": "Server is running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
