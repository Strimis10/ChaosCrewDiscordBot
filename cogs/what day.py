#pip install schedule


import time
from discord.ext import commands, tasks
import discord
import discord.utils
import json



class birthday(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.index = 0
        self.printer.start()

    def birthday_unload(self,):
        self.printer.cancel()

    @tasks.loop(hours=12)
    async def printer(self, message):
        self.index += 1

        from datetime import date
        list = {}

        current = date.today()

        datel = []
        date = str(date.today())
        for number in date:
            datel.append(number)
        # while current == date.today():
        with open("birthdays.json") as f:       
            data = json.load(f) 
            for user in data:
                day = []
                for number in data[user]:
                    day.append(number)
                match = 0
                for number in range(4, 9):
                    if day[number] == datel[number]:
                        match += 1
                        

                if match == 5:
                    # await ctx.send("Happy")
                    #await commands.ctx.send("Happy")
                    #934475802593091636# 786013884737781872]
                    # await client.change_presence(activity=discord.Game('B')
                    # channel = client.get_channel(934475802593091636)
                    await message.channel.send(f"{user}: match")
                    print(f"{user}: match")
                    print("Happy birthday!!")

        #     print(date)
       
       
       
        # @printer.before_loop
        # async def before_printer(self):
        #     print('waiting...')
        #     await self.bot.wait_until_ready()
           
        
        
    #     discord.ctx.send("")

    # print(date.today())


def setup(bot):
    bot.add_cog(birthday(bot))


