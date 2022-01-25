from ast import alias
from discord.ext import commands
import discord
import discord.utils
import json
import os
import random


class EightBall(commands.Cog):
    def init(self, bot):
        self.bot = bot

    @commands.command(name='8ball', aliases = ["EightBall"])
    async def EightBall(self, ctx):
        with open("EightBall.json") as f:
            data =json.load(f)
        
        await ctx.send(random.choice(data))


def setup(bot):
    bot.add_cog(EightBall(bot))
