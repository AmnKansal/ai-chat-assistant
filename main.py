from fastapi import FastAPI,status
from chatbot_service import enable_chatbot

app = FastAPI()

@app.get("/welcome",status_code=status.HTTP_200_OK)
def welcome_user() -> dict :
    return {"message":"welcome to my ai chatbot assistant"}

@app.post("/enablechatbot")
def get_enable_chatbot(query:str) -> dict :
    response = enable_chatbot(query)
    return {"data":response}