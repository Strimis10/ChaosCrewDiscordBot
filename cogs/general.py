from discord.ext import commands
import discord
import discord.utils
import json
from typing import Optional
from discord_slash import cog_ext, SlashContext 
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from matplotlib.pyplot import text

class general(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    #adds all users to the user_info.json file
    @commands.command(name = 'update_user_info')
    async def on_ready(self, ctx):
        for member in self.bot.get_all_members():
            if member.bot == False:
                with open("jsons/user_info.json") as oj: 
                    feeds = json.load(oj)
                if str(member.id) not in feeds:
                    print(f"Added {member.name} to the user_info.json file")
                    
                    feeds[member.id] = {"new":420.69}
                    with open("jsons/user_info.json", mode='w') as f:
                        f.write(json.dumps(feeds, indent=2))
                    with open("jsons/user_info.json") as oj: 
                        feeds = json.load(oj)
                    feeds[str(member.id)]["name"] = member.name
                    feeds[str(member.id)]["id"] = member.id
                    feeds[str(member.id)]["last_active(days)"] = 0
                    feeds[str(member.id)]["Timezone"] = []
                    with open("jsons/user_info.json", mode='w') as f:
                        f.write(json.dumps(feeds, indent=2))
        print("Done")
  
    @cog_ext.cog_slash(
        name="what_job", 
        description="What job does eevee think <user> has?",
        guild_ids=[932684556572700773,786013884216639509,983015288910000188])
    async def say(self, ctx, target: Optional[discord.Member]):
        target = target or ctx.author
        with open("jsons/jobs.json") as feedsjson: 
            feeds = json.load(feedsjson)
        name = target.name
        target_id = str(target.id)
        try:
            await ctx.send(f"{name}'s job is: {feeds[target_id]}")
        
        except KeyError:
            await ctx.send(f"EEVEE has not guessed {name}'s job yet")


    @commands.command(name='say',description='bot says [text]',brief='bot says [text]')
    async def say(self, ctx, *, text: commands.clean_content = ''):
        #                         ^^ This is for pings / mentions being cleaned so you can't do `a!say @everyone`.
        if text == '':
            await ctx.send("You need to say something")
        else:
            await ctx.send(f"{ctx.author.mention} says: {text}")
            await ctx.message.delete()


        ##command to give DAVE the bot role but is missing perms
    # @commands.command(name='ups')
    # async def ups(self, ctx):
    #     guild= discord.utils.get(self.bot.guilds, id=int(786013884216639509))
    #     role = discord.utils.get(guild.roles, id=int(803745819869839393))
    #     member = guild.get_member(932687176997687316)
    #     await member.add_roles(role)



    


def setup(bot):
    bot.add_cog(general(bot))
    
    
    