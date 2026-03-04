import streamlit as st
from agents.crew_setup import run_pipeline

st.title("RAG AI Assistant")

user_input = st.text_input("Ask a question:")

if st.button("Submit"):
    if user_input:
        result = run_pipeline(user_input)
        st.write("### Answer:")
        st.write(result)