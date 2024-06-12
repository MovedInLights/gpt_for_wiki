import base64
import logging
import os
from enum import Enum
from typing import Dict, Any

import requests

from prompts import (
    CONCLUSION_PROMPT,
    RUPTO_TOOLKIT_TEXT,
    COMPARE_PROMPT,
    COMPARE_REQUEST,
)


# def convert_string_to_json(data_to_convert: str) -> Union[Dict[str, Any], List[Any]]:
#     try:
#         data_for_chat = json.loads(data_to_convert)
#     except json.JSONDecodeError as e:
#         logging.warning(f'Error parsing JSON: {e}')
#         data_for_chat = []
#     return data_for_chat


class Role(str, Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"


def convert_url_image_to_base64(image_url) -> str | None:
    try:
        response = requests.get(image_url)
        response.raise_for_status()
        image_data = response.content
        decoded_image = base64.b64encode(image_data).decode("utf-8")
        return decoded_image
    except Exception as e:
        logging.warning(f"Error converting image to base64: {e}")
        return None


def get_image_gpt_dict(base64_img: str | None) -> Dict[str, str]:
    return {"url": f"data:image/jpeg;base64,{base64_img}"}


def encode_image(image_path) -> str:
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def compare_tokens(token: str) -> bool:
    api_token = os.getenv("API_GPT_TOKEN")
    if not token or api_token is None or token != "Bearer " + api_token:
        return False
    return True


def generate_conclusion_message_draft(
    clients_tm_app_name: str, image_link_to_compare: str
) -> list[Dict[str, Any]]:
    return [
        {
            'role': 'system',
            'type': 'text',
            'body': CONCLUSION_PROMPT.format(RUPTO_TOOLKIT_TEXT=RUPTO_TOOLKIT_TEXT),
        },
        {
            "role": "user",
            "type": "text",
            "body": clients_tm_app_name,
        },
        {
            "role": "user",
            "type": "image_url",
            "body": image_link_to_compare,
        },
    ]


def generate_compare_message_draft(
    clients_tm_app_name: str, registered_tm: str
) -> list[Dict[str, Any]]:
    return [
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
