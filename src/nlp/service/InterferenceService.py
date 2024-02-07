import os
from openai import OpenAI
from src.nlp.utils.Const import TEMPERATURE, MAX_TOKENS, CLEAN_TEXT

class InferenceService:
    def __init__(self):
        self.__model = os.getenv('OPENAI_MODEL', 'text-davinci-003')
        self.__openai_client = OpenAI()
        self.__text = ""
        self.__prompt_template_resume = 'Dame u resumen en un rango de 10 a 20 palabras del texto: '
        self.__custom_prompt = ""

    def set_custom_prompt(self, custom_prompt):
        self.__prompt_template_resume = custom_prompt;


    def __inference(self, prompt):
        return CLEAN_TEXT(self.__openai_client.completions.create(
            model=self.__model,
            prompt=prompt,
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE
        ).choices[0].text)

    def invokeResume(self, text : str) -> str:
        prompt = (self.__prompt_template_resume) + text
        return self.__inference(prompt)

    def invokeCustom(self, text : str) -> str:
        prompt = (self.__custom_prompt) + " en el texto: " + text
        return self.__inference(prompt)