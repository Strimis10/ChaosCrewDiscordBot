from discord.ext import tasks, commands
import discord
import discord.utils
import time

class live(commands.Cog):
    def __init__(self, bot):
        self.can_run = True
        self.has_run = True
        self.bot = bot
        self.index = 0
        self.printer.start()
        

    @tasks.loop(hours=24)
    async def printer(self):
        self.index += 1
        self.can_run = True 

    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == 932708048856838184 and message.author.id != 932687176997687316:
            self.can_run = False
            print("eeeee")
            await message.channel.send("Hello")




def setup(bot):
    bot.add_cog(live(bot))
