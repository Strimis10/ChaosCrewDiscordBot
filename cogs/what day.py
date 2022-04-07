#pip install schedule



import time
from cv2 import medianBlur
from discord.ext import commands, tasks
import discord
import discord.utils
import json
import asyncio
import pandas as pd
import os

client = commands.Bot(command_prefix="?",owner_ids=[386826952599928842, 427822985102098434], intents=discord.Intents.all())


class birthday(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.index = 0

    # @commands.Cog.listener()
    # async def on_ready(self, client):
    # @commands.Cog.listener()
    # async def on_ready(self, client):
    @commands.Cog.listener()
    async def on_ready(self):
        while(True):
            from datetime import date

            

            
            # if not os.path.isfile("date.json"):
            #     y = 2
                
            #     with open("date.json", mode='w') as f:
            #         f.write(json.dumps(y, indent=2))
            

            if 1 == 1: 
                y = str(date.today())
                
                
                
                with open("date.json") as fj: 
                    feeds = json.load(fj)
                
                
                if feeds != y:
                    
                    with open("date.json", mode='w') as f:
                        f.write(json.dumps(y, indent=2))
                    self.channel = self.client.get_channel(934475802593091636)       
                    if self.channel != None:
                
                        
                        list = {}

                        curren = date.today()
                        
                        current = str(curren)

                        datel = []
                        date1 = str(date.today())
                        for number in date1:
                            datel.append(number)
                        # while current == date.today():
                        with open("birthdays.json") as f:       
                            data = json.load(f) 
                            for user in data:
                               
                                day = []
                                for number in data[user]:
                                    day.append(number)
                                match = 0
                                for number in range(4, 10):
                                    if day[number] == datel[number]:
                                        match += 1
                                        
                                
                                if match == 6:
                                    # await ctx.send("Happy")
                                    #await commands.ctx.send("Happy")
                                    #934475802593091636# 786013884737781872]
                                    # await client.change_presence(activity=discord.Game('B')
                                    # channel = client.get_channel(934475802593091636)
                                    #bot.get_channel
                                    #https://www.youtube.com/watch?v=0tn86pqnp0Q
                                    username = self.client.get_user(user)
                                    umention = f"<@{user}>"
                                    thier_year = ""
                                    current_year = ""
                                    for number in range(0, 4):
                                        thier_year = thier_year + day[number]
                                    for number in range(0, 4):
                                        current_year = current_year + current[number]
                                    
                                    if thier_year != "0000":
                                        age = int(current_year) - int(thier_year)
                                        await self.channel.send(f"It's {umention}'s birthday today, Congrats!")
                                        if age < 0:
                                            await self.channel.send(f"By the birthyear they've set they are turning {age}, and I don't think that's possible...")
                                        elif age > 100:
                                            await self.channel.send(f"By the birthyear they've set they are turning {age}, that's very impressive")
                                        elif age == 18:
                                            await self.channel.send(f"They are turning {age} and can now legally drink alcohol in Sweden")
                                        elif age == 20:
                                            await self.channel.send(f"They are turning {age} and can now legally buy alcohol in Sweden (Systembolaget)")
                                        else:
                                            await self.channel.send(f"They are turning {age}!")




                                    else:
                                        await self.channel.send(f"It's {umention}'s birthday today, Congrats!")
                                    print(f"{user}: match")
                                    print("Happy birthday!!")


                    with open("last_active.json") as feedsjson: 
                        data = json.load(feedsjson)
                    for key in data:      
                        data[key] = data[key]+1


                    with open("last_active.json", mode='w') as f:
                        f.write(json.dumps(data, indent=2))
                    guild= discord.utils.get(self.client.guilds, id=int(932684556572700773))
                    one_month = discord.utils.get(guild.roles, id=int(961226882534236161)) 
                    three_months = discord.utils.get(guild.roles, id=int(961529848369659914)) 
                    six_months = discord.utils.get(guild.roles, id=int(961530872933257246)) 
                    one_year = discord.utils.get(guild.roles, id=int(961531454460944406))
                    two_years_or_more = discord.utils.get(guild.roles, id=int(961531735500288062))  
                    for key in data:
                        days = data[key]
                        if days >= 30 and days <= 89:
                            member = guild.get_member(int(key))
                            await member.add_roles(one_month)
                        elif days >= 90 and days <= 119:
                            member = guild.get_member(int(key))
                            await member.add_roles(three_months)
                        elif days >= 182 and days <= 364:
                            member = guild.get_member(int(key))
                            await member.add_roles(six_months)
                        elif days >= 365 and days <= 729:
                            member = guild.get_member(int(key))
                            await member.add_roles(one_year)
                        elif days >= 730:
                            member = guild.get_member(int(key))
                            await member.add_roles(two_years_or_more)
          
                    

                    
                    
            await asyncio.sleep(43200)


    
         

        

            #     print(date)
       
       

    
    @commands.command(name='what_date',aliases=["whd"],description='what day is it?',brief='what day is it?')
    async def say(self, ctx, *, text: commands.clean_content = ''):
        from datetime import date
        await ctx.send(date.today())

        # @printer.before_loop
        # async def before_printer(self):
        #     print('waiting...')
        #     await self.bot.wait_until_ready()
           
        
        
    #     discord.ctx.send("")

    # print(date.today())


def setup(bot):
    bot.add_cog(birthday(bot))


