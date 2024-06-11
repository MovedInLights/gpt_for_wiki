import logging

from dotenv import load_dotenv
from flask import Flask
from flask import request

from chat_processor import ChatClient
from prompts import (
    COMPARE_PROMPT,
    COMPARE_REQUEST,
)
from utils import compare_tokens

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

load_dotenv()
logging.basicConfig(level=logging.DEBUG)

app.logger.setLevel(logging.INFO)
handler = logging.FileHandler("app.log")
app.logger.addHandler(handler)


@app.route("/compare_tm_apps")
def compare_tm_apps():
    logging.debug("Application started, logging is configured correctly.")
    is_token_correct = compare_tokens(request.headers.get("Authorization"))
    if not is_token_correct:
        return "Invalid token", 401

    clients_tm_app_name = request.args.get("clients_tm_app_name", None)
    registered_tm = request.args.get("tm_app_to_compare", None)
    logging.info(
        f"received request, TM {clients_tm_app_name}, registered_tm {registered_tm}"
    )

    chat_client = ChatClient()
    messages = chat_client.compile_messages(
        messages_draft=[
            {
                'role': 'system',
                'type': 'text',
                'body': COMPARE_PROMPT,
            },
            {
                'role': 'user',
                'type': 'text',
                'body': COMPARE_REQUEST.format(
                    clients_tm_app_name=clients_tm_app_name,
                    registered_tm=registered_tm,
                ),
            },
        ]
    )
    logging.info(f'Received messages for GPT {messages}')

    chat_response = chat_client.chat_with_gpt(
        model="gpt-4o",
        temperature=0,
        messages=messages,
    )
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
        messages_draft=[
            {
                "name": clients_tm_app_name,
                "type": "text",
            },
            {
                "name": image_link_to_compare,
                "type": "image_url",
            },
        ]
    )
    chat_response = chat_client.chat_with_gpt(
        model="gpt-4o",
        temperature=0,
        messages=messages,
    )
    return {"result": chat_response}
