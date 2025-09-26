from dataclasses import dataclass, field
from src.lib.exceptions import DiscordBotException
from os import getenv
from json import loads
from logging import getLogger

logger = getLogger(__name__)


@dataclass
class Config:
    api_key: str
    discord_key: str
    general_channel_id: str
    video_channel_id: str
    game_suggestion_command_url: str
    game_suggestion_rest_url: str
    steam_ids: list = field(default_factory=list)


def create_config():
    logger.info("creating config from environment variables")
    api_key = getenv("RAPID_API_KEY")
    discord_token = getenv("DISCORD_TOKEN")
    general_channel_id = getenv("GENERAL_CHANNEL_ID")
    video_channel_id = getenv("VIDEO_CHANNEL_ID")  # TODO: what was this for?
    game_suggestion_command_url = getenv("GAME_SUGGESTION_COMMAND_URL")
    game_suggestion_rest_url = getenv("GAME_SUGGESTION_REST_URL")

    config_map = {
        "api_key": api_key,
        "discord_token": discord_token,
        "general_channel_id": general_channel_id,
        # "video_channel_id": video_channel_id,
        "game_suggestion_command_url": game_suggestion_command_url,
        "game_suggestion_rest_url": game_suggestion_rest_url,
    }

    for key, value in config_map.items():
        if not value:
            raise DiscordBotException(
                f"One or more environment variables are missing: {key}"
            )
    logger.info(f"config %s", config_map)

    with open("users.json", "r") as file:
        json_data = loads(file.read())

    steam_ids = [user["steam_id"] for user in json_data.get("group_users", {})]

    return Config(
        api_key=api_key,
        discord_key=discord_token,
        general_channel_id=general_channel_id,
        video_channel_id=video_channel_id,
        game_suggestion_command_url=game_suggestion_command_url,
        game_suggestion_rest_url=game_suggestion_rest_url,
        steam_ids=steam_ids,
    )


CONFIG = create_config()
