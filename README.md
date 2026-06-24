# AI Chat Assistant

A production-style AI chatbot built with FastAPI and Groq LLM.

## Tech Stack
- Python
- FastAPI
- LangChain
- Groq (LLaMA 3.1)
- Pydantic
- UV (package manager)

## Project Structure
ai-chat-assistant/
├── main.py               # FastAPI routes
├── chatbot_service.py    # LLM logic
├── schemas/
│   ├── request.py        # Request models
│   └── response.py       # Response models
└── .env                  # API keys (not pushed)

## Setup
1. Clone the repo
2. Create .env file with your GROQ_API key
3. Run: uv add langchain langchain-groq python-dotenv fastapi uvicorn
4. Run: uvicorn main:app --reload
5. Open: http://localhost:8000/docs

## API Endpoints
- GET  /welcome → health check
- POST /chat    → send query, get AI response