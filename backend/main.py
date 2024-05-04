from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
from db_create import get_context_query
from pdf_scrapper import text_from_pdfURL
from web_scrapper import extract_content

app = FastAPI()
client = OpenAI(api_key="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")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"response": "OK"}


@app.get("/ask/{prompt}")
def ask(prompt: str):
    return {"response": get_response(prompt)}

def get_response(prompt: str):
    db_name='Monopoly'
    context_list = get_context_query(prompt, db_name)
    context_string = "\n".join(context_list) 
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": 'Answer questions based only on the following context:'+context_string},
            {"role": "user", "content": prompt}
        ]
    )

    return completion.choices[0].message.content


@app.get("/get_url/{URL}")
def get_url(URL:str) -> None:
    text: str = ""
    if URL[-3:] == "pdf":
        text = text_from_pdfURL(URL)
    else:
        text = extract_content(URL)


    #preprocess del text


