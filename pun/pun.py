import discord
from discord.ext import commands
import aiohttp

base_url = 'https://pun.andrewmacheret.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}


class pun:
    """pun"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="wowtoken", pass_context=True)
    async def pun(self, ctx):
        """Prints random pun """

        url = ''.join([base_url])

        await
        self.print_pun(url)

    async def print_pun(self, url):
        try:
            async with aiohttp.get(url, headers=headers) as response:
                pun = await
            response.text()
            em = discord.Embed(description=pun, colour=0xFFD966)
            await
            self.bot.say(embed=em)

        except:
            await
            self.bot.say("Error")


def setup(bot):
    bot.add_cog(pun(bot))
