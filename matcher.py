from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = Ollama(model="mistral")

resume_prompt = PromptTemplate.from_template("""
Extract a comma-separated list of top relevant technical and soft skills from this resume:

{resume_text}
""")

job_prompt = PromptTemplate.from_template("""
Extract a comma-separated list of skills and technologies required from this job description:

{job_text}
""")

letter_prompt = PromptTemplate.from_template("""
Write a personalized, formal cover letter tailored to the job below using the candidate's resume.

Resume:
{resume_text}

Job Description:
{job_text}
""")

question_prompt = PromptTemplate.from_template("""Given the following resume and job description, generate 5 to 10 
role-specific technical or behavioral interview questions that the candidate should prepare for.

Resume:
{resume_text}

Job Description:
{job_text}
""")


def extract_resume_skills(resume_text):
    chain = LLMChain(llm=llm, prompt=resume_prompt)
    return chain.run(resume_text).strip()


def extract_job_skills(job_text):
    chain = LLMChain(llm=llm, prompt=job_prompt)
    return chain.run(job_text).strip()


def compute_match_score(resume_skills, job_skills):
    resume_set = set(s.strip().lower() for s in resume_skills.split(","))
    job_set = set(s.strip().lower() for s in job_skills.split(","))
    if not job_set:
        return 0.0
    return len(resume_set & job_set) / len(job_set) * 100


def generate_cover_letter(resume_text, job_text):
    chain = LLMChain(llm=llm, prompt=letter_prompt)
    return chain.run({
        "resume_text": resume_text,
        "job_text": job_text
    }).strip()


def generate_interview_questions(resume_text, job_text):
    chain = LLMChain(llm=llm, prompt=question_prompt)
    return chain.run({"resume_text": resume_text, "job_text": job_text})