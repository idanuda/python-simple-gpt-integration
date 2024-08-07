from flask import make_response, Blueprint, request
from langchain_community.tools.tavily_search import TavilySearchResults
from tavily import TavilyClient
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from pinecone import Pinecone


import requests


openai_controller = Blueprint('openai_controller', __name__, template_folder='templates')
ENDPOINT = "YOUR-ENDPOINT"
API_KEY = "YOU-API-KEY"

@openai_controller.route('/api/v0/openai/gpt-4', methods=(['POST']))
def gpt_chat():

    # Configuration

    headers = {
        "Content-Type": "application/json",
        "api-key": API_KEY,
    }
    prompt = request.get_json().get('prompt')
    # Payload for the request
    payload = {
        "messages": [
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "You are an AI assistant that helps people find information."
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            },
            {
                "role": "assistant",
                "content": [
                    {
                        "type": "text",
                        "text": "Hello! How can I assist you today?"
                    }
                ]
            }
        ],
        "temperature": 0.7,
        "top_p": 0.95,
        "max_tokens": 800
    }



    # Send request
    try:
        response = requests.post(ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
    except requests.RequestException as e:
        print(e)
        raise SystemExit(f"Failed to make the request. Error: {e}")


    # Handle the response as needed (e.g., print or process)
    print(response.json())
    return make_response(
        response.json(),
        200
    )

@openai_controller.route('/api/v0/langchain', methods=(['GET']))
def lang_chain_simple_example():

    llm = ChatOpenAI(api_key="")

    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "You are a world class technical documentation writer."),
        ("user", "{input}")
    ])

    output_parser = StrOutputParser()

    chain = prompt_template | llm | output_parser

    request_question = request.get_json().get('request_question')

    gpt_response = chain.invoke({"input": request_question})

    return make_response(
        {'gpt_response': gpt_response},
        200
    )
