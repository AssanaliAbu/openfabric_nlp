"""
Wikipedia Question Answering Module

This module uses the `wikipediaapi` library and the Hugging Face `transformers`
library to perform question answering with information extracted from Wikipedia.

Functions:
    get_wikipedia_page_content(page_title: str) -> str:
        Retrieves the content of a Wikipedia page given its title.

    search_wikipedia(query: str) -> str:
        Searches for a Wikipedia page that matches the query and returns its content.

    get_response(query: str) -> str:
        Generates an answer to a question by searching Wikipedia and running a
        question-answering model on the result.

Dependencies:
    wikipediaapi: Library to access and parse data from Wikipedia.
    transformers: Library by Hugging Face for state-of-the-art machine learning models.
    requests: Library for making HTTP requests in Python.
    json: Library for JSON manipulation in Python.

Model:
    The script uses the `deepset/tinyroberta-squad2` model for question answering.
    It is a small and fast version of RoBERTa trained on the SQuAD2.0 dataset.

Usage:
    The `get_response` function is the main entry point for using this module.
    Provide a question as a string, and the function will return an answer
    using Wikipedia content as the context.

Example:
    answer = get_response("What is the capital of France?")
    print(answer)

Note:
    The Wikimedia API requires a user agent for requests, which should be replaced
    with our own user information. The number of results is currently set to 1,
    meaning it will only return the top search result from Wikipedia.
"""

import wikipediaapi
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
import requests
import json

# Initialize the question-answering pipeline with the specified model
model_name = "deepset/tinyroberta-squad2"
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
language_code = 'en'


base_url = 'https://api.wikimedia.org/core/v1/wikipedia/'
endpoint = '/search/page'
number_of_results = 1
headers = {
  'User-Agent': 'assanali_abu'
}


def get_wikipedia_page_content(page_title):
    url = f"https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&titles={page_title}&exlimit=1&explaintext"
    response = requests.get(url)
    data = response.json()
    page_id = next(iter(data['query']['pages']))
    return data['query']['pages'][page_id]['extract']


def search_wikipedia(query):
    url = base_url + language_code + endpoint
    parameters = {'q': query, 'limit': number_of_results}
    response = requests.get(url, headers=headers, params=parameters)

    response = json.loads(response.text)

    for page in response['pages']:
      display_title = page['title']
      print(display_title)
      article_url = 'https://' + language_code + '.wikipedia.org/wiki/' + page['key']
      article_description = page['description']

    content = get_wikipedia_page_content(display_title)
    return content


def get_response(query):
    context = search_wikipedia(query)

    QA_input = {
        'question': query,
        'context': context
    }
    res = nlp(QA_input)['answer']

    return res
