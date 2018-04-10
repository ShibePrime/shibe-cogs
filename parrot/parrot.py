import pathlib
import asyncio  # noqa: F401
import discord
from discord.ext import commands
from cogs.utils.dataIO import dataIO
from cogs.utils import checks
from datetime import datetime

path = 'data/parrot'

class parrot:
    """Waterfall Convo Repeat and Join"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="pun", pass_context=True)
    async def parrot(self, ctx):
        await self.ask()
        """Prints Random Puns"""

    async def ask(self):
        await self.bot.send_message(author,
                                         "Please respond to this message "
                                         "with your message you want to say "
                                         "you do want? wait 30s")
        title = await self.bot.wait_for_message(channel=channel,
                                                author=author, timeout=30)
        if title is None:
            await self.bot.send_message(author,
                                        "Okay, fine.")
        else:
            self.bot.send_message(author, ":", title)

def setup(bot):
    bot.add_cog(parrot(bot))
