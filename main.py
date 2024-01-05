import os
from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv
import src.discord.bot_commands as Commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!!")


@bot.command(name="ud")
async def urban_dictionary(ctx, arg):
    """function to get definition for a term"""
    await Commands.get_urban_dictionary_definition(ctx, arg)


bot.run(TOKEN)
