# Retrieval Augmented Generation Assistant

The [Retrieval Augmented Generation Assistant](https://rag-assistant.pages.dev) is an intelligent chatbot that enables users to ask questions about information that was not available in the training dataset of the Large Language Model being used. 

To achieve so, the user just has to introduce any URL (it works both with webpages and PDFs) and Retrieval Augmented Generation Assistant will be able to answer questions about that content:

![Retrieval Augmented Generation Assistant](https://github.com/adriablancafort/retrieval-augmented-generation-assistant-hackupc24/assets/76774853/d735261b-517f-4dd2-b961-de81d9c84e69)

**Note:** This project was developed during the HackUPC 2024. [See it on DevPost](https://devpost.com/software/retrieval-augmented-generation-iris-intersystems)

## Features

- **Specify Data Source Input:** The chatbot includes an input to specify the desired data source. Users can provide the URL of the webpage or PDF they are interested in, and the chatbot will retrieve relevant information from the webpage in real-time.

- **Information Query Input:** The chatbot offers a second input where users can ask questions or request specific information about the loaded webpage or PDF. Users can inquire about any information available in the webpage, such as its title, meta description, keywords, headings, images, links, and more.

## Usage

To use the Webpage Information Chatbot, follow these steps:

1. Provide the URL of the webpage or PDF you want to analyze in the designated input field.
2. Ask questions or request specific information about the webpage or PDF in the chat interface.
3. Receive intelligent responses from the chatbot, which will provide relevant information extracted from the webpage or PDF.

# Retrieval Augmented Generation Assistant API

Welcome to the Retrieval-Augmented Generation Assistant API documentation. This API is designed to provide users with functionalities for retrieving information from URLs and generating responses to user prompts or questions based on the retrieved content.

### Endpoints

#### 1. GET_URL

- **Description**: Fetches content from a given URL (can be html or pdf).
  
- **Method**: `POST`
  
- **Endpoint**: `/get_url`

- **Request Parameters**:
  - `url` (string): The URL from which to retrieve content.

- **Success Responses**:
  - **Code**: `200 OK`
    - **Content**: Null if database was uploaded correctly to InterSystems
    - **Example**:
      The database has been uploaded to the InterSystems website, as indicated in the image provided. 
      ![image](https://github.com/adriablancafort/retrieval-augmented-generation-assistent-hackupc24/assets/132887066/913d99a1-d366-40c7-b6d8-68315a831198)
      Additionally, the API returned null, signifying that the fetched document was found without any issues.
      ![Example Response](https://github.com/adriablancafort/retrieval-augmented-generation-assistent-hackupc24/assets/132887066/6b6e09e8-3a16-468d-902b-7acc14e6a645)

- **Error Responses**:
  - **Code**: `400 Bad Request`
    - **Content**: Raised Error
    - **Example**:
      ![Invalid URL Error](https://github.com/adriablancafort/retrieval-augmented-generation-assistent-hackupc24/assets/132887066/c54a0221-68ce-4f54-88e8-5ca55e479ee2)

#### 2. ASK

- **Description**: Generates a response to a user question based on the content of a specified URL.
  
- **Method**: `POST`
  
- **Endpoint**: `/ask`

- **Request Parameters**:
  - `question` (string): The question posed by the user.

- **Success Responses**:
  - **Code**: `200 OK`
    - **Content**: JSON object containing the generated response. If no awnser valid or found the API will tell you explain what happened in the questions.
    - **Example**:
      ```json
      {
        "response": "The response to the user's question..."
      }
      ```
      ![Example Response](https://github.com/adriablancafort/retrieval-augmented-generation-assistent-hackupc24/assets/132887066/84af8273-60ec-42d6-9293-eaab3e0a8bc8)

### Usage

To use the Retrieval-Augmented Generation Assistant API, make HTTP POST requests to the appropriate endpoints with the required parameters.

### Notes

- Ensure that the URLs provided are accessible and contain valid content.
- The API may return errors for invalid or inaccessible URLs.

# How it works

Retrieval Augmented Generation Assistant consists of two decoupled parts: a frontend interface and backend API, as you can see in the structure of this repository.

## Frontend

The frontend is a simple chat interface built using Svelte.js and Vite.js. It manages the logic of calling the correct API endpoints and a basic state management to show the user a loading spinner icon between a question is submitted and the message with the API response is rendered in the chat interface. It also includes a button to toggle between dark mode and white mode.

## Backend

The backend is built using the Python Framework FastAPI to expose the API endpoints specified before. It also requires an instance of the Iris Vector Database by InterSystems.

- To scrape the webpages or PDFs, we are using Beautiful Soup.
- To split the text into chunks we use RecursiveCharacterTextSplitter by Langchain.
- To generate the embeddings we use the OpenAI text embedings model.
- To store the embedings and perform similarity_search_with_relevance_scores, we use the Iris Vector Database by InterSystems.
- To interact with the user, we use OpenAI gpt-3.5 turbo Large Language Model.
- To Deploy the backend to a VPS we used Docker.
