from discord.ext import commands
import discord
import discord.utils
import get_twitch_info
import asyncio

class meth(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        #runs every minute and checks if Kenny is live, if so it sends a command to my pc to start the "stream protocol" 
        #basically just opens a new tab in the browser and goes to the stream
        #
        #could be used for automated stream anouncements 
    @commands.Cog.listener()
    async def on_ready(self):
        live_before = False
        while True:
            if get_twitch_info.kenny_live() == True:
                if not live_before:
                    await self.bot.get_channel(949590152202813453).send(f"69Kennevo_is_live")
                    print("Kenny is live")
            
                
                live_before = True
            else:
                live_before = False
            await asyncio.sleep(60)

        #basically the same as the other one but it's manual
    @commands.command(name='Kenny_live',aliases=['KL'])
    async def Kenny_live(self, ctx):
        await self.bot.get_channel(949590152202813453).send(f"69Kennevo_is_live")
       
    


def setup(bot):
    bot.add_cog(meth(bot))