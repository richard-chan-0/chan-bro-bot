from dataclasses import dataclass
from os import getenv


@dataclass
class Config:
    api_key: str
    discord_key: str
    urban_dictionary_url: str


API_KEY = getenv("RAPID_API_KEY")
URBAN_URL = getenv("URBAN_DICTIONARY_URL")
TOKEN = getenv("DISCORD_TOKEN")

config = Config(api_key=API_KEY, discord_key=TOKEN, urban_dictionary_url=URBAN_URL)
