from os import getenv
from src.api.urban_dictionary import get_urban_definition
from src.exceptions.exceptions import DiscordBotException
from discord.ext.commands import Context
from logging import getLogger

logger = getLogger(__name__)

API_KEY = getenv("RAPID_API_KEY")


async def get_urban_dictionary_definition(ctx: Context, term: str):
    """function to reply to user with definitions from urban dictionary for a term"""
    failure_message = f"could not lookup {term}"
    try:
        messages = await get_urban_definition(term)

        reply_message = f"the term **{term}** means...\n"
        for message in messages:
            reply_message += f"- {message}\n"

        await ctx.reply(reply_message)

    except DiscordBotException as err:
        logger.error(err)
        await ctx.reply(failure_message)
