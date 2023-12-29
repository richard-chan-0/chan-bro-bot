from os import getenv
from requests import request
import json
from random import sample
from src.api.urban_dictionary import get_urban_definition
from src.exceptions.exceptions import DiscordBotException
from logging import getLogger

logger = getLogger(__name__)

API_KEY = getenv("RAPID_API_KEY")


async def get_urban_dictionary_definition(ctx, term):
    try:
        messages = await get_urban_definition(term)
        if not messages:
            await ctx.send(f"could not lookup {term}")
            return

        for message in messages:
            await ctx.send(message)
    except DiscordBotException as err:
        logger.error(err)
        await ctx.send("could not complete urban dictionary lookup")
