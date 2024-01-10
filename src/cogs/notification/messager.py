from discord.ext import commands, tasks
from src.config import Config


class NotificationCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @tasks.loop(seconds=10)
    async def test_tasks(self):
        channel_id = int(Config.general_channel_id)
        channel = self.bot.get_channel(channel_id)
        await channel.send("https://discordpy.readthedocs.io/en/stable/index.html")
