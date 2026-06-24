from pydantic import BaseModel

class RequestChatBotQuery(BaseModel):
    query:str