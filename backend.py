from pydantic import BaseModel
from typing import List
from fastapi import FastAPI, HTTPException
from ai_agent import get_response_from_ai_agent
import logging

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool

ALLOWED_MODEL_NAMES = ["llama-3.1-8b-instant", "mistral-8x7b-32786", "llama-3.3-70b-versatile"]

app = FastAPI(title="Langgraph AI Agent")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.post("/chat")
def chat_endpoint(request: RequestState):
    """
    API endpoint to interact with the chatbot using lang-graph and search tools 
    """
    try:
        llm_id = request.model_name
        query = request.messages
        allow_search = request.allow_search
        system_prompt = request.system_prompt
        provider = request.model_provider

        logger.info(f"Received request: {request}")

        if request.model_name not in ALLOWED_MODEL_NAMES:
            raise HTTPException(status_code=400, detail="Model name not allowed. Please select a valid model")

        # Create AI Agent and fetch a response from it
        response = get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider)
        logger.info(f"AI Agent response: {response}")
        return response
    except Exception as e:
        logger.error(f"Error in chat_endpoint: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
