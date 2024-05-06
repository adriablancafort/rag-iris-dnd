from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
from functions_vector_search import save_database, nearest_vector
from pdf_scrapper import text_from_pdfURL
from web_scrapper import extract_content

# Initialize FastAPI app
app = FastAPI()

# Initialize OpenAI client
client = OpenAI()

# Root endpoint
@app.get("/")
async def root():
    return {"response": "OK"}

# Ask endpoint to get response from OpenAI API
@app.get("/ask/{prompt}")
def ask(prompt: str):
    return {"response": get_response(prompt)}

# Function to get response from OpenAI API
def get_response(prompt: str) -> str:
    """
    Given a prompt, gets the additional information from the vectorial database
    and obtains the answer from the OpenAI API.

    Parameters: String with the query
    Output: A string with the answer to the query 
    """
    # Get context from vector database
    context_list = nearest_vector(prompt, 1) # list of strings; if list length is 0, the text is not talking about the subject
    print(context_list)
    context_string = "--------".join(context_list) 
    if len(context_list) == 0:
        # If no context found, ask OpenAI directly
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": 'Answer the question'},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content + " No additional information was given to answer this question."

    else:
        # If context found, provide context to OpenAI
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": 'Answer questions based only on the following context:'+context_string+'if context does not exist, or you can\'t find the answer, say it'},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content

# Get URL endpoint to extract text content from PDF or web page
@app.get("/get_url/{URL:path}")
def get_url(URL:str) -> None:
    if URL[-3:] == "pdf":
        text = text_from_pdfURL(URL)
    else:
        text = extract_content(URL)
    
    # Save extracted text to database
    save_database(text)
