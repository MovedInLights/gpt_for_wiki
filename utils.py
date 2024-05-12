import base64
import json
import logging
from io import BytesIO
from typing import Union, Dict, Any, List

import requests
from PIL import Image


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
        response.raise_for_status()
        compressed_image = Image.open(BytesIO(response.content))
        compressed_image.thumbnail((120, 80), Image.Resampling.LANCZOS)

        img_byte_arr = BytesIO()
        image_format = 'JPEG'
        compressed_image.save(img_byte_arr, format=image_format, quality=75)
        decoded_image = base64.b64encode(img_byte_arr.getvalue()).decode('utf-8')
        logging.info(f'Decoded image: {decoded_image}')
        return decoded_image
    except Exception as e:
        logging.warning(f'Error converting image to base64: {e}')
        return None
