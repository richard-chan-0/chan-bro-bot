import os
from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv
import api_controller

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!!")


@bot.event
async def on_message(message):
    lang = api_controller.detect_langage(message.content)
    if message.author != bot.user and lang == "zh-cn":
        translate = await api_controller.translate_message(message, lang)
        if not translate:
            return
        await message.reply(
            f"fancy language found! bot googled and found you said...'{translate}'"
        )


@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)


@bot.command(name="ud")
async def urban_dictionary(ctx, arg):
    await api_controller.get_urban_dictionary(ctx, arg)


bot.run(TOKEN)
