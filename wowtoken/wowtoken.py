import discord
from discord.ext import commands
from .utils.chat_formatting import pagify
import aiohttp

try:  # check if BeautifulSoup4 is installed
    from bs4 import BeautifulSoup
    soup_available = True
except:
    soup_available = False

try:  # check if pypandoc is installed
    import pypandoc
    pypandoc_available = True
except:
    pypandoc_available = False

# Special thanks to judge2020 for telling me about pandoc, and offering their
# code as a reference: https://github.com/judge2020/BattleNetUpdateChecker

# This cog requires:
# BeautifulSoup4 :: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# pypandoc :: https://pypi.python.org/pypi/pypandoc
# Pandoc :: http://pandoc.org/

base_url = 'https://wowtoken.info/'
headers = {'User-Agent': 'Battle.net/1.0.8.4217'}


class WoWToken:

    """WoW Token Price"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="wowtoken", pass_context=True)
    async def wowtoken(self, ctx):
        """Prints latest NA wowtoken price """

        url = ''.join([base_url])

        await self.print_patch_notes(url)

    async def print_patch_notes(self, url):
        try:
            async with aiohttp.get(url, headers=headers) as response:
                soup = BeautifulSoup(await response.text(), "html.parser")

            html_notes = soup.find('div', {"class": "mui-panel realm-panel" , "id": "na-panel"})
            text_notes = pypandoc.convert_text(html_notes, 'plain',
                                               format='html',
                                               extra_args=['--wrap=none'])
            text_notes = text_notes.replace('&nbsp;', ' ')
            text_notes = text_notes.replace('&apos;', "'")
            text_notes = text_notes.replace('+', "")
            text_notes = text_notes.replace('-', "")
            em = discord.Embed(title='WoW Token Info', description=text_notes, colour=0xFFD966)
            em.set_author(name='ShibeBot', icon_url='https://pbs.twimg.com/profile_images/586731244467150849/U4TyFhW8.jpg')
            await self.bot.say(embed=em)

        except:
            await self.bot.say("Error")


def setup(bot):
    if soup_available and pypandoc_available:
        bot.add_cog(WoWToken(bot))
    else:
        if not soup_available:
            error_text += "You need to run `pip install beautifulsoup4`\n"
        if not pypandoc_available:
            error_text += "You need to run `pip install pypandoc`\n"
        raise RuntimeError(error_text)
