import os 
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()
llm_key = os.getenv("GROQ_API")

chat_bot = ChatGroq(model="llama-3.1-8b-instant",temperature=0.7,api_key=llm_key)
print("Chatbot are active pls type exit for exit...")
while True :
    try :
        user_input = input("Please enter your query...")
        if user_input.lower() == "exit" :
            print("Bye..have a great day")
            break
        response = chat_bot.invoke(user_input)
        print(response.content)
    except Exception as e :
        print(f"We are encountred with an error {e}")
