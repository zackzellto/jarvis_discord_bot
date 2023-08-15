import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai_key = os.getenv('OPENAI_API_KEY')


def get_gpt4_response(question):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=150
    )
    return response.choices[0].text
