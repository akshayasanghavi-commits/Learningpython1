# Learningpython1
AgenticResumeTailor 🤖📄

Overview
The AgenticResumeTailor is a sophisticated AI-driven tool designed to bridge the gap between job descriptions and candidate resumes. By utilizing Multi-Agent Orchestration and Retrieval-Augmented Generation (RAG), the system analyzes a candidate's background and intelligently aligns it with specific job requirements.

Core Features

Multi-Agent Orchestration: Utilizes CrewAI to manage specialized agents for job description analysis and resume formatting.


Contextual Grounding (RAG): Employs the CrewAI PDF Search Tool to extract and prioritize facts directly from the source resume.


LLM Integration: Powered by Google Gemini via langchain_google_genai for high-fidelity natural language processing.


Modular Design: Built with Python, allowing for easy integration into wider web services or RESTful APIs.

Technical Stack

Language: Python 


AI Frameworks: CrewAI, LangChain 


Model: Google Gemini Pro 


Data Handling: Pandas, PyPDF 

How It Works

Ingestion: The user provides a PDF resume and a target Job Description.


Retrieval: The RAG tool searches the PDF to ensure no "hallucinations" occur and only actual skills are used.


Analysis: A "Researcher" agent identifies key gaps between the resume and the JD.


Generation: A "Writer" agent generates a tailored resume and cover letter suggestions.
