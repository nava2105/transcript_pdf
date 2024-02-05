import os
from openai import OpenAI
from src.nlp.utils.Const import TEMPERATURE, MAX_TOKENS, CLEAN_TEXT

class InferenceService:
    def __init__(self):
        self.__model = os.getenv('OPENAI_MODEL', 'text-davinci-003')
        self.__openai_client = OpenAI()
        self.__prompt_template = 'Eres lingüista y especialista en psicología, dime la emoción más representativa en el texto {text} '

    def __inference(self, prompt):
        return CLEAN_TEXT(self.__openai_client.completions.create(
            model=self.__model,
            prompt=prompt,
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE
        ).choices[0].text)

    def invoke(self, text: str) -> str:
        prompt = self.__prompt_template.format(text=str)
        return self.__inference(prompt)