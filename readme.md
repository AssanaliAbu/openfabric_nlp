# Cognitive Assistant

Welcome to the Cognitive Assistant application, an AI-driven chatbot focusing on science-related questions. This application utilizes advanced Natural Language Processing (NLP) models to answer queries, built on the OpenFabric SDK.

## Overview

Cognitive Assistant is designed to handle complex science-related queries using NLP techniques. It is structured with various components that work together to process and respond to user inputs.

### Wikipedia Integration

The application leverages the Wikipedia-API to fetch relevant information as context for the NLP model. This allows the chatbot to provide informed and accurate answers to user queries based on up-to-date Wikipedia content.

#### How it Works

- When a query is received, the application first searches Wikipedia for relevant articles or information.
- The Wikipedia-API is used to fetch extracts or summaries of these articles.
- This content is then passed as context to the NLP model, which processes the information to generate a response.

#### Configuration and Usage

- The Wikipedia-API integration is configured in the `nlp.py` file.
- Users can modify the search parameters or the method of fetching data from Wikipedia as needed.
- The application is set up to handle requests in English, but this can be configured for other languages supported by Wikipedia.


#### Example

**Query:**

```json
{
  "text": [
    "What is the theory of relativity?"
  ]
}
```

**Response:**

```json
{
  "text": [
    "Space–time structure from a dynamical perspective"
  ]
}
```
## Key Components

- `main.py`: Core application logic, including the request processing function.
- `nlp.py`: Handles interactions with the NLP model.
- `ignite.py`: Script to initialize and start the application.
- `start.sh`: Shell script to execute `ignite.py`.
- `Dockerfile`: Defines the Docker environment, including all dependencies.

## Setup and Installation

### Prerequisites

- Docker must be installed on your system.
- Ensure you have an internet connection for pulling base images and dependencies.

### Build the Docker Image

Navigate to the directory containing the `Dockerfile`, then build the image:

```bash
docker build -t cognitive-assistant .
```
### Run the Docker Container
After the image is built, run the container by mapping the container's port 5500 to the host's port 5500:

```bash
docker run -p 5500:5500 cognitive-assistant
```
The application should now be running and ready to process requests.

## Interacting with the Application
Once the container is up, the application will be listening for requests. Interaction with the application will depend on how the request and response handling is implemented in main.py.

## Model and Processing
The application leverages the deepset/tinyroberta-squad2 model from the Hugging Face transformers library for question answering. The implementation details are in nlp.py, and the request processing logic is in the execute function of main.py.



