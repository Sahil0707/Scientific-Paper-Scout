import requests
import xml.etree.ElementTree as ET

def search_papers(query, max_results):
    url = f"http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results={max_results}"
    response = requests.get(url)
    entries = []
    root = ET.fromstring(response.content)
    for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
        title = entry.find('{http://www.w3.org/2005/Atom}title').text.strip()
        pdf_url = entry.find('{http://www.w3.org/2005/Atom}id').text.strip().replace('abs', 'pdf') + ".pdf"
        entries.append({"title": title, "pdf_url": pdf_url})
    return entries
