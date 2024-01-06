from src.api.rapid_api_wrapper import request_rapid_api
from src.exceptions.exceptions import RapidApiException
from src.config import config
from typing import Iterable


MAX_RESPONSES = 3


def get_definitions_from_response(response: dict) -> Iterable[str]:
    """function to parse definitions into list of difinitions"""
    messages = []

    try:
        responses = response["list"]
        if not response:
            raise RapidApiException(f"urban dictionary could not get responses")

        indexes = min(len(responses), MAX_RESPONSES)
        for index in range(indexes):
            response = responses[index]
            definition = response["definition"]
            author = response["author"]
            messages.append(f"*{definition}* - {author}")

        return messages

    except Exception as err:
        raise RapidApiException(f"urban dictionary api failed for: {err}")


async def get_urban_definition(term: str) -> Iterable[str]:
    """function to get urban dictionary definitions for a term"""

    query = {"term": term}
    host = "mashape-community-urban-dictionary.p.rapidapi.com"
    response = await request_rapid_api(
        key=config.api_key, url=config.urban_dictionary_url, host=host, query=query
    )

    if not response:
        return []

    return get_definitions_from_response(response=response)
