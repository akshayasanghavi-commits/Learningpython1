from crewai import Agent, Task, Crew, LLM
from agents.tools import retrieve_tool
from agents.memory import ConversationMemory
from agents.sql_tool import SQLTool
from agents.web_tool import WebSearchTool

web_tool = WebSearchTool()



sql_tool = SQLTool()

# -------------------------
# 1️⃣ Setup Local LLM via CrewAI Native Wrapper
# -------------------------

local_llm = LLM(
    model="ollama/mistral",
    temperature=0.3
)


# -------------------------
# 2️⃣ Memory
# -------------------------

memory = ConversationMemory()


# -------------------------
# 3️⃣ Agents
# -------------------------

retriever_agent = Agent(
    role="Document Retrieval Specialist",
    goal="Retrieve relevant document context for the question.",
    backstory="Expert in semantic search and vector similarity.",
    tools=[retrieve_tool],
    llm=local_llm,
    verbose=True
)

answer_agent = Agent(
    role="Answer Generator",
    goal="""
You can use:
- Document retrieval tool for PDF questions
- Database Query Tool for structured data
- Web Search Tool for real-time information

Choose the correct tool based on question type.
Answer in short do not explain the answer. If you use a tool, only return the tool output as the answer.
""",
    backstory="Expert at forming structured and clear responses.",
    tools=[retrieve_tool, sql_tool, web_tool],
    llm=local_llm,
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

    previous_context = memory.get_context()

    answer_task = Task(
        description=f"""
        Previous Conversation:
        {previous_context}

        User Question:
        {question}

      You can use:
- Document retrieval tool for PDF questions
- Database Query Tool for structured data
- Web Search Tool for real-time information

Choose the correct tool based on question type.
        """,
        expected_output="A clear, well-structured answer to the user question.",
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

    crew = Crew(
        agents=[retriever_agent, answer_agent, critique_agent],
        tasks=[answer_task, critique_task, refinement_task],
        verbose=True
    )

    result = crew.kickoff()
    memory.add(question, result)

    return result


if __name__ == "__main__":
    while True:
        question = input("\nAsk your question (or type 'exit'): ")
        if question.lower() == "exit":
            break

        final_answer = run_pipeline(question)
        print("\nFinal Improved Answer:\n")
        print(final_answer)