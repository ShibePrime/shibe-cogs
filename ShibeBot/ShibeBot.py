# noinspection PyUnresolvedReferences
import discord
import random
from discord.ext import commands
from cogs.utils import checks
from cogs.utils.chat_formatting import box,  pagify, escape_mass_mentions
from random import choice, randint
import xkcd


__author__ = "shibe "

class Shibe:
    """Shibe's Commands"""

    def __init__(self, bot):
        self.bot = bot
        self.base = 'data/shibebot/'

    @commands.command(pass_context=True)
    async def yoshi(self, context):
        """YOSHI"""
        await self.bot.send_file(context.message.channel, '{}images/yoshi.png'.format(self.base))

    @commands.command(pass_context=True)
    async def shibe(self, context):
        """SHIBE"""
        await self.bot.send_file(context.message.channel, '{}images/shibe.png'.format(self.base))

    @commands.command()
    async def suh(self):
        """suh dude"""
        await self.bot.say(" :v: SUH DUDE :v: ")

    @commands.command()
    async def ark(self):
        """Get's link for Mandrew ARK"""
        em = discord.Embed(title='Click To Connect to Mandrew ARK', description='steam://connect/71.93.28.250:27015 \n Whisper a Doge Master for the password \n\n NOTE: If it\'s your first time, You\'ll have to reconnect multiple times until all the mods are loaded. You can track workshop content download progress in your steam client in between reconnects', colour=0xDEADBF)
        em.set_author(name='ShibeBot', icon_url='http://i.imgur.com/mYdLixs.png')
        await self.bot.say(embed=em)

    @commands.command()
    async def piefact(self):
        """100 Percent PieFacts"""
        lines = open('{}/piefacts/piefacts.txt'.format(self.base)).read().splitlines()
        piefact = random.choice(lines)
        await self.bot.say(piefact)

            @commands.group(name="xkcd", pass_context=True)
    async def xkcd(self, ctx):
        """Displays latest xkcd comic."""
        if ctx.invoked_subcommand is None:
            await self.bot.say(xkcd.getLatestComic().getImageLink())

    @xkcd.command(name="random", pass_context=True)
    async def _random(self, ctx):
        """Displays random xkcd comic."""
        await self.bot.say(xkcd.getRandomComic().getImageLink())

    @xkcd.command(name="number", pass_context=True)
    async def _number(self, ctx, number: int):
        """Displays specified xkcd comic."""
        await self.bot.say(xkcd.getComic(number).getImageLink())


def setup(bot):
    n = Shibe(bot)
    bot.add_cog(n)
