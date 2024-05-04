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
    try:
        response = requests.get(URL)
        pdf_path = "data/Downloaded/downloaded_data.pdf"
        if response.status_code != 200:
            return "error" + f"bad status code: {response.status_code}"
        pdf = open(pdf_path, "wb")
        pdf.write(response.content)
        pdf.close()
        documents = load_document(pdf_path).page_content
        return documents
    except:
        return "ERROR"

