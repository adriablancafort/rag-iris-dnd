import requests
from langchain.document_loaders.pdf import PyPDFDirectoryLoader, PyPDFLoader


# Function to load documents from a PDF folder
def load_documents(pdf_folder_path: str):
    document_loader = PyPDFDirectoryLoader(pdf_folder_path)
    return document_loader.load()

def load_document(pdf_folder_path: str):
    document_loader = PyPDFLoader(pdf_folder_path)
    return document_loader.load()


def text_from_pdfURL(URL: str):
    pdf_path = "data/Downdloaded/downloaded_data.pdf"
    pdf = open(pdf_path, "wb")
    pdf.write(requests.get(URL).content)
    pdf.close()
    documents = load_document(pdf_path).page_content
    return documents


#text_from_pdfURL("https://orkerhulen.dk/onewebmedia/DnD%205e%20Players%20Handbook%20%28BnW%20OCR%29.pdf")