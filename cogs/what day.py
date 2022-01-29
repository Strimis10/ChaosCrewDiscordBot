#pip install schedule

from datetime import date
import time
from discord.ext import commands
import discord
import discord.utils
import json

list = {}

current = date.today()

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # @commands.command(name='say',description='bot says [text]',brief='bot says [text]')
    # async def say(self, ctx, *, text: commands.clean_content = ''):
    #     #                         ^^ This is for pings / mentions being cleaned so you can't do `a!say @everyone`.
    #     #command content
    
    date = date.today()
    # while current == date.today():
    with open("birthdays.json") as f:       
        data = json.load(f) 
        for user in data:
            print(user)
            for number in range(4, 9):
                if data[user[number]] == date[number]:
                    print("ugh")
            print(data[user])
    #     print(date)
           
        
        
    #     discord.ctx.send("")

    # print(date.today())


def setup(bot):
    bot.add_cog(fun(bot))


