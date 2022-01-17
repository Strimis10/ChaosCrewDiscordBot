import discord
from discord import client
from discord.ext import commands
import asyncio
import random
import os

from discord.ext.commands import bot


class Harry(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot




def setup(bot:commands.Bot):
    bot.add_cog(Harry(bot))