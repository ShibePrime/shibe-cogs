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
        await self.fetch()

    async def fetch(self):
        async with ClientSession() as session:s
            async with session.post(url, data=json.dumps(payload), headers=headers) as response:
                data = await response.json()
                activities = data["data"]["activeMilestones"][0]["availableQuests"][0]["activities"]
                modifiers = activities["modifiers"]
                imageurl = data["data"]["activeMilestones"][0]["availableQuests"][0]["iconUrl"]
                nightfallInfo = "__**" +activities["activity"]["name"] + "**__\n" + \
                                activities["activity"]["description"] + "\n\n***Modifiers***\n" + \
                                "**"+modifiers[0]["name"] + ":**\n*" + modifiers[0]["description"] + "*\n" + \
                                "**"+modifiers[1]["name"] + ":**\n*" + modifiers[1]["description"] + "*"
                print(nightfallInfo)
                print(imageurl)
                em = discord.Embed(title='', description=nightfallInfo, colour=0xFFD966)
                em.set_author(name='Destiny Weekly Info', icon_url="https://cdn.thetrackernetwork.com/destiny//common/destiny2_content/icons/4de13648c3bf8741e773d8e7e8a0164b.png",url="http://db.destinytracker.com/d2/en")
                await self.bot.say(embed=em)


def setup(bot):
    bot.add_cog(ddb(bot))
