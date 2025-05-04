import streamlit as st

# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "home"

# Sidebar Navigation Buttons
st.sidebar.title("AI Tools Dashboard")

if st.sidebar.button("AI Text Summariser"):
    st.session_state.page = "ai_summariser"

if st.sidebar.button("PDF Summarizer"):
    st.session_state.page = "pdf_summarizer"

if st.sidebar.button("Resume Analyser"):
    st.session_state.page = "resume_analyser"

if st.sidebar.button("Bullet Enhancer"):
    st.session_state.page = "Bullet Enhancer"


# Load Selected Page
if st.session_state.page == "ai_summariser":
    import ai_summariser
    ai_summariser.run()

elif st.session_state.page == "pdf_summarizer":
    import pdf_summarizer
    pdf_summarizer.run()

elif st.session_state.page == "resume_analyser":
    import resume_analyser
    resume_analyser.run()

elif st.session_state.page == "Bullet Enhancer":
    import clg
    clg.run()

else:
    st.title("Welcome to the AI Tools Dashboard")
    st.write("Please select a tool from the sidebar.")
