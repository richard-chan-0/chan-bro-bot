from requests import get, post
from logging import getLogger
from src.lib.exceptions import GameSuggestionExcepion

logger = getLogger(__name__)


def get_shared_games() -> dict:
    try:
        logger.info("sending api request")
        api_response = get(url="localhost:5010")
        return api_response.json()
    except Exception as err:
        logger.error(err)
        raise GameSuggestionExcepion(err)
