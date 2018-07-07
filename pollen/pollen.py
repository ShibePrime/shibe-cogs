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
                state = pollen["Location"]["State"]
                Yesterday = pollen["Location"]["periods"][0]["Index"]
                Today = pollen["Location"]["periods"][1]["Index"]
                Tomorrow = pollen["Location"]["periods"][2]["Index"]
                polleninfo = "**" + city + ", " + state + "\n"+ zip + "**\n" + \
                                "\n\n__**Pollen Index**__\n" + \
                                "***Yesterday: " + str(Yesterday) + "***\n" + \
                                "**Today: " + str(Today) + "**\n" + \
                                "***Tomorrow: " + str(Tomorrow) + "***\n"
                em = discord.Embed(title='', description=polleninfo, colour=0x0FFD966, )
                em.set_thumbnail(url="https://www.pollen.com/Content/images/Logo.png")
                em.set_author(name='Pollen Info', icon_url="https://www.gstatic.com/healthricherkp/pollen/icon_very_high_pollen.png",
                              url="http://db.destinytracker.com/d2/en")
                await self.bot.say(embed=em)

def setup(bot):
    bot.add_cog(pollen(bot))