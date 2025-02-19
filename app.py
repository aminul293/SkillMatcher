import fitz  # PyMuPDF for PDFs
import docx  # python-docx for Word documents
import streamlit as st

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

if uploaded_resume:
    file_type = uploaded_resume.type

    if file_type == "application/pdf":
        resume_text = extract_text_from_pdf(uploaded_resume)
    elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        resume_text = extract_text_from_docx(uploaded_resume)
    else:  # Handle text files
        resume_text = uploaded_resume.read().decode("utf-8")

    st.text_area("📄 Extracted Resume Content:", resume_text, height=200)
    st.write("📝 Now, let's match your resume with our job listings!")