import streamlit as st
import fitz  # PyMuPDF for PDF reading
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
from collections import Counter



#list of all stop words
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))




# Extract text from uploaded PDF
def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text


#keyword extraction
def extract_keywords(text, top_n=20):
    words = [word.lower() for word in text.split() if word.isalpha() and word.lower() not in stop_words]
    freq = Counter(words)
    return set([word for word, _ in freq.most_common(top_n)])



# Get similarity score using TF-IDF + cosine
def get_similarity_score(text1, text2):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([text1, text2])
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return round(similarity * 100, 2)



def run():
    st.title("📄 AI Resume Rating Tool")
    st.write("(Work in Prgress:)")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Job Description")
        job_description = st.text_area("Paste Job Description", height=300)

    with col2:
        st.subheader("Upload Resume")
        uploaded_resume = st.file_uploader("Upload Resume (PDF)", type="pdf")
        resume_text = ""
        if uploaded_resume:
            resume_text = extract_text_from_pdf(uploaded_resume)
            st.success("Resume text extracted!")

    if st.button("🔍 Analyze Resume"):
        if not job_description.strip() or not resume_text.strip():
            st.warning("Please provide both a job description and a resume.")
            return

        score = get_similarity_score(job_description, resume_text)
        st.markdown(f"### ✅ Resume Match Score: `{score}/100`")

        job_keywords = extract_keywords(job_description)
        resume_keywords = extract_keywords(resume_text)
        missing_keywords = job_keywords - resume_keywords


        st.markdown("### ❌ Missing Keywords:")
        if missing_keywords:
            st.write(", ".join(list(missing_keywords)))
        else:
            st.write("Great! No important keywords are missing.")

        st.markdown("### 💡 AI-Powered Suggestions:")
        if missing_keywords:
            st.write("• Consider adding these keywords or related experiences: " + ", ".join(list(missing_keywords)))
        if score < 50:
            st.write("• Your resume has low similarity. Try restructuring to better reflect the job role.")
        elif score < 75:
            st.write("• The match is decent. You could improve it by refining your skills and experience sections.")
        else:
            st.write("• Good match! Minor tweaks could further align your resume.")
