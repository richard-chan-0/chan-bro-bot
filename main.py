from src.cogs import *
from logging import getLogger, StreamHandler, Formatter
from sys import stdout
from src.bot.config import CONFIG
from src.bot.bot import bot
from dotenv import load_dotenv

load_dotenv()

logger = getLogger(__name__)
logger.setLevel("INFO")
handler = StreamHandler(stdout)
handler.setFormatter(Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s"))
logger.addHandler(handler)


def main():
    try:
        bot.run(CONFIG.discord_key)
    except Exception as e:
        logger.error(e)


if __name__ == "__main__":
    main()
