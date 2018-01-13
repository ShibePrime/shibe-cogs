import json
import discord
from aiohttp import ClientSession
from discord.ext import commands

url = 'https://pun.andrewmacheret.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}


class pun:
    """Random Puns"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="pun", pass_context=True)
    async def pun(self, ctx):
        await self.get_pun()
        """Prints Random Puns"""

    async def get_pun(self):
        async with ClientSession() as session:
            async with session.post(url, headers=headers) as response:
                data = await response.json()
                pun = data[0]
                imageurl = 'https://i.pinimg.com/originals/28/c1/1c/28c11c84de44f79450c8794849d02ab5.jpg'
                pun = "__**" + pun[0] + "**__"
                em = discord.Embed(title='', description=pun, colour=0xFFD966, )
                em.set_thumbnail(url=imageurl)
                em.set_author(name='ShibeBot The Pun Lord')
                await self.bot.say(embed=em)

def setup(bot):
    bot.add_cog(pun(bot))
