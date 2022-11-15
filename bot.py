import os
from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv
from requests import request
import json
from random import sample

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!!")


@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)


@bot.command(name="ud")
async def urban_dictionary(ctx, arg):
    urban_url = os.getenv("URBAN_DICTIONARY_URL")
    query = {"term": arg}
    headers = {
        "X-RapidAPI-Key": "d2a33b43c8mshf876d903bee8ee9p198929jsn920fa3852e7a",
        "X-RapidAPI-Host": "mashape-community-urban-dictionary.p.rapidapi.com",
    }
    try:
        response = request("GET", urban_url, headers=headers, params=query)
        responses = json.loads(response.text)["list"]
        num_samples = 3 if len(responses) else len(responses)
        indexes = sample(range(len(responses)), num_samples)
        for index in indexes:
            response = responses[index]
            definition = response["definition"]
            author = response["author"]
            await ctx.send(f"{author} says '{arg}' means '{definition}'")

    except TypeError as err:
        await ctx.send("noo...you know ask me properly...")
    finally:
        await ctx.send(f"why did you search for '{arg}' on urban dictionary!!")


bot.run(TOKEN)
