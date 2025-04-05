import streamlit as st
from transformers import pipeline

# Load summarizer model once
@st.cache_resource
def load_summarizer():
    return pipeline("summarization")

def run():
    summarizer = load_summarizer()

    # Streamlit UI
    st.title("🧠 AI Text Summarizer")
    st.write("Paste any long text below and get a short summary using NLP!")

    text_input = st.text_area("Enter your long text here", height=300)

    if st.button("Summarize"):
        if not text_input.strip():
            st.warning("Please enter some text to summarize.")
        else:
            with st.spinner("Summarizing..."):
                summary = summarizer(text_input, max_length=500, min_length=100, do_sample=False)
                st.success("Done!")
                st.subheader("📄 Summary:")
                st.write(summary[0]['summary_text'])

    st.markdown("---")
    st.caption("Built with 🤗 Hugging Face and Streamlit")
