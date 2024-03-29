# Bot.py

import discord
from discord.ext import commands
from isbnlib import *
from dotenv import *
import requests
from bs4 import BeautifulSoup
import time
import itertools


ROLE = ""
buzzfeed_urls_dict = {"URL": [], "Category": []};

class Bot(commands.Cog):
    """ a class filled with all commands related to the bot. """

    def __init__(self, client):
        self.client = client
        
    # Searches for quizzes (generic search that is similar to setquiz).
    # @commands.command()
    # async def quizsearch(self, ctx):
    #     await ctx.send(f'{ctx.author.mention}, what\'s the quiz called?')

    #     def check(message):
    #         return message.channel == ctx.channel

    #     try:
    #         current_message = await self.client.wait_for('message', check=check, timeout=30)
    #         quiz_results = goom(current_message.content)
    #         if quiz_results:
    #             quiz_results_count = len(quiz_results)
    #             embed = discord.Embed(color=0xf5ddb9, title="Quiz Results:")
    #             i = 1
    #             while i < quiz_results_count:
    #                 for quiz in quiz_results:
    #                     if len(quiz['Authors']) == 0:
    #                         embed.add_field(name='{}. {} ({})'.format(i, quiz['Title'], quiz['Year']),
    #                                         value='No Authors Specified', inline=False)
    #                     else:
    #                         embed.add_field(name='{}. {} ({})'.format(i, quiz['Title'], quiz['Year']),
    #                                         value=', '.join(quiz['Authors']), inline=False)
    #                     i += 1
    #             embed.set_footer(
    #                 text="{} quizzes found!\nCouldn't find the quiz? Try again but with more precision 😉".format(
    #                     quiz_results_count))
    #             await ctx.send(embed=embed)
    #         else:
    #             await ctx.send("I couldn't find any quizzes. ¯\\_(ツ)_/¯")
    #     except asyncio.TimeoutError as e:
    #         print(e)
    #         await ctx.send("Response timed out.")

    @commands.command()
    async def random_quiz(self, ctx):
        print("Here's a quiz.")


    @commands.command()
    async def post_quiz(self, ctx):
        url = 'https://www.buzzfeed.com/uk/quizzes/'
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        

        for link in soup.find_all('a'):
            if ("quiz" in str(link.get('href'))) and ("quizzes" not in str(link.get('href'))):
                buzzfeed_urls_dict["URL"].append(str(link.get('href')))
                await ctx.send(str(link.get('href')))
                # for div in soup.findAll('div', {'class': 'value'}):
                #     buzzfeed_urls_dict["Category"].append(div.find('a').attrs['class'][0].text.strip())
                #     await ctx.send(div.find('a').attrs['class'][0].text.strip())
                            

        # Remember to @ the Quiz Tag.
        
    #######   TROUBLESHOOTING AND INFORMATION ########


    # Returns information about bot.
    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(title='QuizQuetzal (Bot)', url='https://github.com/Iqrahaq/QuizQuetzal',
                                description='A bot that generates various personality quizzes', color=0xf5ddb9)
        embed.set_author(name='Iqra Haq', url='https://www.iqrahaq.com')
        embed.set_thumbnail(url='https://raw.githubusercontent.com/Iqrahaq/QuizQuetzal/main/img/quetzal_square.jpg')
        embed.add_field(name='How to use?', value='Use the "qq!help" command!', inline=False)
        await ctx.send(embed=embed)
        


    # Ping to answer with the ms latency, helpful for troubleshooting.
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms ')



    # Help list and details of commands...
    @commands.command(pass_context=True)
    async def help(self, ctx):
        embed = discord.Embed(color=0xf5ddb9)
        embed.set_author(name='Help - List of commands available: ')
        embed.add_field(name='qq!ping', value='Returns my response time in milliseconds.', inline=False)
        embed.add_field(name='qq!info', value='Returns information about me.', inline=False)
        embed.set_thumbnail(url='https://raw.githubusercontent.com/Iqrahaq/QuizQuetzal/main/img/quetzal_square.jpg')
        embed.set_footer(text="© Iqra Haq (BuraWolf#1158)")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Bot(client))


