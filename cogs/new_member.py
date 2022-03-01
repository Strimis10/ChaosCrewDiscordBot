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
    async def on_ready(bot):
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
                        print
                        (type(user))
                        #user2 = discord.Member(user)
                        # user1 = user - user[0]
                        # print(len(user1))
                        #user2 = user1 - user[len(user1)]
                        # 0user2 = user

                        #guild = client.get_guild(786013884216639509)
                        guild = bot.get_guild(786013884216639509)
                        member = guild.get_member(int(user))
                        print(member)
                        role = guild.get_role(int(946936153687347230))
                        print(role)
                        await member.remove_roles(role)


                        # role = discord.utils.get(user2.guild.roles, id=946936153687347230)
                        # await user2.remove_roles(role)

                    else:
                        o[user] = o[user] + 1

                with open("new.json", mode='w') as f:
                    f.write(json.dumps(o, indent=2))
            await asyncio.sleep(10)



def setup(bot):
    bot.add_cog(new(bot))


