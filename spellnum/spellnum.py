from num2words import num2words
from discord.ext import commands


class spellnum:
    """Shows the word of a number"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def spellnum(self, context):
        """spellnum"""
        wordnum = num2words(1, 'sigfig',3, 'trz',false)
        await self.bot.say(wordnum)


def setup(bot):
    bot.add_cog(spellnum(bot))
