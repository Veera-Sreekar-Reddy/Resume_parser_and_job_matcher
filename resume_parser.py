import fitz  # PyMuPDF
from io import BytesIO
import docx2txt


def extract_text(uploaded_file):
    filename = uploaded_file.name.lower()

    try:
        if filename.endswith(".pdf"):
            return extract_text_from_pdf(uploaded_file)
        elif filename.endswith(".docx"):
            return extract_text_from_docx(uploaded_file)
        elif filename.endswith(".txt"):
            return uploaded_file.read().decode("utf-8")
        else:
            return "Unsupported file format."
    except Exception as e:
        print(f" Error extracting text: {e}")
        return "Error extracting text from file."


def extract_text_from_pdf(uploaded_file):
    file_bytes = BytesIO(uploaded_file.read())
    doc = fitz.open(stream=file_bytes, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def extract_text_from_docx(uploaded_file):
    file_bytes = BytesIO(uploaded_file.read())
    return docx2txt.process(file_bytes)
