from discord.ext import tasks, commands
import discord
import discord.utils
import json
import requests
import os 
from twitchAPI import Twitch
from discord.utils import get


class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='nope',description='bot says [text]',brief='bot says [text]')
    async def nope(self, ctx, *, text: commands.clean_content = ''):
        print("")
        #                         ^^ This is for pings / mentions being cleaned so you can't do `a!say @everyone`.
        #command content


def setup(bot):
    bot.add_cog(fun(bot))