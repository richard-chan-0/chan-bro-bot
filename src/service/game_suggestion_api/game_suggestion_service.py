from src.bot.config import CONFIG
from logging import getLogger
from src.service.game_suggestion_api.game_suggestion_wrapper import get_shared_games
from src.service.game_suggestion_api.game_suggestion_adapter import (
    create_shared_games_response,
)

logger = getLogger(__name__)


def get_shared_game_suggestions():
    steam_ids = CONFIG.steam_ids
    logger.info(f"Fetching game suggestions for steam IDs: {steam_ids}")
    list_games = get_shared_games(steam_ids=steam_ids)
    games_string = create_shared_games_response(list_games)
    logger.info(f"Shared games: {games_string}")
    return f"Here are the shared games:\n{games_string}"
