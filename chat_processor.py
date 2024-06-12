import logging
import os
from typing import Dict, Any

from openai import OpenAI

from utils import create_gpt_message, convert_url_image_to_base64


# можно сделать класс и добавлять туда методы, которые могут быть выполнены
# Сделать класс клиент. Второй класс с логикой.
# Во втором классе должен использоваться клиент
#
#


class ChatClient:
    def prepare_image(self, url: str):
        pass

    def compile_messages(self, messages_draft: list) -> list[dict]:
        messages = []
        for message in messages_draft:
            logging.info(f'Working with message: {message}')
            if message['type'] != 'text':
                message_to_add = self.prepare_message(
                    role=message['role'],
                    message_type=message['type'],
                    base64_img=convert_url_image_to_base64(message['body']),
                )
                messages.append(message_to_add)
            else:
                message_to_add = self.prepare_message(
                    role=message['role'],
                    message_type=message['type'],
                    text=message['body'],
                )
                messages.append(message_to_add)
        return messages

    def prepare_message(
        self, role: str, message_type: str, base64_img: str | None = "", text: str = ""
    ) -> Dict[str, Any]:
        if base64_img != "":
            return create_gpt_message(
                role=role, message_type=message_type, base64_img=base64_img
            )
        if text != "":
            return create_gpt_message(role=role, message_type=message_type, text=text)
        return {}

    def chat_with_gpt(self, model: str, temperature: int, messages: dict) -> str:
        api_key = os.getenv("GPT_KEY")
        if not api_key:
            raise ValueError("GPT key was not obtained")

        client = OpenAI(api_key=api_key)

        completion = client.chat.completions.create(
            model=model,
            messages=messages,
        )

        return completion.choices[0].message.content
