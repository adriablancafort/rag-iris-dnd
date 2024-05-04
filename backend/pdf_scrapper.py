import requests
from langchain.document_loaders.pdf import PyPDFDirectoryLoader

def load_documents(pdf_folder_path: str):
    document_loader = PyPDFDirectoryLoader(pdf_folder_path)
    return document_loader.load()
# Function to load PDF

def text_from_pdfURL(URL: str):
    response = requests.get(URL)
    pdf_path = "data/Downloaded"
    pdf = open(pdf_path + "/downloaded_data.pdf", "wb")
    pdf.write(response.content)
    pdf.close()
    document = load_documents(pdf_path)
    return document


text_from_pdfURL("https://orkerhulen.dk/onewebmedia/DnD%205e%20Players%20Handbook%20%28BnW%20OCR%29.pdf")
