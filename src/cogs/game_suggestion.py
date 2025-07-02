from discord.ext.commands import Context
from discord.ext import commands
from logging import getLogger
from src.service.logic.game_suggestion_service import get_shared_game_suggestions

logger = getLogger(__name__)


class GameSuggestionCog(
    commands.Cog,
    name="Game Suggestion",
    description="performs game suggestion api queries",
):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def get_shared_games(self, ctx: Context) -> None:
        reply_message = get_shared_game_suggestions()
        await ctx.reply(reply_message)
