import discord
import json
from discord.ext import commands
from .utils.chat_formatting import pagify
from aiohttp import ClientSession
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

#:authority:db-api.destinytracker.com
# :method:POST
# :path:/api/graphql
# :scheme:https
# accept:/
# accept-encoding:gzip, deflate, br
# accept-language:en
# cache-control:no-cache
# content-length:1004
# content-type:application/json
# origin:http://db.destinytracker.com
# pragma:no-cache
# referer:http://db.destinytracker.com/d2/en
# user-agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36

url = 'https://db-api.destinytracker.com/api/graphql'
headers = {"authority": "db-api.destinytracker.com",
           "accept": "*/*",
           "accept-encoding": "gzip, deflate, br",
           "accept-language": "en",
           "cache-control": "no-cache",
           "content-type": "application/json",
           "origin": "http://db.destinytracker.com",
           "referer": "http://db.destinytracker.com/d2/en",
           "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
           }
payload = {
    "query": "query GetMilestones($types: [MilestoneType]) {\n  activeMilestones(types: $types) {\n    hash\n    name\n    description\n    iconUrl\n    hasPredicatableDates\n    startDate\n    endDate\n    availableQuests {\n      name\n      description\n      iconUrl\n      overrideImage\n      quest {\n        name\n        description\n        __typename\n      }\n      activities {\n        activity {\n          name\n          description\n          pgcrImageUrl\n          __typename\n        }\n        modifiers {\n          name\n          description\n          iconUrl\n          __typename\n        }\n        variants {\n          activity {\n            level\n            __typename\n          }\n          challenges {\n            name\n            description\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",
    "variables": {"types": ["Weekly", "Daily"]},
    "operationName": "GetMilestones"
}



class ddb:
    """db.destinytracker.com """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ddb", pass_context=True)
    async def ddb(self, ctx):
        """Scrapes db.destinytracker.com for infos"""
        await self.print_notes()

    async def fetch(self):
        async with ClientSession() as session:
            async with session.post(url, data=json.dumps(payload), headers=headers) as response:
                results = await response.text()
                em = discord.Embed(title='Destiny Weekly Info', description=results[1], colour=0xFFD966)
                await self.bot.say(embed=em)

    async def print_notes(self):
        try:
            await self.fetch()
        except:
            await self.bot.say("Error")


def setup(bot):
    bot.add_cog(ddb(bot))
