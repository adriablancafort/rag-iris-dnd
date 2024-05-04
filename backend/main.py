from fastapi import FastAPI
from openai import OpenAI




from langchain_openai import OpenAIEmbeddings

def get_embedding_function():
    embeddings_model = OpenAIEmbeddings(api_key="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")
    return embeddings_model

from langchain.document_loaders.pdf import PyPDFDirectoryLoader

def load_documents(pdf_folder_path: str):
    document_loader = PyPDFDirectoryLoader(pdf_folder_path)
    return document_loader.load()


from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document

def split_document(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 800,
        chunk_overlap=80,
        length_function=len,
        is_separator_regex=False,
    )
    return text_splitter.split_documents(documents)



app = FastAPI()
client = OpenAI()


@app.get("/")
async def root():
    return {"response": "OK"}


@app.get("/ask/{prompt}")
def ask(prompt: str):
    return {"response": get_response(prompt)}


def get_response(prompt: str):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message.content