from discord.ext import commands
import discord
import discord.utils
import json
import asyncio
from datetime import date
import datetime
import pytz
import functions
client = commands.Bot(command_prefix="?",owner_ids=[386826952599928842, 427822985102098434], intents=discord.Intents.all())


class day(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.index = 0

        #runs every hour to check if the day has changed and if so, runs the birthday function and last_active functions
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

        
            

            if True: 
                y = str(date.today())
                
                
                
                
                with open("jsons/date.json") as fj: 
                    feeds = json.load(fj)
                with open("jsons/user_info.json") as oj: 
                    o = json.load(oj)
                
                #if it's a new day this will run:
                if feeds != y:
                    #await asyncio.sleep(10)
                    print(feeds)
                    print(y)
                    
                    print(f"\nStarting checks:\n\n")
                    #removes the "new" role from users if thier 7 days are up
                    print("starting new member check")
                    for user in o:
                        

                        if o[user]["new"] == 7:
                            o[user]["new"] = 420.69  
                            member = guild.get_member(int(user))
                            await member.remove_roles(role)
                            
                        elif o[user]["new"] > 7:
                            pass

                        else:
                            o[user]["new"] = o[user]["new"] + 1
                    print(f"done with new member check\n")

                    # with open("jsons/user_info.json", mode='w') as f:
                    #     f.write(json.dumps(o, indent=2))
                        
                    
                    
                    
     
                    
                
                    #Birthday function, If it's your birthday the bot will anounce it to the server 
                    

                    current = str(date.today())
                    datel = []
                    date1 = str(date.today())
                    for number in date1:
                        datel.append(number)
                     
                    print("starting birthday check")
                    for user in o:
                    
                        day = []
                        try:
                            for number in o[user]["birthday"]:
                                day.append(number)
                            match = 0
                            for number in range(4, 10):
                                if day[number] == datel[number]:
                                    match += 1
                                    
                            
                            if match == 6:
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
                        except:
                            pass
                    print("done with birthday check\n")            




                                
                    # with open("jsons/user_info.json") as feedsjson: 
                    #     data = json.load(feedsjson)
                    
                        #last_active, Adds +1 to the users Inactive days
                    
                    print("starting last active check")
                    for key in o:  
                        
                        try:
                            o[key]["last_active(days)"] = o[key]["last_active(days)"]+1
                        except:
                            o[key]["last_active(days)"] = 1

                        
                        
                        guild= discord.utils.get(self.client.guilds, id=int(932684556572700773))
                        one_month = discord.utils.get(guild.roles, id=int(961226882534236161)) 
                        three_months = discord.utils.get(guild.roles, id=int(961529848369659914)) 
                        six_months = discord.utils.get(guild.roles, id=int(961530872933257246)) 
                        one_year = discord.utils.get(guild.roles, id=int(961531454460944406))
                        two_years_or_more = discord.utils.get(guild.roles, id=int(961531735500288062))  
                        
                        days = o[key]["last_active(days)"]
                        for key in o:
                            if not days < 30:
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
                    
                    with open("jsons/user_info.json", mode='w') as f:
                        f.write(json.dumps(o, indent=2))
                    print("done with last active check\n")

                    #Post clips to reddit
                    
                    with open("jsons/clips.json") as f:
                        clips = json.load(f)
                    if clips != {}:
                        if len(clips) == 10:
                            member = discord.utils.get(self.client.get_all_members(), id=457493058687205377)
                            await member.send("Waring: there are 10 clips left in the queue, please add more to the queue")
                            
                        if len(clips) >= 10:
                            functions.post_todays_clip()
                        else:
                            with open("jsons/day_of_clips.json") as f:
                                day = json.load(f)
                            if day == 2:
                                functions.post_todays_clip()
                                day = 1
                            else:
                                day = 2
                                
                            with open("jsons/day_of_clips.json", mode='w') as f:
                                f.write(json.dumps(day, indent=2))
                    
                    with open("jsons/date.json", mode='w') as f:
                        f.write(json.dumps(y, indent=2))
                    
                    
                        
                    
                
          
                    

                    
                    
            await asyncio.sleep(3600)


    
         

        


       
       
    
        #Command to se what date it is (I dunno why anyone would use this but it's here)(I use it for testing)
    @commands.command(name='what_date',aliases=["whd"],description='what day is it?',brief='what day is it?')
    async def what_date(self, ctx, *, text: commands.clean_content = ''):
        await ctx.send(f"Time in Buffalo, New York: {date.today()}")



        #Command to see what time it is for Kenny
    @commands.command(name='kenny_time',aliases=["knt"],brief='What time is it for Kenny?')
    async def kenny_time(self, ctx, *, text: commands.clean_content = ''):
        dt_today = datetime.datetime.today()
        dt_Kenny = dt_today.astimezone(pytz.timezone('America/Edmonton'))
        Kenny_time = (dt_Kenny.strftime('%m/%d %H:%M'))
        await ctx.send(Kenny_time)



def setup(bot):
    bot.add_cog(day(bot))

