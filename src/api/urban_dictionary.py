from os import getenv
from dotenv import load_dotenv
from random import sample
from src.api.rapid_api_wrapper import request_rapid_api
from src.exceptions.exceptions import RapidApiException
from typing import Iterable

load_dotenv()

API_KEY = getenv("RAPID_API_KEY")

MAX_RESPONSES = 3


def parse_response(term, response) -> Iterable[str]:
    messages = []

    try:
        responses = response["list"]
        num_samples = MAX_RESPONSES if len(responses) else len(responses)
        indexes = sample(range(len(responses)), num_samples)
        for index in indexes:
            response = responses[index]
            definition = response["definition"]
            author = response["author"]
            messages.append(f"{author} says '{term}' means '{definition}'")

        return messages

    except Exception as err:
        raise RapidApiException(f"urban dictionary api failed for: {err}")


async def get_urban_definition(arg) -> Iterable[str]:
    urban_url = getenv("URBAN_DICTIONARY_URL")
    query = {"term": arg}
    host = "mashape-community-urban-dictionary.p.rapidapi.com"
    response = await request_rapid_api(
        key=API_KEY, url=urban_url, host=host, query=query
    )

    if not response:
        return []

    return parse_response(arg, response=response)
