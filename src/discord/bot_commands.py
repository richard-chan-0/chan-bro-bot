from os import getenv
from src.api.urban_dictionary import get_urban_definition
from src.exceptions.exceptions import DiscordBotException
from discord.ext.commands import Context
from logging import getLogger

logger = getLogger(__name__)

API_KEY = getenv("RAPID_API_KEY")


async def get_urban_dictionary_definition(ctx: Context, term: str):
    """function to reply to user with definitions from urban dictionary for a term"""
    try:
        messages = await get_urban_definition(term)
        if not messages:
            await ctx.reply(f"could not lookup {term}")
            return

        for message in messages:
            await ctx.reply(message)
    except DiscordBotException as err:
        logger.error(err)
        await ctx.reply("could not complete urban dictionary lookup")
