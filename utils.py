import base64
import json
import logging
from typing import Union, Dict, Any, List

import requests


def convert_string_to_json(data_to_convert: str) -> Union[Dict[str, Any], List[Any]]:
    try:
        data_for_chat = json.loads(data_to_convert)
    except json.JSONDecodeError as e:
        logging.warning(f'Error parsing JSON: {e}')
        data_for_chat = []
    return data_for_chat


def convert_image_to_base64(image_url):
    try:
        response = requests.get(image_url)
        return base64.b64encode(response.content).decode('utf-8')
    except Exception as e:
        logging.warning(f'Error converting image to base64: {e}')
        return None
