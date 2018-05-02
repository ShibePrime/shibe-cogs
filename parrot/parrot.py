import pathlib
import asyncio  # noqa: F401
import discord
from discord.ext import commands
from cogs.utils.dataIO import dataIO
from cogs.utils import checks
from datetime import datetime

path = 'data/parrot'


class parrot:
    """Waterfall Convo Parrot"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="parrot", pass_context=True)
    async def parrot(self, ctx, game: str):
        """Interactive prompt for making a raid, Do something like .parrot WoW or .parrot destiny to get started """
        author = ctx.message.author
        server = ctx.message.server

        await self.bot.say("I will message you to continue.")
        await self.contact_for_parrot(game, author, server)

    async def contact_for_parrot(self, game: str, author, server=None):

        dm = await self.bot.send_message(author,
                                  "Please respond to this message "
                                  "with the details of your raid.\r\n If "
                                  "you do not want a details, wait 30s\r\n\n"
                                  "Ex: `Prestige Argos` ; `WoW Mythics` ; `LFR`")

        desc = await self.bot.wait_for_message(channel=dm.channel,
                                      author=author, timeout=30)

        if desc is None:

            await self.bot.send_message(author,
                                  "Okay, this one won't have a description.")

        dm = await self.bot.send_message(author,
                                  "what day? Follow the example format. `MM/DD/YY` "
                                  "Ex: `12/25/17`")

        day = await self.bot.wait_for_message(channel=dm.channel,
                                  author=author, timeout=30)
        if day is None:
            return await self.bot.send_message(author,
                                  "I can't wait forever, "
                                  "try again when ready")

        dm = await self.bot.send_message(author,
                                  "what time? Follow the example format. `H:MA` "
                                  "Ex: `8:00PM` or `11:00AM`")

        time = await self.bot.wait_for_message(channel=dm.channel,
                                  author=author, timeout=30)
        if time is None:
            return await self.bot.send_message(author,
                                  "I can't wait forever, "
                                  "try again when ready")

        dm = await self.bot.send_message(author,
                                  "what time zone?"
                                  "Ex: `PST` , `EST` etc. ")

        zone = await self.bot.wait_for_message(channel=dm.channel,
                                  author=author, timeout=30)
        if zone is None:
            return await self.bot.send_message(author,
                                  "I can't wait forever, "
                                  "try again when ready")
        else:
            jointime = " ".join((day.content, time.content))
            e = discord.Embed(colour=discord.Colour.red())
            e.title = "You've created a raid!"
            e.add_field(name="Game:", value=game, inline=False)
            e.add_field(name="Time:", value=jointime + " " + zone.content, inline=False)
            e.add_field(name="Description:", value=desc.content, inline=False)
            e.add_field(name="Note:", value="Go do .raid list in a relevant game channel to see the raids available , tell your friends to .raid join #(the number next to your raid)", inline=False)
            await self.bot.send_message(author, time.content)
            await self.bot.send_message(author, zone.content)
            await self.bot.send_message(author, day.content)
            await self.bot.send_message(author, jointime + zone.content)
            await self.bot.send_message(author, embed=e)



def setup(bot):
    bot.add_cog(parrot(bot))
