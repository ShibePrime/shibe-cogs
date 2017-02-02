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
        em = discord.Embed(title='Click To Connect to Mandrew ARK', description='\"steam:\/\/connect\/71.93.28.250:27015\"\r\n\"Whisper a Doge Master for the password\"\r\n\"NOTE: If it's your first time, You'll have to reconnect multiple times until all the mods are loaded. You can track workshop content download progress in your steam client inbetween reconnects\"', colour=0xDEADBF)
        em.set_author(name='ShibeBot', icon_url='http://i.imgur.com/mYdLixs.png')
        await self.bot.say(embed=em)


def setup(bot):
    n = Shibe(bot)
    bot.add_cog(n)
