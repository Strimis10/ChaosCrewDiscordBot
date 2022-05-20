from discord.ext import commands
import discord
import discord.utils
import json
import random
from discord_slash import cog_ext, SlashContext 
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option

class EightBall(commands.Cog):
    def init(self, bot):
        self.bot = bot
        #I think this one is self explanatory
    #@commands.command(name='8ball', aliases = ["EightBall"])
    @cog_ext.cog_slash(
        name="8ball", 
        description="",
        guild_ids=[932684556572700773,786013884216639509])
    async def EightBall(self, ctx):
        with open("EightBall.json") as f:
            data =json.load(f)
        
        await ctx.send(random.choice(data))


def setup(bot):
    bot.add_cog(EightBall(bot))
