import base64
import logging
import os
from enum import Enum
from typing import Dict, Any

import requests

from gpt_prompts.prompts import (
    CONCLUSION_PROMPT,
    RUPTO_TOOLKIT_TEXT,
    COMPARE_PROMPT,
    COMPARE_REQUEST,
    DESCRIPTION_PROMPT,
    DESCRIPTION_REQUEST,
)


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
            'role': Role.SYSTEM,
            'type': 'text',
            'body': CONCLUSION_PROMPT.format(RUPTO_TOOLKIT_TEXT=RUPTO_TOOLKIT_TEXT),
        },
        {
            "role": Role.USER,
            "type": "text",
            "body": f'Clients desirable name: {clients_tm_app_name}',
        },
        {
            "role": Role.USER,
            "type": "image_url",
            "body": f'{image_link_to_compare}',
        },
    ]


def generate_compare_message_draft(
    clients_tm_app_name: str, registered_tm: str
) -> list[Dict[str, Any]]:
    return [
        {
            'role': Role.SYSTEM,
            'type': 'text',
            'body': COMPARE_PROMPT,
        },
        {
            'role': Role.USER,
            'type': 'text',
            'body': COMPARE_REQUEST.format(
                clients_tm_app_name=clients_tm_app_name,
                registered_tm=registered_tm,
            ),
        },
    ]


def generate_description_message_draft(
    logo_link: str | None, tm_type: str
) -> list[Dict[str, Any]]:
    return [
        {
            'role': Role.SYSTEM,
            'type': 'text',
            'body': DESCRIPTION_PROMPT,
        },
        {
            'role': Role.USER,
            'type': 'text',
            'body': DESCRIPTION_REQUEST.format(
                tm_type=tm_type,
            ),
        },
        {
            "role": Role.USER,
            "type": "image_url",
            "body": f'{logo_link}',
        },
    ]
