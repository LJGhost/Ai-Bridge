import streamlit as st
import cohere


co = cohere.Client("YOUR API KEY HERE")



def run():
    st.title("💡 Resume Bullet Point Enhancer")
    st.write("Improve weak resume bullet points with powerful AI rewrites.")

    bullet_input = st.text_area("Paste your bullet point", placeholder="e.g., Worked on a data project")

    if st.button("✨ Enhance Bullet Point"):
        if not bullet_input.strip():
            st.warning("Please enter a bullet point to enhance.")
        else:
            with st.spinner("Enhancing..."):
                prompt = f"Rewrite this resume bullet point to sound more professional, action-oriented, and quantified:\n'{bullet_input}'"

                try:
                    response = co.generate(
                        model='command',
                        prompt="Rewrite this resume bullet point professionally: Worked on a data science project",
                        max_tokens=100,
                        temperature=0.7,
                    )
                    enhanced = response.generations[0].text
                    st.subheader("✅ Enhanced Bullet Point")
                    st.write(enhanced)
                except Exception as e:
                    st.error(f"Something went wrong: {e}")
