import json
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
        await self.get_pollen()
        """Prints pollen"""

    async def get_pollen(self):
        async with ClientSession() as websession:
            await self.run(websession)

    async def run(websession):
        client = pypollencom.Client(98908, websession)
        data = client.allergens.current()
        em = discord.Embed(title='', description=data, colour=0x6FA8DC, )
        await self.bot.say(embed=em)

def setup(bot):
    bot.add_cog(pollen(bot))
