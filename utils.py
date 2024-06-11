import base64
import logging
import os
from enum import Enum
from io import BytesIO
from typing import Union, Dict, Any, List

import requests
from PIL import Image

from prompts import CONCLUSION_PROMPT, RUPTO_TOOLKIT_TEXT


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


def convert_image_to_base64(image_url):
    try:
        response = requests.get(image_url)
        response.raise_for_status()
        compressed_image = Image.open(BytesIO(response.content))
        compressed_image.thumbnail((120, 80), Image.Resampling.LANCZOS)

        img_byte_arr = BytesIO()
        image_format = "JPEG"
        compressed_image.save(img_byte_arr, format=image_format, quality=75)
        decoded_image = base64.b64encode(img_byte_arr.getvalue()).decode("utf-8")
        logging.info(f"Decoded image: {decoded_image}")
        return decoded_image
    except Exception as e:
        logging.warning(f"Error converting image to base64: {e}")
        return None


def create_gpt_message(
    role: str, message_type: str, base64_img: str = "", text: str = ""
):
    logging.info(f"Creating GPT message for {role} {message_type} {base64_img} {text}")

    if message_type == "image_url":
        image_dict_data_for_gpt = get_image_gpt_dict(base64_img)
        return {
            "role": role,
            "content": {
                "type": message_type,
                "image_url": image_dict_data_for_gpt,
            },
        }
    return {
        "role": role,
        "content": text,
    }


def get_image_gpt_dict(base64_img: str) -> Union[Dict[str, Any], List[Any]]:
    return {"url": f"data:image/jpeg;base64,{base64_img}"}


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def compare_tokens(token: str) -> bool:
    api_token = os.getenv("API_GPT_TOKEN")
    if not token or api_token is None or token != "Bearer " + api_token:
        return False
    return True


def generate_conclusion_message_draft(clients_tm_app_name, image_link_to_compare):
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
