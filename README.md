# Langgraph AI Chatbot with Web Search Integration

This project is a web-based AI chatbot application that leverages the Langgraph framework and the Groq LLM (Large Language Model) to provide intelligent responses to user queries. The chatbot is enhanced with a web search tool, Tavily, which allows it to fetch and present relevant information from the web.

## Key Features

- **AI Chatbot**: Utilizes the Groq LLM to generate responses to user queries based on a defined system prompt.
- **Web Search Integration**: Incorporates the Tavily search tool to fetch relevant web search results and present them in a user-friendly format.
- **Customizable System Prompt**: Allows users to define the behavior and personality of the AI agent through a customizable system prompt.
- **User-Friendly Interface**: Built with Streamlit, providing an intuitive and interactive user interface for querying the AI agent.
- **Formatted Responses**: Formats web search results to include titles, snippets, and links, making the information easy to read and navigate.

## Components

1. **Frontend (`frontend.py`)**:
   - Built with Streamlit to provide a user-friendly interface.
   - Allows users to input queries, select models, and define system prompts.
   - Displays the AI agent's responses, including formatted web search results.

2. **Backend (`backend.py`)**:
   - Built with FastAPI to handle API requests from the frontend.
   - Processes user queries and interacts with the AI agent.
   - Returns formatted responses to the frontend.

3. **AI Agent (`ai_agent.py`)**:
   - Utilizes the Groq LLM to generate responses.
   - Integrates the Tavily search tool to fetch web search results.
   - Formats the search results to include relevant information (titles, snippets, and links).

## How It Works

1. **User Interaction**: Users interact with the chatbot through the Streamlit interface, inputting queries and defining system prompts.
2. **API Request**: The frontend sends the user query and other parameters to the backend via an API request.
3. **AI Processing**: The backend processes the request using the Groq LLM and, if enabled, the Tavily search tool.
4. **Response Formatting**: The AI agent formats the web search results and generates a response.
5. **Display Response**: The formatted response is sent back to the frontend and displayed to the user.

## Installation and Usage

### Prerequisites

- Python 3.7 or higher
- Pip (Python package installer)

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/langgraph-ai-chatbot.git
   cd langgraph-ai-chatbot
