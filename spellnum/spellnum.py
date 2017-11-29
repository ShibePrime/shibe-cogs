import json
import discord
from discord.ext import commands
from num2words import num2words


class spellnum:
    """Shows the word version of a number"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def spellnum(self, context):
        """spellnum"""
        spellnum=num2words(context, to='cardinal')
        await self.bot.say(spellnum)

def setup(bot):
    bot.add_cog(spellnum(bot))
