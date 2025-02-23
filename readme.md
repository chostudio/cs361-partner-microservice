Web3 chatbot Flask Groq API Microservice

Overview

This microservice provides a REST API endpoint to send a question to the Groq AI platform and receive a response.

How to Request Data from the Microservice

To request data, send a POST request to the /ask endpoint with a JSON payload containing a question field.

Example Request (Python)

import requests

url = "http://127.0.0.1:5000/ask"
headers = {"Content-Type": "application/json"}
data = {"question": "Explain the importance of blockchain"}

response = requests.post(url, json=data, headers=headers)
print(response.json())  # Output the response from the API

Example Request (cURL)

curl -X POST "http://127.0.0.1:5000/ask" \
     -H "Content-Type: application/json" \
     -d '{"question": "Explain the importance of fast language models"}'

How to Receive Data from the Microservice

The microservice returns a JSON response containing the AI-generated answer.

Example Response

{
    "response": "Fast language models are important because they enable real-time applications, improve user experience, reduce latency, and enhance scalability."
}

If the request is missing the question field, the API will return an error:

{
    "error": "Question is required"
}

UML Sequence Diagram

Below is a UML sequence diagram describing the interaction between the client and the Flask microservice.

     +------------+        +----------------+        +----------+
     |  Client    |        | Flask API      |        | Groq API |
     +------------+        +----------------+        +----------+
           |                      |                      |
           | 1. POST /ask         |                      |
           | -------------------> |                      |
           |                      |                      |
           |                      | 2. Send request to Groq API
           |                      | --------------------> |
           |                      |                      |
           |                      | 3. Receive AI response
           |                      | <-------------------- |
           |                      |                      |
           | 4. Return JSON response
           | <------------------  |
           |                      |                      |
           | 5. Display response  |                      |
           |                      |                      |
     +------------+        +----------------+        +----------+

Setup Instructions

1. Install Dependencies

pip install flask groq requests

2. Run the Flask Server

python app.py

This starts the server at http://127.0.0.1:5000.

3. Send a Request

Use one of the example requests above to test the API.

Notes

The Groq API key must be configured in your environment.

The model parameter used is llama-3.3-70b-versatile, but this can be changed as needed.

To use a virtual env you can use this command to activate it on mac:
source .venv/bin/activate

make sure to have a .env file with GROQ_API_KEY
