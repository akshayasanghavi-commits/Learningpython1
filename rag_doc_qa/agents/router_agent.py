# agents/router_agent.py

from crewai import Agent

def create_router(llm):

    router = Agent(
        role="Intelligent Query Router",
        goal="""
        Decide which data source should answer the question.

        Choose ONLY ONE:
        - PDF
        - SQL
        - WEB

        Respond with only one word.
        """,
        backstory="""
        You are an expert AI system architect.
        You analyze user questions and route them
        to the correct data source.
        """,
        llm=llm,
        verbose=True
    )

    return router