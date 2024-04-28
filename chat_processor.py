import os

from openai import OpenAI

# можно сделать класс и добавлять туда методы, которые могут быть выполнены
# Сделать класс клиент. Второй класс с логикой.
# Во втором классе должен использоваться клиент


class ChatClient:
    def chat_with_gpt(self, prompt_content: str, request_text: str) -> str:
        api_key = os.getenv('GPT_KEY')
        if not api_key:
            raise ValueError('GPT key was not obtained')

        client = OpenAI(api_key=api_key)

        completion = client.chat.completions.create(
            model='gpt-3.5-turbo-0125',
            messages=[
                {'role': 'system', 'content': prompt_content},
                {'role': 'user', 'content': request_text},
            ],
        )

        return completion.choices[0].message.content
