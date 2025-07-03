from requests import get, post
from logging import getLogger
from src.lib.exceptions import GameSuggestionExcepion
from src.lib.config import CONFIG

logger = getLogger(__name__)


def get_shared_games(steam_ids: list) -> dict:
    try:
        api_url = f"{CONFIG.game_suggestion_url}/shared"
        logger.info("sending api request to %s with steam_ids: %s", api_url, steam_ids)
        api_response = post(url=api_url, data={"steam_ids": steam_ids})
        return api_response.json()
    except Exception as err:
        logger.error(err)
        raise GameSuggestionExcepion(err)
