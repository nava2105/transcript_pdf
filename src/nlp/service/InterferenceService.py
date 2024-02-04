import os
from openai import OpenAI
from src.nlp.utils.Const import TEMPERATURE, MAX_TOKENS, CLEAN_TEXT

class InferenceService:
    def __init__(self):
        self.__model = os.getenv('OPENAI_MODEL', 'text-davinci-003')
        self.__openai_client = OpenAI()
        self.__prompt_template = 'Transform the number {number} to binary, Example: Number: 7 Binary: 111'

    def __inference(self, prompt):
        return CLEAN_TEXT(self.__openai_client.completions.create(
            model=self.__model,
            prompt=prompt,
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE
        ).choices[0].text)

    def invoke(self, number: int) -> str:
        prompt = self.__prompt_template.format(number=int)
        return self.__inference(prompt)