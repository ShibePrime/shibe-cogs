import json
import discord
from aiohttp import ClientSession
from discord.ext import commands

url = 'https://www.pollen.com/api/forecast/current/pollen/'
headers = {'Content-Type': 'application/json; charset=utf-8','Referer': 'https://www.pollen.com','User-Agent': 'ShibeBot'}


class pollen:
    """get pollen"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="pollen")
    async def pollen(self,zip):
        await self.get_pollen(zip)
        """Prints pollen"""

    async def get_pollen(self,zip):
        async with ClientSession() as session:
            async with session.get(url + str(zip), headers=headers) as response:
                pollen = await response.json()
#                em = discord.Embed(title='', description=pollenstr, colour=0x6FA8DC, )
                zip = pollen["Location"]["ZIP"]
                city = pollen["Location"]["City"]
                state = pollen["Location"]["WA"]
                await self.bot.say(zip)
                await self.bot.say(city)
                await self.bot.say(state)

def setup(bot):
    bot.add_cog(pollen(bot))