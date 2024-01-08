from src.exceptions.exceptions import DiscordBotException
from discord.ext.commands import Context
from discord.ext import commands
from logging import getLogger
from src.api.rapid_api_wrapper import request_rapid_api
from src.exceptions.exceptions import UrbanDictionaryException
from src.config import config
from typing import Iterable


logger = getLogger(__name__)

MAX_RESPONSES = 3


class UrbanDictionaryCog(
    commands.Cog,
    name="Urban Dictionary",
    description="performs Urban Dictionary queries",
):
    def get_definitions_from_response(self, response: dict) -> Iterable[str]:
        """function to parse definitions into list of difinitions"""
        messages = []
        responses = response["list"]
        if not response:
            raise UrbanDictionaryException(f"urban dictionary could not get responses")

        try:
            indexes = min(len(responses), MAX_RESPONSES)
            for index in range(indexes):
                response = responses[index]
                definition = response["definition"]
                author = response["author"]
                messages.append(f"*{definition}* - {author}")

            return messages
        except KeyError as err:
            raise UrbanDictionaryException(f"urban dictionary api failed for: {err}")

    async def get_urban_definition(self, term: str) -> Iterable[str]:
        """function to get urban dictionary definitions for a term"""
        query = {"term": term}
        host = "mashape-community-urban-dictionary.p.rapidapi.com"
        response = await request_rapid_api(
            key=config.api_key,
            url="https://mashape-community-urban-dictionary.p.rapidapi.com/define",
            host=host,
            query=query,
        )

        return self.get_definitions_from_response(response=response)

    def create_response(self, term: str, messages: Iterable[str]) -> str:
        logger.info("creating reply")
        reply_message = f"the term **{term}** means...\n"
        for message in messages:
            reply_message += f"- {message}\n"

        return reply_message

    @commands.command()
    async def define_slang(self, ctx: Context, term: str) -> None:
        """get a definition from urban dictionary"""
        try:
            logger.info(f"getting definition for {term}")
            messages = await self.get_urban_definition(term)
            reply_message = self.create_response(term, messages)
            await ctx.reply(reply_message)

        except DiscordBotException as err:
            logger.error(err)
            await ctx.reply(f"could not lookup {term}")
