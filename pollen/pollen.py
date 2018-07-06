import json
import discord
from aiohttp import ClientSession
from discord.ext import commands

url = 'https://www.pollen.com/api/forecast/current/pollen/98908'
headers = {'Content-Type': 'application/json; charset=utf-8','Referer': 'https://www.pollen.com/forecast/current/pollen/98908'}


class pollen:
    """get pollen"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="pollen", pass_context=True)
    async def pollen(self, ctx):
        await self.get_pollen()
        """Prints pollen zip"""

    async def get_pollen(self):
        async with ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                pollen = await response.json()
                pollen1 = pollen["Type"]["Location"]
                em = discord.Embed(title='', description=pollen1, colour=0x6FA8DC, )
                await self.bot.say(embed=em)
def setup(bot):
    bot.add_cog(pollen(bot))
