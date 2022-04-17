from discord.ext import tasks, commands
import discord
import discord.utils
import time

terms = ["good morning"]
terms2 = ["good night"]

class good_morning(commands.Cog):
    def __init__(self, bot):
        self.can_run = True
        self.has_run = True
        self.bot = bot
        self.index = 0
        self.printer.start()




    @tasks.loop(hours=1)
    async def printer(self):
        self.index += 1
        global can_run
        if self.has_run == True:
            self.can_run = True

        else:
            self.can_run = True
            self.has_run = True

        

    
    @commands.Cog.listener()
    async def on_message(self, message):
        if self.has_run == False:
            self.can_run = False
        if self.can_run == True:
            if message.content.lower().startswith("good morning"):
                    self.has_run = False
                    time.sleep(7)
                    await message.reply("Good Morning.")

            

        
    




def setup(bot):
    bot.add_cog(good_morning(bot))
