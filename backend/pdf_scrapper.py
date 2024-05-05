import requests
from langchain.document_loaders.pdf import PyPDFDirectoryLoader

def load_documents(pdf_folder_path: str):
    """
    Loads the document of the given path and returns the Document of itself
    """
    document_loader = PyPDFDirectoryLoader(pdf_folder_path)
    return document_loader.load()
# Function to load PDF

def text_from_pdfURL(URL: str):
    """
    Given a URL gets the PDF files from that url, stores it in pdf_path,
    fetches the text in the pdf and converts it into Document.
    """
    response = requests.get(URL)
    pdf_path = "data"
    pdf = open(pdf_path + "/downloaded_data.pdf", "wb")
    pdf.write(response.content)
    pdf.close()
    document = load_documents(pdf_path)
    return document
