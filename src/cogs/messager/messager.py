from discord.ext import commands
from discord import Message
from src.cogs.messager.greetings import is_greeting, greet_user
from typing import Iterable, Callable, Tuple


class MessagerCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: Message):
        if message.author == self.bot.user:
            return

        reply = self.create_reply(message)
        if reply:
            await message.channel.send(reply)

    def get_all_message_handlers(self) -> Iterable[Tuple[Callable, Callable]]:
        return [(is_greeting, greet_user)]

    def get_message_handler(self, message: str) -> Callable:
        message_handlers = self.get_all_message_handlers()
        for is_message, message_replier in message_handlers:
            if is_message(message):
                return message_replier

    def create_reply(self, message: Message) -> str:
        text = message.content

        handler = self.get_message_handler(text)

        if not handler:
            return

        return handler()
