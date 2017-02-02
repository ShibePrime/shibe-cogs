# noinspection PyUnresolvedReferences
import discord
from discord.ext import commands
from cogs.utils import checks
from cogs.utils.chat_formatting import box,  pagify, escape_mass_mentions
from random import choice, randint
import datetime

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
        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)

        randnum = randint(1, 10)
        empty = u"\u2063"
        emptyrand = empty * randnum

        data = discord.Embed(
            "Click To Connect to Mandrew ARK"
            "steam://connect/71.93.28.250:27015"
            "Whisper a Doge Master for the password"
            "NOTE: If it's your first time, You'll have to reconnect multiple times until all the mods are loaded. You can track workshop content download progress in your steam client inbetween reconnects"), colour=discord.Colour(value=colour)

        if ctx.message.author.avatar_url:
            data.set_author(name=ctx.message.author.name,
                            url=ctx.message.author.avatar_url, icon_url=ctx.message.author.avatar_url)
        else:
            data.set_author(name=ctx.message.author.name)

        try:
            await self.bot.say(emptyrand, embed=data)
        except:
            await self.bot.say("I need the `Embed links` permission to send this")

def setup(bot):
    n = Shibe(bot)
    bot.add_cog(n)
