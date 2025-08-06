import streamlit as st
from resume_parser import extract_text
from matcher import (
    extract_resume_skills,
    extract_job_skills,
    compute_match_score,
    generate_cover_letter,
)

st.set_page_config(page_title="Resume Analyzer & Job Matcher", layout="centered")
st.title("Resume Analyzer & Job Matcher (LangChain + Ollama)")

st.markdown("Choose **one method** below for Resume and Job Description: upload a file *or* paste text directly.")

# RESUME input
st.subheader("Resume")
resume_file = st.file_uploader("Upload Resume File (PDF/DOCX/TXT)", type=["pdf", "docx", "txt"], key="resume_file")
resume_text_input = st.text_area("Or Paste Resume Text Here", height=200, key="resume_text")

# JD input
st.subheader("Job Description")
jd_file = st.file_uploader("Upload JD File (PDF/DOCX/TXT)", type=["pdf", "docx", "txt"], key="jd_file")
jd_text_input = st.text_area("Or Paste JD Text Here", height=200, key="jd_text")

# Analyze Button
if st.button("Analyze"):
    if (resume_file or resume_text_input.strip()) and (jd_file or jd_text_input.strip()):
        with st.spinner("Analyzing..."):
            resume_text = (
                extract_text(resume_file) if resume_file else resume_text_input.strip()
            )
            jd_text = (
                extract_text(jd_file) if jd_file else jd_text_input.strip()
            )

            resume_skills = extract_resume_skills(resume_text)
            job_skills = extract_job_skills(jd_text)
            match_score = compute_match_score(resume_skills, job_skills)
            letter = generate_cover_letter(resume_text, jd_text)

        st.success("Analysis Complete")
        st.markdown(f"### Match Score: **{match_score:.2f}%**")

        st.subheader("Extracted Resume Skills")
        st.write(resume_skills)

        st.subheader("Extracted Job Description Skills")
        st.write(job_skills)

        st.subheader(" Tailored Cover Letter")
        st.text_area("Generated Cover Letter", letter, height=300)

    else:
        st.warning("Please upload or paste both resume and job description.")

