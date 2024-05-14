from discord.ext import commands, tasks
from discord import Member, Status
from src.lib.config import CONFIG
import datetime as dt
from zoneinfo import ZoneInfo
from random import randint

BED_TIME = dt.time(hour=23, tzinfo=ZoneInfo("America/Chicago"))


class GoodNightCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.channel = self.bot.get_channel(int(CONFIG.general_channel_id))
        self.good_night_notification.start()

    def cog_unload(self):
        self.good_night_notification.cancel()

    def get_night_message(self):
        messages = ["good night!", "晚安!", "go to sleep, go to sleep, go to sleep!"]
        message_index = randint(0, len(messages))
        return messages[message_index]

    @tasks.loop(time=BED_TIME)
    async def good_night_notification(self):
        await self.channel.send(self.get_night_message())


class PresenceUpdateCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.channel = self.bot.get_channel(int(CONFIG.general_channel_id))

    def is_online(self, member: Member):
        if member.status == Status.online:
            self.channel.send(f"{member.display_name} is online")

    @commands.Cog.listener()
    async def on_presence_update(self, before, after):
        self.is_online(after)
