from discord import Intents
from discord.ext import commands
import src.discord.bot_commands as Commands
from logging import getLogger
from src.config import config

logger = getLogger(__name__)

intents = Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    logger.info(f"{bot.user.name} has connected to Discord!!")


@bot.command(name="ud", help="returns the definition of a term via Urban Dictionary")
async def urban_dictionary(ctx, arg):
    """function to get definition for a term"""
    await Commands.get_urban_dictionary_definition(ctx, arg)


bot.run(config.discord_key)
