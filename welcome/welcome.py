import discord
import datetime
from cogs.utils import checks
from discord.ext import commands

class welcome:
    """PM People Using The Bot"""
    def __init__(self, bot):
        self.bot = bot
        msg = '*Hello, this is doge!* :wolf:\r\nI\'m here to inform you of the new role you\'ve been granted by the mighty doges of the Thunderdoge.\r\nMuch congrats!\r\nNow that you\'re officially part of the pack you can use bot commands in `#botplayground` to assign yourself roles and join game specific text channels.\r\nVisit the `#announcements` text channel under the \"General Text Chat\" category to view these roles\/commands.\r\nThank you for joining us!\r\nIf you need help with anything, please bork in the `#halp_pls` channel or bork at a DogeMaster\/DogeMod\r\nWelcome to the Thunderdoge!'

    @commands.command(pass_context=True)
    @checks.is_owner()
    async def welcome(self, ctx, user_id: str):
        """Sends a user the welcome message after a manual promote to DOGE"""
        user = await self.bot.get_user_info(id)
        try:
            e = discord.Embed(colour=discord.Colour.red())
            e.title = "You've recieved a message from a DogeMod!"
            e.add_field(name="Time:", value=datetime.datetime.now().strftime("%A, %B %-d %Y at %-I:%M%p").replace("PM", "pm").replace("AM", "am"), inline=False)
            e.add_field(name="Message:", value=msg, inline=False)
            e.set_thumbnail(url=ctx.message.author.avatar_url)
            await self.bot.send_message(user, embed=e)
        except:
            await self.bot.say(':x: Failed to send message to user_id `{}`.'.format(user_id))
        else:
            await self.bot.say('Succesfully sent message to {}'.format(user_id))

def setup(bot):
    bot.remove_command('welcome')
    n = welcome(bot)
    bot.add_cog(n)
