from logging import getLogger, StreamHandler, Formatter, basicConfig
from sys import stdout
from dotenv import load_dotenv

load_dotenv()

from src.bot.bot import bot
from src.bot.config import CONFIG
from src.cogs import *

basicConfig(
    level="INFO",
    handlers=[StreamHandler(stdout)],
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
logger = getLogger(__name__)


def main():
    try:
        logger.info("starting bot...")
        bot.run(token=CONFIG.discord_key)
    except Exception as e:
        logger.error(e)


if __name__ == "__main__":
    main()
