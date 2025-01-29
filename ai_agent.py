import os
from dotenv import load_dotenv
import logging

load_dotenv()
GROQ_API_KEY = os.environ.get('GROQ_API_KEY')
TAVILY_API_KEY = os.environ.get('TAVILY_API_KEY')

from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

groq_llm = ChatGroq(model="llama-3.1-8b-instant")
search_tool = TavilySearchResults(max_results=True, api_key=TAVILY_API_KEY)

def format_tool_response(tool_response):
    # Extract and format the relevant information from the tool response
    formatted_response = ""
    for result in tool_response.get("results", []):
        title = result.get("title", "No title")
        link = result.get("link", "No link")
        snippet = result.get("snippet", "No snippet")
        formatted_response += f"**{title}**\n{snippet}\n[Read more]({link})\n\n"
    return formatted_response

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    try:
        logger.info(f"get_response_from_ai_agent called with llm_id: {llm_id}, query: {query}, allow_search: {allow_search}, system_prompt: {system_prompt}, provider: {provider}")

        if provider != "groq":
            raise ValueError(f"Unsupported provider: {provider}")

        model = groq_llm

        tools = [search_tool] if allow_search else []

        agent = create_react_agent(
            model=model,
            tools=tools,
            state_modifier=system_prompt
        )

        state = {"messages": query}
        response = agent.invoke(state)
        logger.info(f"AI Agent response: {response}")

        # Handle tool calls
        messages = response.get("messages", [])
        for message in messages:
            if "tool_calls" in message:
                for tool_call in message["tool_calls"]:
                    tool_name = tool_call["tool_name"]
                    tool_input = tool_call["tool_input"]
                    if tool_name == "tavily_search_results_json":
                        tool_response = search_tool.invoke(tool_input)
                        formatted_response = format_tool_response(tool_response)
                        message["content"] = formatted_response

        return response
    except Exception as e:
        logger.error(f"Error in get_response_from_ai_agent: {e}")
        raise