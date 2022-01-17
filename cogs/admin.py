import discord
from discord import client
from discord.ext import commands
import asyncio
import random
import os

from discord.ext.commands import bot


class admin(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.command(name = "die")
    @commands.is_owner()
    async def die(self, ctx):
        await ctx.send("damn bro didn\'t need to be like this \n<\\3")
        await bot.close()


def setup(bot:commands.Bot):
    bot.add_cog(admin(bot))