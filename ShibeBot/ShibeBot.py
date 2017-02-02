# noinspection PyUnresolvedReferences
import discord
from discord.ext import commands

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
        data = "Click To Connect to Mandrew ARK"
        "steam://connect/71.93.28.250:27015"
        "Whisper a Doge Master for the password"
        "NOTE: If it's your first time, You'll have to reconnect multiple times until all the mods are loaded. You can track workshop content download progress in your steam client inbetween reconnects"
        await self.bot.say(embed=data)

def setup(bot):
    n = Shibe(bot)
    bot.add_cog(n)
