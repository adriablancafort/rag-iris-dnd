from langchain_openai import OpenAIEmbeddings
from langchain_iris import IRISVector
import os

def get_embedding_function():
    """
    Initialize and return the OpenAI embeddings model.
    """
    embeddings_model = OpenAIEmbeddings(api_key="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")
    return embeddings_model


username, password = 'demo', 'demo'
hostname = os.getenv('IRIS_HOSTNAME', 'localhost')
port, namespace = '1972', 'USER'
CONNECTION_STRING = f"iris://{username}:{password}@{hostname}:{port}/{namespace}"



# Initialize IRISVector instance
db = IRISVector(
    embedding_function=get_embedding_function(),
    dimension=1536,
    connection_string=CONNECTION_STRING,
)
db.delete_collection()