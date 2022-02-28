from discord.ext import tasks, commands
import discord
import discord.utils
import time
from datetime import datetime
from pytz import timezone
import pytz

terms = ["good morning"]

class shout(commands.Cog):
    def __init__(self, bot):
        self.can_run = True
        self.has_run = True
        self.bot = bot
        self.index = 0
        self.printer.start()




    @tasks.loop(hours=8)
    async def printer(self):
        self.index += 1
        global can_run
        if self.has_run == True:
            self.can_run = True

        else:
            self.can_run = True
            self.has_run = True

        

    
    @commands.Cog.listener()
    async def on_message(self, ctx):
        if self.has_run == False:
            self.can_run = False
        if self.can_run == True:
            now = datetime.now()
            def convert(dte, fromZone, toZone):
                fromZone, toZone = pytz.timezone(fromZone), pytz.timezone(toZone)
                return fromZone.localize(dte, is_dst=True).astimezone(toZone)


            #current_time = now.strftime("%H:%M:%S")
            #print("Current Time =", current_time)
            #convert(current_time, )
            mst = timezone('MST')
            print("Time in MST:", datetime.now(mst))
           
        
    



    # @commands.Cog.listener()
    # async def on_message(self, message):
    #     if message.content.lower().startswith("good night"):
    #         if message.author.id != 932687176997687316:
    #             time.sleep(10)
    #             await message.reply("Good Night")


def setup(bot):
    bot.add_cog(shout(bot))
