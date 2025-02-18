import streamlit as st

st.title("🔍 SkillMatcher – AI-Powered Resume Matching")

uploaded_resume = st.file_uploader("Upload your resume (PDF/Text)", type=["pdf", "txt"])

if uploaded_resume:
    st.success("Resume uploaded successfully!")
    resume_text = uploaded_resume.read().decode("utf-8")  # Convert file to text
    st.text_area("📄 Extracted Resume Content:", resume_text, height=200)

st.subheader("🔗 Paste Job Description Below:")
job_description = st.text_area("Job Description:")

if st.button("Match Resume to Job"):
    st.success("Matching in progress... (AI feature coming soon!)")

