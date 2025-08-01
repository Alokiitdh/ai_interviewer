from langchain_tavily import TavilySearch
from dotenv import load_dotenv

load_dotenv()
# Create the Tavily Search tool
tavily_tool = TavilySearch(max_results = 5)