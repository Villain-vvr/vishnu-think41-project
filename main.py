from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from backend.chatbot import handle_query

app = FastAPI()

# Allow frontend to access backend API (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For dev, allow all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/query")
async def query(request: Request):
    data = await request.json()
    user_input = data.get("question", "")
    response = handle_query(user_input)
    return {"answer": response}