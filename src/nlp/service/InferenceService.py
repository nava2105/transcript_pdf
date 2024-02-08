import os
from openai import OpenAI
from src.nlp.utils.Const import TEMPERATURE, MAX_TOKENS, CLEAN_TEXT

class InferenceService:
    def __init__(self):
        self.__model = os.getenv('OPENAI_MODEL', 'text-davinci-003')
        self.__openai_client = OpenAI()
        self.__text = ""
        self.__prompt_template_resume = 'Dame un resumen en un rango de 10 a 20 palabras del texto: '

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

    def invokeCustom(self, question : str, text : str) -> str:
        prompt = "Responde la pregunta: " + question + " en base a el texto: " + text
        return self.__inference(prompt)