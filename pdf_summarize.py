import requests
import fitz  # PyMuPDF
import os
import pdfplumber
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

LLM_PROVIDER = os.getenv("LLM_PROVIDER")

def download_pdf(url, file_path):
    response = requests.get(url)
    with open(file_path, 'wb') as f:
        f.write(response.content)

def extract_text_from_pdf(file_path, max_pages=3):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for i, page in enumerate(pdf.pages):
            if i >= max_pages:
                break
            text += page.extract_text() or ""
    return text


def call_gemini_api(prompt):
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("models/gemini-1.5-pro")
    response = model.generate_content(prompt)
    return response.text

def summarize_pdf(pdf_url):
    file_path = "temp.pdf"
    download_pdf(pdf_url, file_path)
    text = extract_text_from_pdf(file_path)
    os.remove(file_path)
    prompt = f"Summarize the following research paper content:\n\n{text[:3000]}"

    if LLM_PROVIDER == "gemini":
        summary = call_gemini_api(prompt)
    else:
        summary = "Unsupported LLM provider."
    return summary
