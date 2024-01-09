from discord import Intents
from discord.ext import commands
from src.cogs.urban_dictionary.urban_dictionary import UrbanDictionaryCog
from src.cogs.messager.messager import MessagerCog
from logging import getLogger
from src.config import config

logger = getLogger(__name__)

intents = Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    logger.info(f"{bot.user.name} has connected to Discord!!")
    await bot.add_cog(UrbanDictionaryCog(bot))
    await bot.add_cog(MessagerCog(bot))


bot.run(config.discord_key)
