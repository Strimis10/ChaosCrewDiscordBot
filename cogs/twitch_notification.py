from discord.ext import commands
import discord
import discord.utils
from get_twitch_info import kenny_live
import time

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        while True:
            if kenny_live() == True:
                await self.bot.get_channel(949590152202813453).send(f"69Kennevo_is_live")
            
                print("Kenny is live")
                
            #sleep for three minutes
            time.sleep(180)
        


def setup(bot):
    bot.add_cog(fun(bot))