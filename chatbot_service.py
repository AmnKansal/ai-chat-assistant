import os 
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
llm_key = os.getenv("GROQ_API")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant who explains things in a simple way."),
    ("human", "{user_input}")
])

chat_bot = ChatGroq(model="llama-3.1-8b-instant", temperature=0.7, api_key=llm_key)
print("Chatbot is active. Please type exit to quit...")

def enable_chatbot(user_input: str) -> str:
    try:
        formatted_prompt = prompt.format_messages(user_input=user_input)
        response = chat_bot.invoke(formatted_prompt)
        return response.content
    except Exception as e:
        return f"Error: {e}"