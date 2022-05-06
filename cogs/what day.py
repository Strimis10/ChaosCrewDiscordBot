import time
from discord.ext import commands, tasks
import discord
import discord.utils
import json
import asyncio
import pandas as pd
import os
from datetime import date
import datetime
import pytz
client = commands.Bot(command_prefix="?",owner_ids=[386826952599928842, 427822985102098434], intents=discord.Intents.all())


class birthday(commands.Cog):
    def __init__(self, client):
        self.client = client
        #self.bot = bot
        self.index = 0

    # @commands.Cog.listener()
    # async def on_ready(self, client):
    # @commands.Cog.listener()
    # async def on_ready(self, client):
    @commands.Cog.listener()
    async def on_ready(self):
        while(True):
            from datetime import date
            import what_server
            if what_server.Kennevo:
                guild = discord.utils.get(self.client.guilds, id=int(786013884216639509))
                role = discord.utils.get(guild.roles, id=int(953004596882702386))
                self.channel = self.client.get_channel(786013884737781872) 
                
                
            else:
                guild= discord.utils.get(self.client.guilds, id=int(932684556572700773))
                role = discord.utils.get(guild.roles, id=int(946936153687347230))
                self.channel = self.client.get_channel(934475802593091636) 

            

            
            # if not os.path.isfile("date.json"):
            #     y = 2
                
            #     with open("date.json", mode='w') as f:
            #         f.write(json.dumps(y, indent=2))
            

            if 1 == 1: 
                y = str(date.today())
                
                
                
                with open("date.json") as fj: 
                    feeds = json.load(fj)
                with open("user_info.json") as oj: 
                    o = json.load(oj)
                
                
                if feeds != y:
                    for user in o:
                        if o[user]["new"] == 420.69:
                            pass
                        elif o[user]["new"] >= 7:
                            o[user]["new"] = 420.69
                            # user1 = await self.bot.get_user_info(user)
                            # username = user1.name
                            
                            #username = client.get_user(user)
                            
                            #user2 = discord.Member(user)
                            # user1 = user - user[0]
                            # print(len(user1))
                            #user2 = user1 - user[len(user1)]
                            # 0user2 = user

                            #guild = client.get_guild(786013884216639509)
                            # guild = self.bot.get_guild(786013884216639509)
                            # member = guild.get_member(int(user))
                            # print(member)
                            # role = discord.utils.get(guild.roles, id=int(946936153687347230))
                            #guild = self.bot.get_guild(786013884216639509)
                            # import pdb
                            # pdb.set_trace()
                            
                            member = guild.get_member(int(user))
                            
                            

                            



                            await member.remove_roles(role)


                            # role = discord.utils.get(user2.guild.roles, id=946936153687347230)
                            # await user2.remove_roles(role)h


                        else:
                            o[user]["new"] = o[user]["new"] + 1

                    with open("user_info.json", mode='w') as f:
                        f.write(json.dumps(o, indent=2))
                        
                    with open("date.json", mode='w') as f:
                        f.write(json.dumps(y, indent=2))
                        
                    #print(self.channel.name)     
                    if self.channel != None:
                
                        
                        list = {}

                        curren = date.today()
                        
                        current = str(curren)

                        datel = []
                        date1 = str(date.today())
                        for number in date1:
                            datel.append(number)
                        # while current == date.today():
                        with open("user_info.json") as f:       
                            data = json.load(f) 
                        for user in data:
                        
                            day = []
                            for number in data[user]["birthday"]:
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
                    with open("user_info.json") as feedsjson: 
                        data = json.load(feedsjson)
                    for key in data:  
                       
                        try:
                            #print(data[key]["last_active(days)"])
                            data[key]["last_active(days)"] = data[key]["last_active(days)"]+1
                        except:
                            data[key]["last_active(days)"] = 1

                        with open("user_info.json", mode='w') as f:
                            f.write(json.dumps(data, indent=2))
                        with open("user_info.json") as feedsjson: 
                            data = json.load(feedsjson)
                        guild= discord.utils.get(self.client.guilds, id=int(932684556572700773))
                        one_month = discord.utils.get(guild.roles, id=int(961226882534236161)) 
                        three_months = discord.utils.get(guild.roles, id=int(961529848369659914)) 
                        six_months = discord.utils.get(guild.roles, id=int(961530872933257246)) 
                        one_year = discord.utils.get(guild.roles, id=int(961531454460944406))
                        two_years_or_more = discord.utils.get(guild.roles, id=int(961531735500288062))  
                        for key in data:
                            days = data[key]["last_active(days)"]
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
                
          
                    

                    
                    
            await asyncio.sleep(3600)


    
         

        

            #     print(date)
       
       

    
    @commands.command(name='what_date',aliases=["whd"],description='what day is it?',brief='what day is it?')
    async def what_date(self, ctx, *, text: commands.clean_content = ''):
        
        await ctx.send(date.today())
    @commands.command(name='kenny_time',aliases=["knt"],brief='What time is it for Kenny?')
    async def kenny_time(self, ctx, *, text: commands.clean_content = ''):
        dt_today = datetime.datetime.today()
        dt_Kenny = dt_today.astimezone(pytz.timezone('America/Edmonton'))
        Kenny_time = (dt_Kenny.strftime('%m/%d %H:%M'))
        #print(Kenny_time)
        await ctx.send(Kenny_time)

        # @printer.before_loop
        # async def before_printer(self):
        #     print('waiting...')
        #     await self.client.wait_until_ready()
           
        
        
    #     discord.ctx.send("")

    # print(date.today())


def setup(bot):
    bot.add_cog(birthday(bot))


