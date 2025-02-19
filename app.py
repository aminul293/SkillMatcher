import fitz  # PyMuPDF for PDFs
import docx  # python-docx for Word documents
import streamlit as st
import openai  # OpenAI API for job matching

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")  # Replace with your OpenAI key

st.title("🔍 SkillMatcher – AI-Powered Resume Matching")

uploaded_resume = st.file_uploader("Upload your resume (PDF, DOCX, or TXT)", type=["pdf", "docx", "txt"])

def extract_text_from_pdf(uploaded_file):
    """Extract text from a PDF file."""
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        text = "\n".join(page.get_text() for page in doc)
    return text

def extract_text_from_docx(uploaded_file):
    """Extract text from a Word (DOCX) file."""
    doc = docx.Document(uploaded_file)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

# Resume text extraction
resume_text = ""
if uploaded_resume:
    file_type = uploaded_resume.type

    if file_type == "application/pdf":
        resume_text = extract_text_from_pdf(uploaded_resume)
    elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        resume_text = extract_text_from_docx(uploaded_resume)
    else:  # Handle text files
        resume_text = uploaded_resume.read().decode("utf-8")

    st.text_area("📄 Extracted Resume Content:", resume_text, height=200)

# Job description input
st.subheader("🔗 Paste Job Description Below:")
job_description = st.text_area("Job Description:")

def match_resume_to_job(resume_text, job_description):
    """AI-based resume-job matching"""
    prompt = f"""
    Compare the following resume with the job description and provide:
    - A match score (0-100%).
    - Key strengths of the resume for this job.
    - Areas of improvement to increase the match.
    
    Resume:\n{resume_text}\n\nJob Description:\n{job_description}
    """

    response = openai.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]

# Button to trigger AI matching
if job_description:
    if st.button("🔍 Match Resume to Job"):
        st.success("Matching in progress...")
        match_result = match_resume_to_job(resume_text, job_description)
        st.subheader("🎯 AI Match Score & Insights")
        st.write(match_result)
