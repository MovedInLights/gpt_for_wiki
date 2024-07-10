import logging

from dotenv import load_dotenv
from flask import Flask
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
)

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

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
def tm_search():
    if request.method != 'POST':
        return "Method not allowed", 405
    logging.info(f'received request, TM {request}')

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
        f'linkmark_response is {linkmark_response}'
    )
    return search_type_class.handle_response(linkmark_response)


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
