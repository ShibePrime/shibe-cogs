# noinspection PyUnresolvedReferences
import discord
from discord.ext import commands
from cogs.utils import checks
from cogs.utils.chat_formatting import box,  pagify, escape_mass_mentions
from random import choice, randint
import datetime

__author__ = "shibe "

class Shibe:
    """fun random commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def suh(self):
        await self.bot.say(" :v: SUH DUDE :v: ")

    @commands.command()
    async def ark(self):
        em = discord.Embed(title='My Embed Title', description='My Embed Content.', colour=0xDEADBF)
        em.set_author(name='Someone', icon_url=client.user.default_avatar_url)
        await client.send_message(message.channel, embed=em)


def setup(bot):
    n = Shibe(bot)
    bot.add_cog(n)
