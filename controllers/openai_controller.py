from flask import make_response, Blueprint, request
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from services.openai_service import send_request_to_gpt

openai_controller = Blueprint('openai_controller', __name__, template_folder='templates')
ENDPOINT = "YOUR-ENDPOINT"
API_KEY = "YOUR-API-KEY"


@openai_controller.route('/api/v0/openai/gpt-4', methods=(['POST']))
def gpt_chat():
    response = send_request_to_gpt(request.get_json().get('prompt'))
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
