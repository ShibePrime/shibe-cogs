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

base_url = 'http://db.destinytracker.com/d2/en'
headers = { ":authority": "db-api.destinytracker.com",
            ":method": "POST",
            ":path": "/api/graphql",
            "content-type": "application/json",
            "referer": "http://db.destinytracker.com/d2/en",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
}
payload = {"query":"query GetMilestones($types: [MilestoneType]) {\n  activeMilestones(types: $types) {\n    hash\n    name\n    description\n    iconUrl\n    hasPredicatableDates\n    startDate\n    endDate\n    availableQuests {\n      name\n      description\n      iconUrl\n      overrideImage\n      quest {\n        name\n        description\n        __typename\n      }\n      activities {\n        activity {\n          name\n          description\n          pgcrImageUrl\n          __typename\n        }\n        modifiers {\n          name\n          description\n          iconUrl\n          __typename\n        }\n        variants {\n          activity {\n            level\n            __typename\n          }\n          challenges {\n            name\n            description\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n","variables":{"types":["Weekly","Daily"]},"operationName":"GetMilestones"}


class ddb:

    """db.destinytracker.com """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ddb", pass_context=True)
    async def ddb(self, ctx):
        """Scrapes db.destinytracker.com for infos"""

        url = ''.join([base_url])

        await self.print_notes(url)

    async def print_notes(self, url):
        try:
            async with aiohttp.post(url, json=payload, headers=headers) as response:
                soup = BeautifulSoup(await response.text(), "html.parser")

            html_notes = soup.find('div', {"class": "home-page"})
            text_notes = pypandoc.convert_text(html_notes, 'plain',
                                               format='html',
                                               extra_args=['--wrap=none'])
#            text_notes = text_notes.replace('&nbsp;', ' ')
#            text_notes = text_notes.replace('&apos;', "'")
#this is the only way I know howto cleanup the formatting. pls halp @TheRealShibe
#           text_notes = text_notes.replace('+', "")
#            text_notes = text_notes.replace('-', "")
#            text_notes = text_notes.replace('-', "")
#            text_notes = text_notes.replace('|', '')
#            text_notes = text_notes.replace("Buy Price", "Buy Price \n")
#            text_notes = text_notes.replace("24Hour Range", "24Hour Range \n")
#            text_notes = text_notes.replace("API Result", "API Result \n")
#            text_notes = text_notes.replace("Updated", "Updated \n")
            em = discord.Embed(title='Destiny Weekly Info', description=text_notes, colour=0xFFD966)
            await self.bot.say(embed=em)

        except:
            await self.bot.say("Error")


def setup(bot):
    if soup_available and pypandoc_available:
        bot.add_cog(ddb(bot))
    else:
        if not soup_available:
            error_text += "You need to run `pip install beautifulsoup4`\n"
        if not pypandoc_available:
            error_text += "You need to run `pip install pypandoc`\n"
        raise RuntimeError(error_text)
