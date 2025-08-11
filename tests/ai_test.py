from google.api_core import exceptions
from dotenv import load_dotenv
import google.generativeai as genai
import os





def execute_ai(question):

    os.system("cls")

    load_dotenv()
    token = os.getenv("GEMINI_TOKEN")
    genai.configure(api_key=token)

    model = genai.GenerativeModel("gemini-2.5-flash")

    try:
        response = model.generate_content(question)
        return response.text


    except exceptions.ResourceExhausted:
        return "ERRO."