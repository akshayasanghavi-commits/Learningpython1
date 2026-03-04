from duckduckgo_search import DDGS
from crewai.tools import BaseTool


class WebSearchTool(BaseTool):
    name :str = "Web Search Tool"
    description :str = "Search the web for latest information."

    def _run(self, query: str):
        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=3)
            return str(results)