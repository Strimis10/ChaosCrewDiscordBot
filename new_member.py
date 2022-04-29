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
        # #guild = self.bot.get_guild(786013884216639509)
        # import pdb
        # pdb.set_trace()
        # guild= discord.utils.get(self.bot.guilds, id=int(932684556572700773))
        # #member = guild.get_member(int(user))
        # print(guild)
        # role = discord.utils.get(guild.roles, id=int(946936153687347230))
        # print(role)

        # await asyncio.sleep(1)
        # print(f".{self.bot.guilds}")
        
        while(True):
            from datetime import date

            

            
            # if not os.path.isfile("date.json"):
            #     y = 2
                
            #     with open("date.json", mode='w') as f:
            #         f.write(json.dumps(y, indent=2))
                
        
            y = str(date.today())
            
            
            
            with open("date.json") as fj: 
                feeds = json.load(fj)
           
            
            if feeds != y:
               
                with open("date.json", mode='w') as f:
                    f.write(json.dumps(y, indent=2))


               
                with open("new.json") as oj: 
                    o = json.load(oj)
                
                # import pdb
                # pdb.set_trace()

                for user in o:
                    if o[user] == 420.69:
                        pass
                    elif o[user] >= 7:
                        o[user] = 420.69
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
                        import what_server
                        if what_server.Kennevo:
                            guild = discord.utils.get(self.bot.guilds, id=int(786013884216639509))
                            role = discord.utils.get(guild.roles, id=int(953004596882702386))
                        else:
                            guild= discord.utils.get(self.bot.guilds, id=int(932684556572700773))
                            role = discord.utils.get(guild.roles, id=int(946936153687347230))
                        
                        member = guild.get_member(int(user))

                        
                        

                        



                        await member.remove_roles(role)


                        # role = discord.utils.get(user2.guild.roles, id=946936153687347230)
                        # await user2.remove_roles(role)h


                    else:
                        o[user] = o[user] + 1

                with open("new.json", mode='w') as f:
                    f.write(json.dumps(o, indent=2))
            await asyncio.sleep(43200)



def setup(bot):
    bot.add_cog(new(bot))


