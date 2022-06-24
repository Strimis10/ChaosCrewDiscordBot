from discord import Embed
from discord.ext.commands import Bot, Cog
from discord_slash import cog_ext, SlashContext
from discord.ext import commands
import discord
import discord.utils
import json

class reddit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    #responds with the amount of clips in the clips.json file 
    @commands.command(name="clip-amount", alias="ca")
    async def clip_amount(self, ctx):
        with open("clips.json") as f:
            feeds = json.load(f)
        await ctx.send(len(feeds))
    
    #responds with the urls from the clips.json file
    @commands.command(name="clip-urls", alias="cus")
    async def clip_urls(self, ctx):
        with open("clips.json") as f:
            feeds = json.load(f)
        await ctx.send(feeds)


def setup(bot):
    bot.add_cog(reddit(bot))
