from discord.ext import commands
import discord
from typing import Optional
import discord.utils
import json

class job(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='what_job', aliases=["wj"],breif="sends what EEVEE thinks peoples jobs are ")
    async def say(self, ctx, target: Optional[discord.Member]):
        target = target or ctx.author
        with open("jobs.json") as feedsjson: 
            feeds = json.load(feedsjson)
        name = target.name
        target_id = str(target.id)
        try:
            await ctx.send(f"{name}'s job is: {feeds[target_id]}")
        
        except KeyError:
            await ctx.send(f"EEVEE has not guessed {name}'s job yet")

        


def setup(bot):
    bot.add_cog(job(bot))