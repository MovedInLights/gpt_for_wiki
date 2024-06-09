import base64

from openai import OpenAI


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


class ChatClient:
    def chat_with_gpt(self) -> str:
        api_key = "TEST"
        if not api_key:
            raise ValueError("GPT key was not obtained")

        base64_image = encode_image("./img.png")

        client = OpenAI(api_key=api_key)

        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            },
                        },
                        {"type": "text", "text": "What is on this image"},
                    ],
                }
            ],
        )

        return completion.choices[0].message.content


print(ChatClient().chat_with_gpt())
