import json
import discord
from aiohttp import ClientSession
from discord.ext import commands

url = 'https://www.pollen.com/api/forecast/current/pollen/98908'
headers = {'Content-Type': 'application/json; charset=utf-8','Referer': 'https://www.pollen.com'}


class pollen:
    """get pollen"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="pollen", pass_context=True)
    async def pollen(self, ctx):
        await self.get_pollen()
        """Prints pollen"""

    async def get_pollen(self):
        async with ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                pollen = await response.text()
#                em = discord.Embed(title='', description=pollenstr, colour=0x6FA8DC, )
#                data = pollen["Type"]
                await self.bot.say(pollen)
                print (pollen)
def setup(bot):
    bot.add_cog(pollen(bot))