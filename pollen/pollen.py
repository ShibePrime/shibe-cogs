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

base_url = 'https://www.pollen.com/forecast/current/pollen/98908'
headers = {'User-Agent': 'Mozilla/5.0'}


class Pollen:

    """Much Pollen , very area , wow """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="pollen", pass_context=True)
    async def pollen(self, ctx):
        """how many pollen? """

        url = ''.join([base_url])

        await self.print_pollen(url)

    async def print_pollen(self, url):
        try:
            async with aiohttp.get(url, headers=headers) as response:
                soup = BeautifulSoup(await response.text(), "html.parser")

            html_notes = soup.find('div', {"class": "forecast-charts" , "id": "forecast-chart"})
            text_notes = pypandoc.convert_text(html_notes, 'plain',
                                               format='html',
                                               extra_args=['--wrap=none'])
#            text_notes = text_notes.replace('&nbsp;', ' ')
#            text_notes = text_notes.replace('&apos;', "'")
#this is the only way I know howto cleanup the formatting. pls halp @TheRealShibe
#            text_notes = text_notes.replace('+', "")
#            text_notes = text_notes.replace('-', "")
#            text_notes = text_notes.replace('-', "")
#            text_notes = text_notes.replace('|', '')
#            text_notes = text_notes.replace("Buy Price", "Buy Price \n")
#            text_notes = text_notes.replace("24Hour Range", "24Hour Range \n")
#            text_notes = text_notes.replace("API Result", "API Result \n")
#            text_notes = text_notes.replace("Updated", "Updated \n")
            em = discord.Embed(title='Pollen', description=text_notes, colour=0xFFD966)
            await self.bot.say(embed=em)

        except:
            await self.bot.say("Error")


def setup(bot):
    if soup_available and pypandoc_available:
        bot.add_cog(pollen(bot))
    else:
        if not soup_available:
            error_text += "You need to run `pip install beautifulsoup4`\n"
        if not pypandoc_available:
            error_text += "You need to run `pip install pypandoc`\n"
        raise RuntimeError(error_text)
