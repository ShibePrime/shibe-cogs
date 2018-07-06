import discord
import pypollencom
import asyncio
from aiohttp import ClientSession
from discord.ext import commands
from pypollencom import Client

class pollen:
    """get pollen"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="pollen", pass_context=True)
    async def pollen(self, ctx):
        async with ClientSession() as websession:
            Client = pypollencom.Client(98908, websession)
            data = Client.allergens.current()
            em = discord.Embed(title='', description=data, colour=0x6FA8DC, )
            a   wait self.bot.say(embed=em)

def setup(bot):
    bot.add_cog(pollen(bot))
