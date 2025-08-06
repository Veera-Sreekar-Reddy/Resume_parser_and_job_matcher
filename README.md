# LangChain Resume Analyzer & Job Matcher

A Streamlit-based web application that analyzes resumes against job descriptions using **LangChain**, **local LLMs (via Ollama)**, and **PDF/TXT parsing**. It extracts key skills, computes a match score, generates a personalized cover letter, and suggests potential interview questions.

---

## Features

- Upload **Resume (PDF)** and **Job Description (PDF/TXT)**
- Extracts skills from both using a **local LLM**
- Computes a **match percentage** between resume and JD
- Generates a **tailored cover letter**
- Suggests **interview questions** based on resume and JD (optional extension)

---

## Tech Stack

- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [Ollama](https://ollama.com/) (for local LLM like `mistral`)
- [PyMuPDF](https://pymupdf.readthedocs.io/) for PDF parsing

---

## Setup Instructions

### 1. Clone the Repository

### 2. Install Dependencies

- pip install -r requirements.txt

### 3. Install and OLLAMA

- brew install ollama (install ollama)
- ollama serve
- ollama run mistral

### 4. Run streamlit in another terminal

- streamlit run app.py
