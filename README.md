# 📚 Scientific Paper Scout

A command-line AI assistant for summarizing scientific papers (PDFs) using Google's Gemini API.  
It automatically downloads a PDF from a given URL, extracts the text from the first 3 pages, and generates a concise summary.

---

## 📌 Features

- 📥 Download scientific papers from public URLs (like arXiv)
- 📄 Extract text content from the first **3 pages** of the PDF
- 🤖 Summarize the extracted text using **Google Gemini 1.5 Pro API**
- 🖥️ Command-line interface for quick and simple usage

---

## 📦 Dependencies

- `pdfplumber`  
- `requests`  
- `google-generativeai`  

## 🛠 Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Sahil0707/Scientific-Paper-Scout.git
   cd solar-ai-assistant
2. Create a virtual environment and activate it:
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # Mac/Linux
   .venv\Scripts\activate     # Windows
3. Install Dependencies:
   ```sh
   pip install -r requirements.txt
4. Set up your .env file(create a .env file and add your api key):
   ```sh
   GEMINI_API_KEY=your_gemini_api_key
5. Run the application
   ```sh
   python main.py

---
