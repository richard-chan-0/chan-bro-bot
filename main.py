from discord import Intents
from discord.ext import commands
from src.cogs.urban_dictionary import UrbanDictionaryCog
from src.cogs.messager import MessagerCog
from src.cogs.notification import *
from logging import getLogger
from src.lib.config import CONFIG

logger = getLogger(__name__)

intents = Intents.default()
intents.message_content = True
intents.presences = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    logger.info(f"{bot.user.name} has connected to Discord!!")
    await bot.add_cog(UrbanDictionaryCog(bot))
    await bot.add_cog(GoodNightCog(bot))
    await bot.add_cog(MessagerCog(bot))
    # await bot.add_cog(PresenceUpdateCog(bot))


def main():
    try:
        bot.run(CONFIG.discord_key)
    except Exception as e:
        logger.error(e)


if __name__ == "__main__":
    main()
