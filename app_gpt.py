import os
import openai
from app import *
from openai import OpenAI


def chatgpt(messages):

    openai_client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": messages,
            }
        ],
        stream=True
    )

    for chunk in response:
        part = chunk.choices[0].delta.content
        if part is not None:
            yield part
        else:
            return None
