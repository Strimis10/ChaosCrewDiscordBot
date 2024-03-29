import json
from discord.ext import commands
import discord
import discord.utils
from typing import Optional
import asyncio
import time


class inactive(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    #removes all of the "inactive" roles from a user whenever they send a message
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id != 932687176997687316:
            try:
                with open("jsons/user_info.json") as feedsjson: 
                    data = json.load(feedsjson)
                data[str(message.author.id)]["last_active(days)"] = 0
                with open("jsons/user_info.json", mode='w') as f:
                    f.write(json.dumps(data, indent=2)) 
                guild= discord.utils.get(self.bot.guilds, id=int(932684556572700773))
                member = guild.get_member(int(message.author.id))
                one_month = discord.utils.get(guild.roles, id=int(961226882534236161)) 
                three_months = discord.utils.get(guild.roles, id=int(961529848369659914)) 
                six_months = discord.utils.get(guild.roles, id=int(961530872933257246)) 
                one_year = discord.utils.get(guild.roles, id=int(961531454460944406))
                two_years_or_more = discord.utils.get(guild.roles, id=int(961531735500288062))  
                member = guild.get_member(int(message.author.id))
                await member.remove_roles(one_month)
                await member.remove_roles(three_months)
                await member.remove_roles(six_months)
                await member.remove_roles(one_year)
                await member.remove_roles(two_years_or_more)
            except:
                pass
            


        #command to see how long a user has been inactive
    @commands.command(name = 'inactive',aliases=["Inactive", "INACTIVE", "iNACTIVE"],brief='"?Inactive @Strimis10" informs you of how long a user has been inactive in this server: ')
    async def inactive(self, ctx, target: Optional[discord.Member]):
        target = target or ctx.author
        with open("jsons/user_info.json") as feedsjson: 
            feeds = json.load(feedsjson)
        if target == None:
            await ctx.send("Please specify a valid user")
        else:
            name = target.name
            target_id = str(target.id)
            try:
                await ctx.send(f"{name} was last active {feeds[target_id]['last_active(days)']} days ago")
            
            except KeyError:
                await ctx.send(f"{name} has not sent a message in this server")

        
      


def setup(bot):
    bot.add_cog(inactive(bot))