import os
from PyPDF2 import PdfReader

def extract_text_from_file(file_path):
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text
    except Exception as e:
        print(f"❌ Failed to extract text from {file_path}: {e}")
        return ""

def extract_keywords(text, keywords_list):
    return list({kw for kw in keywords_list if kw.lower() in text.lower()})
