import streamlit as st
import fitz  # PyMuPDF
from transformers import pipeline

@st.cache_resource
def load_summarizer():
    return pipeline("summarization")

summarizer = load_summarizer()

def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def run():
    st.title("📄 PDF Summarizer")

#tf is this
    if "pdf_text" not in st.session_state:
        st.session_state["pdf_text"] = ""

    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    if uploaded_file is not None:
        with st.spinner("Extracting text..."):
            pdf_text = extract_text_from_pdf(uploaded_file)
            st.success("Text extracted!")

            if len(pdf_text) < 200:
                st.warning("The PDF content is too short to summarize.")
                return

            st.subheader("Original Extracted Text (Preview):")
            st.text_area("PDF Text", pdf_text[:1000], height=200)

            if st.button("Summarize"):
                with st.spinner("Summarizing..."):
                    summary = summarizer(pdf_text, max_length=120, min_length=30, do_sample=False)
                    st.subheader("📋 Summary:")
                    st.write(summary[0]['summary_text'])
