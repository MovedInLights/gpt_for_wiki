import json
import logging

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request

from chat_processor import ChatClient
from linkmark_client.linkmark_workflow import (
    SearchType,
    WordSearch,
    CompanySearch,
    NumberSearch,
)
from utils import (
    compare_tokens,
    generate_conclusion_message_draft,
    generate_compare_message_draft,
    generate_description_message_draft,
)

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
CORS(
    app,
    resources={
        r"/tm_search": {
            "origins": "*",
            "allow_headers": ["Authorization", "Content-Type"],
        }
    },
)

load_dotenv()
logging.basicConfig(level=logging.DEBUG)

app.logger.setLevel(logging.INFO)
handler = logging.FileHandler("app.log")
app.logger.addHandler(handler)


@app.route("/compare_tm_apps")
def compare_tm_apps():
    logging.debug('Application started, logging is configured correctly.')
    is_token_correct = compare_tokens(request.headers.get('Authorization'))
    if not is_token_correct:
        return "Invalid token", 401

    clients_tm_app_name = request.args.get('clients_tm_app_name', None)
    registered_tm = request.args.get('tm_app_to_compare', None)
    logging.info(
        f'received request, TM {clients_tm_app_name}, registered_tm {registered_tm}'
    )

    chat_client = ChatClient()
    messages = chat_client.compile_messages(
        messages_draft=generate_compare_message_draft(
            clients_tm_app_name=clients_tm_app_name, registered_tm=registered_tm
        )
    )
    logging.info(f'Received messages for GPT {messages}')

    chat_response = chat_client.chat_with_gpt(
        model="gpt-4o",
        temperature=0,
        messages=messages,
    )
    logging.info(f'Received response for GPT {chat_response}')
    return {"result": chat_response}


@app.route("/gpt_conclusion")
def gpt_conclusion():
    is_token_correct = compare_tokens(request.headers.get("Authorization"))
    if not is_token_correct:
        return "Invalid token", 401

    clients_tm_app_name = request.args.get("clients_tm_app_name", None)
    image_link_to_compare = request.args.get("image_link_to_compare", None)

    chat_client = ChatClient()
    messages = chat_client.compile_messages(
        messages_draft=generate_conclusion_message_draft(
            clients_tm_app_name=clients_tm_app_name,
            image_link_to_compare=image_link_to_compare,
        )
    )
    logging.info(f'Received messages for GPT {messages}')
    chat_response = chat_client.chat_with_gpt(
        model="gpt-4o",
        temperature=0,
        messages=messages,
    )
    return {"result": chat_response}


@app.route("/tm_search", methods=['POST'])
@cross_origin()
def tm_search():
    if request.method != 'POST':
        return "Method not allowed", 405
    logging.info(f'received request, TM {request}')
    is_token_correct = compare_tokens(request.headers.get("Authorization"))
    if not is_token_correct:
        return "Invalid token", 401

    search_type = request.args.get('search_type', None)
    tm_name = request.args.get('tm_name', None)
    classes_for_search = request.args.getlist('classes_for_search')

    search_type_class = get_search_type(
        search_type=search_type, tm_name=tm_name, classes_for_search=classes_for_search
    )
    logging.info(f'Received search type {search_type_class}')
    linkmark_response = search_type_class.make_request()
    logging.info(
        f'Search type is {search_type}, '
        f'tm_name is {tm_name}, '
        f'classes_for_search are {classes_for_search}, '
        f'linkmark_response is {linkmark_response.text}'
    )
    return search_type_class.handle_response(linkmark_response)


@app.route('/gpt_description', methods=['POST'])
def gpt_description():
    logging.info(f'Received request: {request}')
    logging.info(f'Request method: {request.method}')
    logging.info(f'Request headers: {request.headers}')
    logging.info(f'Request URL: {request.url}')
    logging.info(f'Request content type: {request.content_type}')
    logging.info(f'Request data: {request.get_data()}')

    is_token_correct = compare_tokens(request.headers.get("Authorization"))
    if not is_token_correct:
        return "Invalid token", 401
    logo_link = request.args.get('logo_link', None)
    tm_type = request.args.get('tm_type', None)
    logging.info(f'Received request, TM {tm_type}, logo_link is {logo_link}')

    chat_client = ChatClient()
    messages = chat_client.compile_messages(
        messages_draft=generate_description_message_draft(
            tm_type=tm_type,
            logo_link=logo_link,
        )
    )
    logging.info(f'Compiled messages for GPT: {messages}')
    chat_response = chat_client.chat_with_gpt(
        model="gpt-4o",
        temperature=0,
        messages=messages,
    )
    try:
        chat_response_dict = json.loads(chat_response)
        result = chat_response_dict.get('result', chat_response)
    except json.JSONDecodeError:
        result = chat_response

    logging.info(f'ChatGPT response: {result}')
    return {"result": result}


def get_search_type(search_type, tm_name, classes_for_search):
    logging.info(f'Called with: {search_type}, {tm_name}, {classes_for_search}')
    if search_type == SearchType.WORD:
        return WordSearch(
            search_type=search_type,
            tm_name=tm_name,
            classes_for_search=classes_for_search,
        )
    elif search_type == SearchType.COMPANY:
        return CompanySearch(
            search_type=search_type,
            tm_name=tm_name,
            classes_for_search=classes_for_search,
        )
    elif search_type == SearchType.NUMBER:
        return NumberSearch(
            search_type=search_type,
            tm_name=tm_name,
            classes_for_search=classes_for_search,
        )
    else:
        logging.error(f'Unknown search type {search_type}')
        return None
