# noinspection PyUnresolvedReferences
import discord
from discord.ext import commands

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
        await self.bot.say("Click To Connect to Mandrew ARK")
        await self.bot.say("steam://connect/71.93.28.250:27015")

def setup(bot):
    n = Shibe(bot)
    bot.add_cog(n)
