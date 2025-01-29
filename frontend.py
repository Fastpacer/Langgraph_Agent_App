# Step 1- Setup UI with streamlit
import streamlit as st
import os
import subprocess
import time

# Start the FastAPI backend
backend_process = subprocess.Popen(["uvicorn", "backend:app", "--host", "0.0.0.0", "--port", "8006"])
time.sleep(5)  # Give the backend some time to start

st.set_page_config(page_title="Langgraph Agent UI", page_icon="🤖", layout="centered")
st.title("AI chatbot Agent with Langgraph and Search Tool")
st.write("Create and interact with AI agents")

system_prompt = st.text_area("Define your AI agent", height=75, placeholder="Enter your AI agent prompt here")

MODEL_NAMES_GROK = ["llama-3.1-8b-instant", "mistral-8x7b-32786", "llama-3.3-70b-versatile"]
selected_model = st.selectbox("Select a model", MODEL_NAMES_GROK)
allow_web_search = st.checkbox("Allow web search")
user_query = st.text_area("Enter your query", height=145, placeholder="Enter your query here")

# Use local URL for API
API_URL = "http://127.0.0.1:8006/chat"

if st.button("Ask Agent"):
    if user_query.strip():
        import requests

        payload = {
            "model_name": selected_model,
            "model_provider": "groq",
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }

        try:
            response = requests.post(API_URL, json=payload)
            response.raise_for_status()  # Raise an error for bad status codes
            if response.status_code == 200:
                response_data = response.json()
                st.write("Agent's Response:")
                for message in response_data.get("messages", []):
                    st.write(message.get("content", "No content"))
            else:
                st.error(f"Error: {response.status_code}")
        except requests.exceptions.RequestException as e:
            st.error(f"Connection error: {e}")

# Stop the FastAPI backend when the Streamlit app stops
def stop_backend():
    backend_process.terminate()

# Register the stop_backend function to be called when the script exits
import atexit
atexit.register(stop_backend)
