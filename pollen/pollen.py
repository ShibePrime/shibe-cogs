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
    async def main(self) -> None:
        """Create the aiohttp session and run the example."""
        async with ClientSession() as websession:
            await self.run(websession)

    async def run(self, websession):
            client = await pypollencom.Client(98908, websession)
            data = await client.allergens.current()
#            em = discord.Embed(title='', description=data, colour=0x6FA8DC, )
#            await self.bot.say(embed=em)
            await self.bot.say(data)
            return data

def setup(bot):
    bot.add_cog(pollen(bot))
