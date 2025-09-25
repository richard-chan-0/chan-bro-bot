from logging import getLogger
from typing import Iterable
from src.bot.config import CONFIG
from src.lib.rapid_api_wrapper import request_rapid_api
from src.lib.exceptions import DiscordBotException, UrbanDictionaryException

logger = getLogger(__name__)

MAX_RESPONSES = 3
URBAN_DICTIONARY_HOST = "mashape-community-urban-dictionary.p.rapidapi.com"
URBAN_DICTIONARY_URL = (
    "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
)


def get_definitions_from_response(response: dict) -> Iterable[str]:
    """function to parse definitions into list of difinitions"""
    messages = []
    responses = response["list"]
    if not response:
        raise UrbanDictionaryException(f"urban dictionary could not get responses")

    try:
        indexes = min(len(responses), MAX_RESPONSES)
        for index in range(indexes):
            response = responses[index]
            definition = response["definition"]
            author = response["author"]
            messages.append(f"*{definition}* - {author}")

        return messages
    except KeyError as err:
        raise UrbanDictionaryException(f"urban dictionary api failed for: {err}")


async def get_urban_definition(term: str) -> Iterable[str]:
    """function to get urban dictionary definitions for a term"""
    query = {"term": term}
    host = URBAN_DICTIONARY_HOST
    response = await request_rapid_api(
        key=CONFIG.api_key,
        url=URBAN_DICTIONARY_URL,
        host=host,
        query=query,
    )

    return get_definitions_from_response(response=response)


def create_response(term: str, messages: Iterable[str]) -> str:
    logger.info("creating reply")
    reply_message = f"the term **{term}** means...\n"
    for message in messages:
        reply_message += f"- {message}\n"

    return reply_message


async def get_definition(term):
    """get a definition from urban dictionary"""
    try:
        logger.info(f"getting definition for {term}")
        messages = await get_urban_definition(term)
        return create_response(term, messages)

    except DiscordBotException as err:
        logger.error(err)
        return f"could not lookup {term}"
