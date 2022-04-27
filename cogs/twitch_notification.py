from discord.ext import commands
import discord
import discord.utils
from get_twitch_info import kenny_live
import time

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #while True:
    #    if kenny_live() == True:
    #        #await self.bot.get_channel(949590152202813453).send(f"69Feed_Strimis: requested by: {ctx.author} (:{ctx.author.id}:) channel.id :{ctx.channel.id}")
    #    
    #        print("Kenny is live")
    #        time.sleep(10)
    #    else:
    #        print("Kenny is not live")
    #        time.sleep(10)
        #                         ^^ This is for pings / mentions being cleaned so you can't do `a!say @everyone`.
        #command content


def setup(bot):
    bot.add_cog(fun(bot))