
import asyncio
from re import M
from discord.ext import commands
import discord
import discord.utils
import json
import os
a = []
e = {}
from typing import Optional
import random
import time

from datetime import datetime
import humanfriendly
import aiohttp
import discord
import warnings
import timeout_user


warnings.filterwarnings("ignore", category=DeprecationWarning)
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=['$',], intents=intents)
bot.session = aiohttp.ClientSession()
the_immune = []
word_immune = []



    




class usefull(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    
    

    @commands.command(name='ban_word',aliases=["bw"],description='Bot bans a word from being used in text chat')  
    async def banWord(self, ctx, *, text):  
        member = discord.utils.get(self.bot.get_all_members(), id=ctx.author.id)
        #user = discord.utils.get(self.bot.get_all_members(), id=message.author.id)
        import what_server
        if what_server.Kennevo:
            guild = discord.utils.get(self.bot.guilds, id=int(786013884216639509))
            roles = [963554018154664068, 786014220721979445, 786014064533831690]
            self.channel = self.bot.get_channel(786013884737781872) 
            
            
        else:
            guild= discord.utils.get(self.bot.guilds, id=int(932684556572700773))
            roles = [932684901801660526]
            self.channel = self.bot.get_channel(934475802593091636) 
        

        print(member.roles)
        for role in member.roles:
            print(role.id)
            if role.id in roles:
                permission = True
                break

            else:
                permission = False
        
        if ctx.author.id == 427822985102098434:
            permission = True
        

        if permission == True:       
            if not os.path.isfile("banned_words.json"):
                a.append(text)
                with open("banned_words.json", mode='w') as f:
                    f.write(json.dumps(a, indent=2))
                await ctx.send(f'Word "{text}" Banned')
            else:
                with open("banned_words.json") as feedsjson: 
                    feeds = json.load(feedsjson)

                feeds.append(text.lower())
                print(feeds)
                for i in range(len(feeds)):
                    feeds[i] = feeds[i].lower()
                    print(feeds)
                    with open("banned_words.json", mode='w') as f:
                        f.write(json.dumps(feeds, indent=2))  
                await ctx.send(f'Word "{text}" Banned')
        elif permission == False:
            await ctx.send("Permission denied")





    @commands.command(name='bannedwords',aliases=["bws"],description='bot sends a list of all banned words')
    async def bannedWords(self, ctx,):
        with open("banned_words.json") as f:
            fe = json.load(f)
            if fe == []:
                await ctx.send("There are no banned words")
            else:
                await ctx.send(fe)




    # @commands.Cog.listener()
    # async def bannedWordsListen(self, ctx, message):
    #     with open("banned_words.json") as f:
    #         fe = json.load(f)
    #     if message.content.lower() in fe:
    #         if message.author.id != 932687176997687316:
    #             await ctx.send(f"@{message.author} That is a banned word an may not be used")

    @commands.command(name='unban_word',aliases = ["ubw"], description='Bot unbans a word from being used in text chat')
    async def unbanWord(self, ctx, *, text):
        member = discord.utils.get(self.bot.get_all_members(), id=ctx.author.id)
        import what_server
        if what_server.Kennevo:
            guild = discord.utils.get(self.bot.guilds, id=int(786013884216639509))
            roles = [963554018154664068, 786014220721979445, 786014064533831690]
            self.channel = self.bot.get_channel(786013884737781872) 
            
            
        else:
            guild= discord.utils.get(self.bot.guilds, id=int(932684556572700773))
            roles = [932684901801660526]
            self.channel = self.bot.get_channel(934475802593091636) 
        

        print(member.roles)
        for role in member.roles:
            print(role.id)
            if role.id in roles:
                permission = True
                break

            else:
                permission = False
        
        if ctx.author.id == 427822985102098434:
            permission = True
        
        if permission == True:

            with open("banned_words.json") as feedsjson: 
                feeds = json.load(feedsjson)

            
            


                try: 
                    text2 = text.lower()
                    yes = feeds.index(text2)
                    print(yes)
                    feeds[yes] = "卐"
                    for i in range(len(feeds)):
                        feeds[i] = feeds[i].lower()
                        print(feeds)
                        with open("banned_words.json", mode='w') as f:
                            f.write(json.dumps(feeds, indent=2))
                    await ctx.send(f'word "{text}" unbaned')





                except ValueError:
                    await ctx.send(f"'{text}' is not a Banned word")
        elif permission == False:
            await ctx.send("Permission denied")

        # with open("banned_words.json", mode='w') as f:
        #     text = text.lower()
        #     f.append(text, indent=2)
            # json.dump(feeds, f)
        #  with open("banned_words.json", "r+") as file:
        #     data = json.load(file)
        #     data.update(text)
        #     file.seek(0)
        #     json.dump(data, file, indent=2)
        # with open('baned_words.json', 'w') as f:
        #     json.dump(text, f, indent=2)




    @commands.command(name='baned_word_immunity',aliases=["BWI", "bwi", "bannedwordimmunity"],breif='Bot grants the specified user imunity from the banned_words function and everything it does.')
    async def word_immunity(self, ctx, target: Optional[discord.Member]):
        target = target
        member = discord.utils.get(self.bot.get_all_members(), id=target.author.id)

        roles = [933127964248375337, 932684901801660526, 786014220721979445]
        
        for role in member.roles:
            if role.id in roles:
                permission = True
                break
            elif ctx.author.id == 427822985102098434:
                permission = True
                break
            

            else:
                permission = False
        
        if ctx.author.id == 427822985102098434:
            permission = True

        if permission == True:
        
           

            
            with open("user_info.json") as feedsjson: 
                feeds = json.load(feedsjson)

            # try:
            #     print(feeds[target.id]["immunity"])

            # except:
            feeds[target.id]["word_immunity"] = True
        
            with open("user_info.json", mode='w') as f:
                f.write(json.dumps(feeds, indent=2))


            await ctx.send(f'{target} is now immune from the banned_words function')
        else:
            await ctx.send("Permission denied")

    #@commands.command(name='bwi_remove',aliases=["BWI_remove", "bannedwordimmunity_remove"],description='Bot removes the user imunity from the banned_words function and everything it does.')

    @commands.Cog.listener()
    async def on_message(self, message):
        member = discord.utils.get(self.bot.get_all_members(), id=message.author.id)
        

        
        import what_server
        if what_server.Kennevo:
            guild_id = 786013884216639509
            guild = discord.utils.get(self.bot.guilds, id=int(786013884216639509))
            role = discord.utils.get(guild.roles, id=int(953004596882702386))
            roles = [963554018154664068, 786014220721979445, 786014064533831690]
            
            
        else:
            guild_id = 932684556572700773
            guild= discord.utils.get(self.bot.guilds, id=int(932684556572700773))
            roles = [932684901801660526]
        for role in member.roles:
            #print(role.name)
            if role.id in roles:
                permission = True
                break


            else:
                permission = False
        # with open("user_info.json") as oj: 
        #     feeds = json.load(oj)
        # if feeds[message.author.id]["word_immunity"] == True:
        #     permission = True
        if message.author.id == 427822985102098434:
            permission = True
        


        if permission == False:            
            if message.author.id != 932687176997687316:
            
                with open("banned_words.json") as oj: 
                        o = json.load(oj)
                        for word in o:
                            try:
                                if word in message.content.lower():

                                  
                                    with open("user_info.json") as feedsjson: 
                                        feeds = json.load(feedsjson)
                                    
                                    try:
                                        print(feeds[str(message.author.id)]["incidents"] )
                                    except:
                                        feeds[str(message.author.id)]["incidents"] = 0
                                    print(feeds[str(message.author.id)]["incidents"] )
                                    feeds[str(message.author.id)]["incidents"] = feeds[str(message.author.id)]["incidents"] + 1
                                    for i in range(len(feeds)):
                                        with open("user_info.json", mode='w') as f:
                                            f.write(json.dumps(feeds, indent=2))  
                                    
                                    
                                    with open("user_info.json") as feedsjson: 
                                        feeds = json.load(feedsjson)
                                    #guild= discord.utils.get(self.bot.guilds, id=int(932684556572700773))
                                    
                                    incidents = feeds[str(message.author.id)]["incidents"]

                                    if incidents == 1:
                                        await message.reply(f"{message.author.mention} That's a Banned word, this is your 1:st incident, this will be logged and after 4 incidents you will be timed out, 5: kicked and 6: banned. use '?bws' to se a list of the banned words")
                                        await message.delete()

                                    if incidents == 2:
                                        await message.reply(f"{message.author.mention} That's a Banned word, this is your 2:nd incident, this will be logged and after 4 incidents you will be timed out, 5: kicked and 6: banned. use '?bws' to se a list of the banned words")
                                        await message.delete()

                                    elif incidents == 3:
                                        await message.reply(f"{message.author.mention} That's a Banned word, this is your 3:d incident, this will be logged and after 4 incidents you will be timed out, 5: kicked and 6: banned. use '?bws' to se a list of the banned words")
                                        await message.delete()

                                    elif incidents == 4:
                                        #guild_id = 932684556572700773
                                        user_id = message.author.id
                                        time_in_mins = 1440
                                        timeout_user.timeout_user(user_id=user_id, guild_id=guild_id,until=time_in_mins)
                                        await message.reply(f"{message.author.mention} That's a Banned word, this is your 4:th incident, you will be timed out for 24 hours")
                                        await message.reply("BAD BOII!!, you can't say that without consequences")
                                        await message.delete()
                                        
                                            
                                        #print(type(message.author))
                                        #await message.author.kick(reason="BAD BOII!!, you can't say that without consequences")
                                        #await message.author.timeout(discord.utils.utcnow() + datetime.timedelta(seconds=86400), reason=reason)
                                        #await member.timeout(until = discord.utils.utcnow() + datetime.timedelta(seconds=86400), reason=reason)
                                        #await ctx.send (f"{member} callate un rato anda {time}")

                                        #await message.author.edit(timeout=nextcord.utils.utcnow()+datetime.timedelta(seconds=86400), reason="BAD BOII!!, you can't say that without consequences")
                                    
                                    elif incidents == 5:
                                        await message.reply(f"{message.author.mention} That's a Banned word, this is your 5:th incident, you will now be kicked from the server. next time this happens you will be banned!")
                                        guild_id = 932684556572700773
                                        user_id = message.author.id
                                        time_in_mins = 2
                                        timeout_user.timeout_user(user_id=user_id, guild_id=guild_id,until=time_in_mins)
                                        await message.delete()
                                        await asyncio.sleep(30)
                                        await message.author.kick(reason="BAD BOII!!, you can't say that without consequences")
                                        

                                    elif incidents == 6:
                                        await message.reply(f"{message.author.mention} That's a Banned word, this is your 6:th incident, you will now be banned from the discord server. Good bye!")
                                        guild_id = 932684556572700773
                                        user_id = message.author.id
                                        time_in_mins = 1
                                        timeout_user.timeout_user(user_id=user_id, guild_id=guild_id,until=time_in_mins)
                                        await message.delete()
                                        await asyncio.sleep(15)
                                        await message.author.ban(reason="BAD BOII!!, you can't say that without consequences")
                                    
                                    elif incidents <= 0:
                                        await message.reply(f"{message.author.mention} That's a Banned word but you've been graced with negative incidents, this means you won't be disciplined untill your negative incidents run out.")
                                        await message.delete()
                                    #if incidents == 4:
                                        
                                    try: 
                                        Strimis = "<@427822985102098434>"
                                        Harry = "<@386826952599928842>"
                                        await message.reply(f"{Strimis} {Harry}; {message.author.mention} said a banned word but something has gone wrong, and needs to be fixed")
                                        await message.delete()

                                    except:
                                        pass
                            except TypeError:
                                pass




                                        
                                            

                                    
                    
                                    

    
       


def setup(bot):
    bot.add_cog(usefull(bot))


# from discord.ext import commands
# import discord
# import discord.utils
# import json

# with open('states.json') as f:
#     data = json.load(f)



# for state in data['states']:
#     del state['area_codes']

# with open('new_states.json', 'w') as f:
#     json.dump(data, f, indent=2)
