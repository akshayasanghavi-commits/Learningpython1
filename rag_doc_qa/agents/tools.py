from retrieval.search import DocumentSearcher
from crewai.tools import tool

searcher = DocumentSearcher()


@tool("retrieve_tool")
def retrieve_tool(query: str) -> str:
    """Search documents and return top results joined as a single string."""
    results = searcher.search(query, top_k=3)
    return "\n\n".join(results)