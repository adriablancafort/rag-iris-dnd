# User guide

The Webpage Information Chatbot is an intelligent assistant designed to provide users with information about a specific webpage through natural language interaction. This chatbot serves as a convenient tool for users who want to quickly gather insights about a webpage without manually navigating through its content.

![image](https://github.com/adriablancafort/retrieval-augmented-generation-assistent-hackupc24/assets/75630316/4fff409a-c5eb-4273-b5b9-ec7b6e0f9321)



## Features

- **Webpage Data Loading Placeholder:** The chatbot includes a placeholder for loading data from a webpage. Users can provide the URL of the webpage they are interested in, and the chatbot will retrieve relevant information from the webpage in real-time.
  
- **Information Query Placeholder:** The chatbot offers a second placeholder where users can ask questions or request specific information about the loaded webpage. Users can inquire about various aspects of the webpage, such as its title, meta description, keywords, headings, images, links, and more.

## Usage

To use the Webpage Information Chatbot, follow these steps:

1. Provide the URL of the webpage you want to analyze in the designated input field.
2. Ask questions or request specific information about the webpage in the chat interface.
3. Receive intelligent responses from the chatbot, which will provide relevant information extracted from the webpage.


# Retrieval-Augmented Generation Assistant API

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
