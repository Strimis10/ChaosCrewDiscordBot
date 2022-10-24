from discord.ext import commands
import discord
import discord.utils
from threading import Thread
import os

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='startAPI',description='bot says [text]',brief='bot says [text]')
    @commands.is_owner()
    async def say(self, ctx, *, text: commands.clean_content = ''):
        def func2():
            print("Starting API")
            os.system("python3 api/main.py")

        t2 = Thread(target=func2)

        t2.start()
        await ctx.send("API running")
        #                         ^^ This is for pings / mentions being cleaned so you can't do `a!say @everyone`.
        #command content


def setup(bot):
    bot.add_cog(fun(bot))




