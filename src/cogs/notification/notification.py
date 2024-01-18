from discord.ext import commands, tasks
from src.config import Config
import datetime as dt
from random import randint

night = dt.time(hour=23, minute=30)


class NotificationCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    def get_night_message(self):
        messages = ["good night!", "晚安！"]
        message_index = randint(0, len(messages))
        return messages[message_index]

    @tasks.loop(time=night)
    async def good_night_notification(self):
        channel_id = int(Config.general_channel_id)
        channel = self.bot.get_channel(channel_id)

        await channel.send(self.get_night_message())
