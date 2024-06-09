import logging

from dotenv import load_dotenv
from flask import Flask
from flask import request

from chat_processor import ChatClient
from prompts import (
    COMPARE_PROMPT,
    COMPARE_REQUEST,
)
from utils import convert_image_to_base64, compare_tokens

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
    tm_app_to_compare = request.args.get("tm_app_to_compare", None)
    image_link_to_compare = request.args.get("image_link_to_compare", None)
    logging.info(
        f"received request, TM {clients_tm_app_name}, image {image_link_to_compare}"
    )
    convert_image_to_base64(image_link_to_compare)
    request_text = COMPARE_REQUEST.format(
        clients_tm_app_name=clients_tm_app_name, tm_app_to_compare=tm_app_to_compare
    )

    chat_client = ChatClient()
    result = chat_client.chat_with_gpt(
        prompt_content=COMPARE_PROMPT, request_text=request_text
    )
    return {"result": result}


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
