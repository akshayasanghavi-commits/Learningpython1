from crewai import Agent, Task, Crew, LLM
from agents.tools import retrieve_tool
from agents.memory import ConversationMemory
from agents.sql_tool import SQLTool
from agents.web_tool import WebSearchTool
from agents.router_agent import create_router


web_tool = WebSearchTool()
sql_tool = SQLTool()

# -------------------------
# 1️⃣ Setup Local LLM via CrewAI Native Wrapper
# -------------------------

local_llm = LLM(
    model="ollama/mistral",
    temperature=0.3
)
router_agent = create_router(local_llm)

# -------------------------
# 2️⃣ Memory
# -------------------------

memory = ConversationMemory()


# -------------------------
# 3️⃣ Agents
# -------------------------

""""retriever_agent = Agent(
    role="Document Retrieval Specialist",
    goal="Retrieve relevant document context for the question.",
    backstory="Expert in semantic search and vector similarity.",
    tools=[retrieve_tool],
    llm=local_llm,
    verbose=True
)
"""

answer_agent = Agent(
    role="Answer Generator",
    goal="""
You can use:
- Document retrieval tool for PDF questions
- Database Query Tool for structured data
- Web Search Tool for real-time information

Choose the tool as per context given use only that tool .
Answer in short do not explain the answer. If you use a tool, only return the tool output as the answer.
""",
    backstory="Expert at forming structured and clear responses.",
    tools=[retrieve_tool, sql_tool, web_tool],
    llm=local_llm,
    max_iter=3,
    verbose=True
)

critique_agent = Agent(
    role="Answer Critic",
    goal="Critically evaluate the answer for accuracy and completeness.",
    backstory="Expert reviewer improving AI responses.",
    llm=local_llm,
    verbose=True
)


# -------------------------
# 4️⃣ Multi-Step Flow
# -------------------------

def run_pipeline(question):

      # STEP 1: ROUTE
    router_task = Task(
    description=f"""
    User Question:
    {question}

    Decide whether it should use:
    PDF
    SQL
    or WEB

    Respond with only one word.
    """,
     expected_output="A single word: PDF or SQL or WEB",
    agent=router_agent
       )

    router_crew = Crew(
      agents=[router_agent],
       tasks=[router_task],
      verbose=True
        )
    routing_result = router_crew.kickoff()
       # DEBUG print
    print("Raw router result:", routing_result)
    routing_text = routing_result.tasks_output[0]
# Extract properly
    if hasattr(routing_result, "raw"):
            routing_text = routing_result.raw
    else:
         routing_text = str(routing_result)

    routing_decision = routing_text.strip().upper()

    
    routing_decision = routing_text.strip().upper()

    print("Routing Decision:", routing_decision)
    # STEP 2: Call correct agent
     
    routing_decision = routing_decision.replace(".", "").strip()

    """ if "SQL" in routing_decision:
      routing_decision = "SQL"
    elif "WEB" in routing_decision:
       routing_decision = "WEB"
    else:
       routing_decision = "PDF"
    
    if routing_decision == "SQL":
        context = sql_tool.run("SELECT * FROM applicants;")
    
    elif routing_decision == "WEB":
        context = web_tool.run(question)

    else:
        context = retrieve_tool.run(question)"""

    previous_context = memory.get_context()

    answer_task = Task(
        description=f"""
        Previous Conversation:
        {previous_context}

        User Question:
        {question}
        Context:
        use this {routing_decision} tool to answer the question.

        Provide a clear and structured answer.
        """,
        expected_output="Final structured answer",
        agent=answer_agent
    )

    critique_task = Task(
        description="""
        Review the previous answer.
        Identify issues and suggest improvements.
        """,
         expected_output="A list of issues and improvement suggestions.",
        agent=critique_agent
    )

    refinement_task = Task(
        description="""
        Improve the answer based on critique feedback.
        Provide final improved answer.
        """,
        expected_output="Final improved and polished answer.",
        agent=answer_agent
    )

    #crew = Crew(
      #  agents=[ answer_agent, critique_agent],
       # tasks=[answer_task, critique_task, refinement_task],
      #  verbose=True
    #)
    crew = Crew(
        agents=[ answer_agent],
       tasks=[answer_task],
       verbose=True
    )
    result = crew.kickoff()
    memory.add(question, result)

  
    return result.raw if hasattr(result, "raw") else str(result)


""""
    if __name__ == "__main__":
    while True:
        question = input("\nAsk your question (or type 'exit'): ")
        if question.lower() == "exit":
            break

        final_answer = run_pipeline(question)
        print("\nFinal Improved Answer:\n")
        print(final_answer)
"""