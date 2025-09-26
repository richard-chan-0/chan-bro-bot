from discord.ext.commands import Context
from discord.ext import commands
from logging import getLogger
from src.service.game_suggestion_api.game_suggestion_service import (
    get_shared_game_suggestions,
)

logger = getLogger(__name__)


class GameSuggestionCog(
    commands.Cog,
    name="Game Suggestion",
    description="performs game suggestion api queries",
):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="sharedgames", help="Get shared game suggestions for all players"
    )
    async def get_shared_games(self, ctx: Context, *args) -> None:
        reply_message = f"Args: {args}"
        if args:
            reply_message = "args not supported"
        else:
            reply_message = get_shared_game_suggestions()
        await ctx.reply(reply_message)
