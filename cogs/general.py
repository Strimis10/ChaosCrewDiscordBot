from discord.ext import commands
import discord
import discord.utils
import json
from typing import Optional
from discord_slash import cog_ext, SlashContext 
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option

class general(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    #adds all users to the user_info.json file
    @commands.Cog.listener()
    async def on_ready(self):
        for member in self.bot.get_all_members():
            if member.bot == False:
                with open("user_info.json") as oj: 
                    feeds = json.load(oj)
                if str(member.id) not in feeds:
                    print(f"Added {member.name} to the user_info.json file")
                    
                    feeds[member.id] = {"new":420.69}
                    with open("user_info.json", mode='w') as f:
                        f.write(json.dumps(feeds, indent=2))
                    with open("user_info.json") as oj: 
                        feeds = json.load(oj)
                    feeds[str(member.id)]["name"] = member.name
                    feeds[str(member.id)]["id"] = member.id
                    feeds[str(member.id)]["word_immunity"] = False
                    with open("user_info.json", mode='w') as f:
                        f.write(json.dumps(feeds, indent=2))
    
        #command to see what job EEVEE thought a user had
    #@commands.command(name='what_job', aliases=["wj"],breif="sends what EEVEE thinks peoples jobs are ")
    @cog_ext.cog_slash(
        name="what_job", 
        description="What job does eevee think <user> has?",
        guild_ids=[932684556572700773,786013884216639509,983015288910000188])
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
    bot.add_cog(general(bot))
    
    
    