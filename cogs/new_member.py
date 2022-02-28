from discord.ext import commands
import discord
import discord.utils
from discord.utils import get
import json
import os
import time
import asyncio

#client = commands.Bot(command_prefix="?",owner_ids=[386826952599928842, 427822985102098434], intents=discord.Intents.all())


class new(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    

    @commands.Cog.listener()
    async def on_ready(self):
        while(True):
            from datetime import date

            

            
            # if not os.path.isfile("date.json"):
            #     y = 2
                
            #     with open("date.json", mode='w') as f:
            #         f.write(json.dumps(y, indent=2))
                
        
            y = str(date.today())
            print(y)
            
            
            with open("date.json") as fj: 
                feeds = json.load(fj)
            print(feeds)
            
            if feeds != y:
                print("not1")
                with open("date.json", mode='w') as f:
                    f.write(json.dumps(y, indent=2))


                print("old")
                with open("new.json") as oj: 
                    o = json.load(oj)

                for user in o:
                    if o[user] == 69.420:
                        pass
                    elif o[user] >= 7:
                        o[user] = 69.420
                        # user1 = await self.bot.get_user_info(user)
                        # username = user1.name
                        client = discord.Client
                        #username = client.get_user(user)
                        print(user)
                        print(type(user))
                        username = await client.fetch_user(user)
                        print(username)#my id: Cluebo#2312
                        role = discord.utils.get(username.guild.roles, id=946936153687347230)
                        await o[user].remove_roles(role)

                    else:
                        o[user] = o[user] + 1

                with open("new.json", mode='w') as f:
                    f.write(json.dumps(o, indent=2))
            await asyncio.sleep(10)



def setup(bot):
    bot.add_cog(new(bot))


