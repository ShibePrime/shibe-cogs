import asyncio
import json

import aiohttp
from discord.ext import commands

from .utils import chat_formatting as cf


class PieFact:

    """Gets random pie facts."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.url = "https://catfacts-api.appspot.com/api/facts?number={}"

    @commands.command(pass_context=True, no_pm=True, name="piefact",
                      aliases=["piefacts"])
    async def _piefact(self, ctx: commands.Context, number: int=1):
        """Gets random pie facts."""

        await self.bot.type()

        if number > 10:
            await self.bot.reply(cf.warning("Be reasonable, please."))
            return

        async with aiohttp.get(self.url.format(number)) as response:
            for fact in json.loads(await response.text())["facts"]:
                await self.bot.say(fact)
                await asyncio.sleep(0.25)


def setup(bot: commands.Bot):
    bot.add_cog(PieFact(bot))
