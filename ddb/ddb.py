import json

import discord
from aiohttp import ClientSession
from discord.ext import commands

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

    @commands.group(name="ddb", pass_context=True)
    async def _ddb(self, ctx):
        """gets db.destinytracker.com infos"""
        if ctx.invoked_subcommand is None:
            prefix = ctx.prefix
            title = '**.ddb gets info from db.destinytracker.com **'
            description = '__**Commands**__\n\n'
            description += '``{0}ddb nightfall`` gets the current nightfall information\n'
            em = discord.Embed(title=title, description=description.format(prefix), color=0xFFD966)
            em.set_footer(text='This cog was made by Shibe w/ help from Arrows pasta making class')
            em.set_author(name='Destiny Info', icon_url="https://i.imgur.com/8JDZzKM.png",
                          url="http://db.destinytracker.com/d2/en")
            em.set_thumbnail(url="https://i.imgur.com/TnBeVFO.png")
            await self.bot.say(embed=em)

    @_ddb.command(pass_context=True, name='nightfall', aliases=["nf"])
    async def nightfall(self, ctx):
        await self.get_nightfall()

    async def get_nightfall(self):
        async with ClientSession() as session:
            async with session.post(url, data=json.dumps(payload), headers=headers) as response:
                data = await response.json()
                activities = data["data"]["activeMilestones"][0]["availableQuests"][0]["activities"]
                modifiers = activities["modifiers"]
                challenges = activities["variants"]
                imageurl = data["data"]["activeMilestones"][0]["availableQuests"][0]["iconUrl"].replace(
                    'destiny//common', 'destiny/common')
                nightfallInfo = "__**" + activities["activity"]["name"] + "**__\n" + \
                                activities["activity"]["description"] + "\n\n***Modifiers***\n" + \
                                "**" + modifiers[0]["name"] + ":**\n*" + modifiers[0]["description"] + "*\n" + \
                                "**" + modifiers[1]["name"] + ":**\n*" + modifiers[1]["description"] + "*\n\n" 
                em = discord.Embed(title='', description=nightfallInfo, colour=0xFFD966, )
                em.set_thumbnail(url=imageurl)
                em.set_author(name='Destiny Info', icon_url="https://i.imgur.com/8JDZzKM.png",
                              url="http://db.destinytracker.com/d2/en")
                await self.bot.say(embed=em)


def setup(bot):
    bot.add_cog(ddb(bot))
