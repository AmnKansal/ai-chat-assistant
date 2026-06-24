from fastapi import FastAPI,status
from chatbot_service import get_response
from schemas.request import RequestChatBotQuery
from schemas.response import APIResponse

app = FastAPI()

@app.get("/welcome",status_code=status.HTTP_200_OK)
def welcome_user() -> dict :
    return APIResponse.success(data="Welcome to AI Chatbot!")

@app.post("/chat", status_code=status.HTTP_200_OK)
def get_chat_response(request: RequestChatBotQuery):
    try:
        response = get_response(request.query)
        return APIResponse.success(data=response)
    except Exception as e:
        return APIResponse.error(message=str(e))