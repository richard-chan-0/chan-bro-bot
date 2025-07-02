from src.lib.config import CONFIG
from logging import getLogger

logger = getLogger(__name__)


def get_shared_game_suggestions():
    steam_ids = CONFIG.steam_ids
    logger.info(f"Fetching game suggestions for steam IDs: {steam_ids}")
    return ["test", "test2"]
