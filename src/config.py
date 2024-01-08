from dataclasses import dataclass
from os import getenv


@dataclass
class Config:
    api_key: str
    discord_key: str


API_KEY = getenv("RAPID_API_KEY")
TOKEN = getenv("DISCORD_TOKEN")

config = Config(api_key=API_KEY, discord_key=TOKEN)
