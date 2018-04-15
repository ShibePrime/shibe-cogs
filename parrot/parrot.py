import pathlib
import asyncio  # noqa: F401
import discord
from discord.ext import commands
from cogs.utils.dataIO import dataIO
from cogs.utils import checks
from datetime import datetime

path = 'data/parrot'

class parrot:
    """Waterfall Convo Repeat and Join"""

    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="parrot", pass_context=True)
    async def parrot(self, ctx, name: str):
        """Interactive prompt for making a raid"""
        author = ctx.message.author
        server = ctx.message.server

        await self.bot.say("I will message you to continue.")
        await self.contact_for_parrot(name, author, server)

    async def contact_for_parrot(self, name: str, author, server=None):

        dm = await self.bot.send_message(author,
                                         "Please respond to this message "
                                         "with the title of your embed. If "
                                         "you do not want a title, wait 30s")
        title = await self.bot.wait_for_message(channel=dm.channel,
                                                author=author, timeout=30)

        if title is None:
            await self.bot.send_message(author,
                                        "Okay, this one won't have a title.")

        dm = await self.bot.send_message(author,
                                         "Please respond to this message "
                                         "with the content of your embed")
        message = await self.bot.wait_for_message(channel=dm.channel,
                                                  author=author, timeout=120)

        if message is None:
            if server is not None:
                self.settings[server.id]['usercache'].remove(author.id)
            else:
                self.settings['global']['usercache'].remove(author.id)
            self.save_settings()
            return await self.bot.send_message(author,
                                               "I can't wait forever, "
                                               "try again when ready")
        else:
            await self.bot.say(name, title, message, server)
            await self.bot.send_message(author, "Your raid was created")

def setup(bot):
    bot.add_cog(parrot(bot))
