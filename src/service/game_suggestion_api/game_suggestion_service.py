from src.bot.config import CONFIG
from logging import getLogger
from src.service.game_suggestion_api.game_suggestion_wrapper import (
    get_shared_games_for_all_players,
)
from src.service.game_suggestion_api.game_suggestion_adapter import (
    create_shared_games_response,
)

logger = getLogger(__name__)


def get_shared_game_suggestions():
    """
    Fetch shared game suggestions for all players and format the response.
    """
    json_response = get_shared_games_for_all_players()
    list_games = json_response.get("games", [])
    if not list_games:
        return "No shared games found."

    games_string = create_shared_games_response(list_games)

    return f"Here are the shared games:\n{games_string}"
