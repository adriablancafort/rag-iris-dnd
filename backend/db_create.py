import os

# Importing necessary modules from langchain and langchain_openai
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
from langchain_iris import IRISVector
from scrapper import load_documents
# Function to initialize and return the embeddings model
def get_embedding_function():
    embeddings_model = OpenAIEmbeddings(api_key="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")
    return embeddings_model

# Function to split the loaded documents into chunks
def split_documents(documents):
    # Initializing a RecursiveCharacterTextSplitter with specified parameters
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 400,
        chunk_overlap=80,
        length_function=len,
        is_separator_regex=False,
    )
    # Splitting documents into chunks
    return text_splitter.split_documents(documents)


# Function to create a database
def add_info_to_db(db_name: str, path_string:str):
    # Loading documents from the specified folder
    documents = load_documents(path_string)
    # Splitting loaded documents into chunks
    chunks = split_documents(documents)

    # Database connection parameters
    username = 'demo'
    password = 'demo' 
    hostname = os.getenv('IRIS_HOSTNAME', 'localhost')
    port = '1972' 
    namespace = 'USER'
    CONNECTION_STRING = f"iris://{username}:{password}@{hostname}:{port}/{namespace}"

    # Name for the collection in the database
    COLLECTION_NAME = db_name

    db = IRISVector.from_documents(
        embedding=get_embedding_function(),
        documents=chunks,
        collection_name=COLLECTION_NAME,
        connection_string=CONNECTION_STRING,
    )


# Function to create a database
def fetch_db(db_name: str):
    # Database connection parameters
    username = 'demo'
    password = 'demo' 
    hostname = os.getenv('IRIS_HOSTNAME', 'localhost')
    port = '1972' 
    namespace = 'USER'
    CONNECTION_STRING = f"iris://{username}:{password}@{hostname}:{port}/{namespace}"

    # Name for the collection in the database
    COLLECTION_NAME = db_name

    db = IRISVector(
        embedding_function=get_embedding_function(),
        dimension=1536,
        collection_name=COLLECTION_NAME,
        connection_string=CONNECTION_STRING,
    ) 

    return db


def get_context_query(query:str, db_name: str):
    db = fetch_db(db_name)
    result = db.similarity_search(query, k=4)
    return [doc.page_content for doc in  result]

