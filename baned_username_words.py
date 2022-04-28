import asyncio
from calendar import c

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
import datetime
import humanfriendly
the_immune = []
word_immune = []




class usefull(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    
    
    

    @commands.command(name='ban_username_word',aliases=["buw"],description='Bot bans a word from being used in a username',brief='Bot bans a word from being used in a username',usage='?ban_username_word <word>') 
    async def banWord(self, ctx, *, text):  
        member = discord.utils.get(self.bot.get_all_members(), id=ctx.author.id)

        roles = [933127964248375337, 932684901801660526, 786014220721979445]

        print(member.roles)
        for role in member.roles:
            print(role.id)
            if role.id in roles:
                permission = True
                break
            elif ctx.author.id == 427822985102098434:
                permission = True
                break

            else:
                permission = False
                
        
        

        if permission == True:       
            if not os.path.isfile("banned_username_words.json"):
                a.append(text)
                with open("banned_username_words.json", mode='w') as f:
                    f.write(json.dumps(a, indent=2))
                await ctx.send(f'Username word "{text}" Banned')
            else:
                with open("banned_username_words.json") as feedsjson: 
                    feeds = json.load(feedsjson)

                feeds.append(text.lower())
                print(feeds)
                for i in range(len(feeds)):
                    feeds[i] = feeds[i].lower()
                    print(feeds)
                    with open("banned_username_words.json", mode='w') as f:
                        f.write(json.dumps(feeds, indent=2))  
                await ctx.send(f'Username word "{text}" Banned')
        elif permission == False:
            await ctx.send("Permission denied")





    @commands.command(name='buws',aliases=["banneduserwords"],description='bot sends a list of all banned username words')
    async def bannedWords(self, ctx,):
        with open("banned_username_words.json") as f:
            fe = json.load(f)
            if fe == []:
                await ctx.send("There are no banned words")
            else:
                await ctx.send(fe)




    # @commands.Cog.listener()
    # async def bannedWordsListen(self, ctx, message):
    #     with open("banned_username_words.json") as f:
    #         fe = json.load(f)
    #     if message.content.lower() in fe:
    #         if message.author.id != 932687176997687316:
    #             await ctx.send(f"@{message.author} That is a banned word an may not be used")

    @commands.command(name='unban_username_word',aliases = ["ubuw"], description='Bot unbans a word from being used in a username',brief='Bot unbans a word from being used in a username',usage='?unban_username_word <word>')
    async def unbanWord(self, ctx, *, text):
        member = discord.utils.get(self.bot.get_all_members(), id=ctx.author.id)
        

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
        

        if permission == True:

            with open("banned_username_words.json") as feedsjson: 
                feeds = json.load(feedsjson)

            
            


                try: 
                    text2 = text.lower()
                    yes = feeds.index(text2)
                    print(yes)
                    feeds[yes] = "卐"
                    for i in range(len(feeds)):
                        feeds[i] = feeds[i].lower()
                        print(feeds)
                        with open("banned_username_words.json", mode='w') as f:
                            f.write(json.dumps(feeds, indent=2))
                    await ctx.send(f'word "{text}" unbaned')





                except ValueError:
                    await ctx.send(f"'{text}' is not a Banned word")
        elif permission == False:
            await ctx.send("Permission denied")



    


    @commands.Cog.listener()
    async def on_message(self, message):
        member = discord.utils.get(self.bot.get_all_members(), id=message.author.id)

        roles = [933127964248375337, 932684901801660526, 786014220721979445]

        for role in member.roles:
            if role.id in roles:
                permission = True
                break
            elif message.author.id == 427822985102098434:
                permission = True
                break
            elif message.author.id in word_immune:
                permission = True
                break

            else:
                permission = False
        
        

        if permission == False:            
            if message.author.id != 932687176997687316:
            
                with open("banned_usernames_words.json") as oj: 
                        o = json.load(oj)
                        for word in o:
                            
                            if word in message.author.name.lower():
                                with open("banned_username_words.json") as f:
                                    fe = json.load(f)
                                    

                                await message.delete()
                                await message.channel.send(f"@{message.author} your username contains a banned word and you will be kicked from the server, please change your username")
                                await message.channel.send(f"The word that was banned was {word}")
                                await message.channel.send(f"The banned words are {fe}")
                                await message.author.edit(timeout=nextcord.utils.utcnow()+datetime.timedelta(seconds=31), reason="BAD BOII!!!")
                                asyncio.sleep(30)
                                await message.author.kick(reason="BAD BOII!!!")
                                break
                            elif word in member.display_name.lower():
                                with open("banned_username_words.json") as f:
                                    fe = json.load(f)
                                    

                                await message.delete()
                                await message.channel.send(f"@{message.author} your username contains a banned word and you will be kicked from the server, please change your username")
                                await message.channel.send(f"The word that was banned was {word}")
                                await message.channel.send(f"The banned words are {fe}")
                                await message.author.edit(timeout=nextcord.utils.utcnow()+datetime.timedelta(seconds=31), reason="BAD BOII!!!")
                                asyncio.sleep(30)
                                await message.author.kick(reason="BAD BOII!!!")
                                break





                                    

    
       


def setup(bot):
    bot.add_cog(usefull(bot))