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
        data = discord.Embed(title=str(text)
        await self.bot.say(embed=data)

def setup(bot):
    n = Shibe(bot)
    bot.add_cog(n)
