from flask import Flask
from flask import request

from chat_processor import ChatClient
from prompts import COMPARE_PROMPT, COMPARE_REQUEST

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route("/compare_tm_apps")
def compare_tm_apps():
    clients_tm_app_name = request.args.get('clients_tm_app_name', None)
    tm_app_to_compare = request.args.get('tm_app_to_compare', None)
    print(f"Received names: {clients_tm_app_name}, {tm_app_to_compare}")
    request_text = COMPARE_REQUEST.format(
        clients_tm_app_name=clients_tm_app_name, tm_app_to_compare=tm_app_to_compare
    )

    chat_client = ChatClient()
    result = chat_client.chat_with_gpt(
        prompt_content=COMPARE_PROMPT, request_text=request_text
    )
    return {'result': result}


# docker
# ngnix
# gunicorn
# pre-commit
# cd/ci
