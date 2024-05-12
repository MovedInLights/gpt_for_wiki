import logging
import os

from dotenv import load_dotenv
from flask import Flask
from flask import request

from chat_processor import ChatClient
from prompts import COMPARE_PROMPT, COMPARE_REQUEST
from utils import convert_image_to_base64

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

load_dotenv()
logging.basicConfig(level=logging.DEBUG)


app.logger.setLevel(logging.INFO)
handler = logging.FileHandler('app.log')
app.logger.addHandler(handler)


@app.route('/')
def index():
    app.logger.info('This is an INFO message')
    app.logger.debug('This is a DEBUG message')
    app.logger.warning('This is a WARNING message')
    app.logger.error('This is an ERROR message')
    app.logger.critical('This is a CRITICAL message')
    return 'Hello, World!'


@app.route("/compare_tm_apps")
def compare_tm_apps():
    logging.debug("Application started, logging is configured correctly.")
    token = request.headers.get('Authorization')
    expected_token = 'Bearer ' + os.getenv('API_GPT_TOKEN')

    if token != expected_token:
        return "Invalid token", 401

    clients_tm_app_name = request.args.get('clients_tm_app_name', None)
    tm_app_to_compare = request.args.get('tm_app_to_compare', None)
    image_link_to_compare = request.args.get('image_link_to_compare', None)
    convert_image_to_base64(image_link_to_compare)
    request_text = COMPARE_REQUEST.format(
        clients_tm_app_name=clients_tm_app_name, tm_app_to_compare=tm_app_to_compare
    )

    chat_client = ChatClient()
    result = chat_client.chat_with_gpt(
        prompt_content=COMPARE_PROMPT, request_text=request_text
    )
    return {'result': result}


# nginx сделать
