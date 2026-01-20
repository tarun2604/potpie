import os
from pydantic_ai.agent import Agent
from pydantic_ai.common_tools.tavily import tavily_search_tool

os.environ["GROQ_API_KEY"] = "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"
TAVILY_API_KEY = "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"

agent = Agent(
    "groq:llama-3.1-8b-instant",
    tools=[tavily_search_tool(TAVILY_API_KEY)],
    system_prompt="Search Tavily for the given query and return the results.",
)

def get_search_results(query: str) -> str:
    result = agent.run_sync(query)
    return result.output
