from discord.ext.commands import Context
from discord.ext import commands
from logging import getLogger
from src.service.urban_dictionary_api.urban_dictionary_service import get_definition


logger = getLogger(__name__)


class UrbanDictionaryCog(
    commands.Cog,
    name="Urban Dictionary",
    description="performs Urban Dictionary queries",
):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def define_slang(self, ctx: Context, term: str) -> None:
        """get a definition from urban dictionary"""
        logger.info(f"Received request to define term: {term}")
        reply_message = await get_definition(term)
        await ctx.reply(reply_message)
