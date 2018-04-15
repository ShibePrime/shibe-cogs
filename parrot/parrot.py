import pathlib
import asyncio  # noqa: F401
import discord
from discord.ext import commands
from cogs.utils.dataIO import dataIO
from cogs.utils import checks
from datetime import datetime

path = 'data/parrot'

class parrot:
    """Waterfall Convo Parrot"""

    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="parrot", pass_context=True)
    async def parrot(self, ctx, game: str):
        """Interactive prompt for making a raid"""
        author = ctx.message.author
        server = ctx.message.server

        await self.bot.say("I will message you to continue.")
        await self.contact_for_parrot(game, author, server)

    async def contact_for_parrot(self, game: str, author, server=None):

        dm = await self.bot.send_message(author,
                                         "Please respond to this message"
                                         "with the details of your raid. If "
                                         "you do not want a details, wait 30s"
                                         "Ex: Prestige Argos ; WoW Mythics ; LFR")
        desc = await self.bot.wait_for_message(channel=dm.channel,
                                                author=author, timeout=30)

        if desc is None:
            await self.bot.send_message(author,
                                        "Okay, this one won't have a description.")

        dm = await self.bot.send_message(author,
                                         "what time? Follow the example format. `MM/DD/YY Hr:MinAM/PM TIMEZONE "
                                         "Ex: 12/25/17 8:00pm PST")
        time = await self.bot.wait_for_message(channel=dm.channel,
                                                  author=author, timeout=120)
        if time is None:
            return await self.bot.send_message(author,
                                               "I can't wait forever, "
                                               "try again when ready")
        else:
        await self.bot.say(game, desc, time, server)
        await self.bot.send_message(author, "Your raid was created")

def setup(bot):
    bot.add_cog(parrot(bot))
