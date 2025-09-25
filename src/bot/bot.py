from discord import Intents
from discord.ext import commands
from src.cogs import *


intents = Intents.default()
intents.message_content = True
intents.presences = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    await bot.add_cog(UrbanDictionaryCog(bot))
    await bot.add_cog(GoodNightCog(bot))
    await bot.add_cog(MessagerCog(bot))
    await bot.add_cog(GameSuggestionCog(bot))
    # await bot.add_cog(PresenceUpdateCog(bot))
