import os
from dotenv import load_dotenv
from paper_search import search_papers
from pdf_summarize import summarize_pdf

load_dotenv()

def process_command(command, args):
    if command == "search":
        query = args[0]
        max_results = int(args[1])
        results = search_papers(query, max_results)
        return results

    elif command == "summarize":
        pdf_url = args[0]
        summary = summarize_pdf(pdf_url)
        return summary

    else:
        return "Unknown command. Use 'search' or 'summarize'."
