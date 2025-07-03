from dataclasses import dataclass, field
from os import getenv
from json import loads


@dataclass
class Config:
    api_key: str
    discord_key: str
    general_channel_id: str
    video_channel_id: str
    game_suggestion_url: str
    steam_ids: list = field(default_factory=list)


API_KEY = getenv("RAPID_API_KEY")
TOKEN = getenv("DISCORD_TOKEN")
GENERAL = getenv("GENERAL_CHANNEL_ID")
VIDEO = getenv("VIDEO_CHANNEL_ID")
GAME_SUGGESTION_URL = getenv("GAME_SUGGESTION_URL")

with open("users.json", "r") as file:
    json_data = loads(file.read())
STEAM_IDS = [user["steam_id"] for user in json_data.get("group_users", {})]

CONFIG = Config(
    api_key=API_KEY,
    discord_key=TOKEN,
    general_channel_id=GENERAL,
    video_channel_id=VIDEO,
    game_suggestion_url=GAME_SUGGESTION_URL,
    steam_ids=STEAM_IDS,
)
