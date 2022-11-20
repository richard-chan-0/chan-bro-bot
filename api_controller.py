from os import getenv
from dotenv import load_dotenv
from requests import request
from langdetect import detect
import json
from random import sample


load_dotenv()

API_KEY = getenv("RAPID_API_KEY")


async def get_urban_dictionary(ctx, arg):
    urban_url = getenv("URBAN_DICTIONARY_URL")
    query = {"term": arg}
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "mashape-community-urban-dictionary.p.rapidapi.com",
    }
    try:
        response = request("GET", urban_url, headers=headers, params=query)
        responses = json.loads(response.text)["list"]
        num_samples = 3 if len(responses) else len(responses)
        indexes = sample(range(len(responses)), num_samples)
        for index in indexes:
            response = responses[index]
            definition = response["definition"]
            author = response["author"]
            await ctx.send(f"{author} says '{arg}' means '{definition}'")

    except TypeError as err:
        await ctx.send("noo...you know ask me properly...")
    finally:
        await ctx.send(f"why did you search for '{arg}' on urban dictionary!!")


async def translate_message(message, source_lang):

    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    target_lang = "en"

    payload = f"q={message}&target={target_lang}&source={source_lang}"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com",
    }

    try:
        response = request("POST", url, data=payload, headers=headers)
        print(response.text)
        payload = json.loads(response.text)
        translations = payload["data"]["translations"]
        if not translations:
            return translations[0]["translatedText"]
        else:
            return "no translation found from google..."
    except Exception as err:
        return None


def detect_langage(message):
    return detect(message)
