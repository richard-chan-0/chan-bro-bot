from dataclasses import dataclass
from os import getenv


@dataclass
class Config:
    api_key: str
    discord_key: str
    general_channel_id: str
    video_channel_id: str


API_KEY = getenv("RAPID_API_KEY")
TOKEN = getenv("DISCORD_TOKEN")
GENERAL = getenv("GENERAL_CHANNEL_ID")
VIDEO = getenv("VIDEO_CHANNEL_ID")

CONFIG = Config(
    api_key=API_KEY,
    discord_key=TOKEN,
    general_channel_id=GENERAL,
    video_channel_id=VIDEO,
)
