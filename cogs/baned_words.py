from textwrap import indent
from aiohttp import client
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
import nextcord
the_immune = []
word_immune = []


def owner_admin_or_roles(ctx, user: discord.Member):
    roles = [786014220721979445, 786014064533831690, 933127964248375337, "Developers", "Admin"]
    with open("word_immune.json") as feedsjson: 
        feeds = json.load(feedsjson)

     

    if str(ctx.message.author.id) in feeds:
        return True

    elif ctx.message.author.id in [386826952599928842, 427822985102098434]:
        return True


    elif "786014220721979445" in [y.id for y in ctx.message.author.roles]:
        return True
    
    elif "786014064533831690" in [y.id for y in ctx.message.author.roles]:
        return True

    elif "933127964248375337" in [y.id for y in ctx.message.author.roles]:
        return True

    elif "Administrator" in [y.name.lower() for y in ctx.message.author.roles]:
        return True

    elif "Admin" in [y.name.lower() for y in ctx.message.author.roles]:
        return True

    elif "Developers" in [y.name.lower() for y in ctx.message.author.roles]:
        return True

    # elif role2 in user.roles:
    #     return True

    # elif role3 in user.roles:
    #     return True

    # elif role4 in user.roles:
    #     return True

    # elif role5 in user.roles:
    #     return True

    # elif ctx.message.author.has_role([786014220721979445, 786014064533831690, 933127964248375337, "Administrator", "Developers"]):
    #     return True
    
    else:
        return False


def owner_admin_or_roles_message(message, user: discord.Member):
    roles = [786014220721979445, 786014064533831690, 933127964248375337, "Developers", "Admin"]

    


    if message.author.id in [386826952599928842, 427822985102098434]:
        return True

    elif "786014220721979445" in [y.id for y in message.author.roles]:
        return True
    
    elif "786014064533831690" in [y.id for y in message.author.roles]:
        return True

    elif "933127964248375337" in [y.id for y in message.author.roles]:
        return True

    elif "Administrator" in [y.name.lower() for y in message.author.roles]:
        return True

    elif "Admin" in [y.name.lower() for y in message.author.roles]:
        return True

    elif "Developers" in [y.name.lower() for y in message.author.roles]:
        return True

    elif "Owner" in [y.name.lower() for y in message.author.roles]:
        return True
    
    
    # elif role2 in user.roles:
    #     return True

    # elif role3 in user.roles:
    #     return True

    # elif role4 in user.roles:
    #     return True

    # elif role5 in user.roles:
    #     return True

    # elif ctx.message.author.has_role([786014220721979445, 786014064533831690, 933127964248375337, "Administrator", "Developers"]):
    #     return True
    
    else:
        return False




class usefull(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    

    @commands.command(name='ban_word',aliases=["bw"],description='Bot bans a word from being used in text chat')  
    async def banWord(self, ctx, *, text):  
        if owner_admin_or_roles(ctx=ctx, user=discord.Member) == True:       
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
        else:
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

    @commands.command(name='unban_word',aliases = ["uw"], description='Bot unbans a word from being used in text chat')
    async def unbanWord(self, ctx, *, text):
        if owner_admin_or_roles(ctx=ctx, user=discord.Member) == True:

            with open("banned_words.json") as feedsjson: 
                feeds = json.load(feedsjson)

            
            


                try: 
                    text2 = text.lower()
                    yes = feeds.index(text2)
                    print(yes)
                    feeds[yes] = "¬"
                    for i in range(len(feeds)):
                        feeds[i] = feeds[i].lower()
                        print(feeds)
                        with open("banned_words.json", mode='w') as f:
                            f.write(json.dumps(feeds, indent=2))
                    await ctx.send(f'word "{text}" unbaned')





                except ValueError:
                    await ctx.send(f"'{text}' is not a Banned word")
        else:
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

    @commands.Cog.listener()
    async def on_message(self, message):
        if "what a hostage situation is" in message.content.lower():
            if message.author.id != 932687176997687316:
                rand2 = random.randint(0, 1)
                if rand2 == 1:
                    await message.reply("EEVEE: Extremly Horny")

    

    @commands.Cog.listener()
    async def on_message(self, message):
        if "i'm not happy!" in message.content.lower():
            if message.author.id != 932687176997687316:
                rand2 = random.randint(0, 1)
                if rand2 == 1:
                    await message.reply("EEVEE: Dead")

    @commands.has_permissions(administrator=True)
    @commands.command(name='word_immunity',aliases=["WI", "wi", "wordimmunity"],description='Bot grants the user imunity from the Banned_words function and everything it does.')
    async def word_immunity(self, ctx, target: Optional[discord.Member]):
        target = target or ctx.author
        

        
        if not os.path.isfile("word_immune.json"):
            word_immune.append(str(target.id))
            
            with open("word_immune.json", mode='w') as f:
                f.write(json.dumps(word_immune, indent=2))

        else: 
            with open("word_immune.json") as feedsjson: 
                feeds = json.load(feedsjson)

            feeds.append(str(target.id))
        
            with open("word_immune.json", mode='w') as f:
                f.write(json.dumps(feeds, indent=2))


    @commands.command(name="remove_incidents")
    async def remove_incidents(ctx, target: Optional[discord.Member], text: commands.clean_content = ''):
        await ctx.send(ctx.author.id)
        if owner_admin_or_roles(ctx,user=discord.Member) == True:
            with open("incidents.json") as inc:
                i = json.load(inc)
            edited = {}
            
            edited.append(i)
            if target.id in edited:
                if text == '':
                    edited[target.id] = 0
                else:
                    #try:
                    edited[target.id] = text
                    #except 
        else:
            await ctx.send("Permission denied")


    @commands.Cog.listener()
    async def on_message(self, message):
        if owner_admin_or_roles_message(message= message, user=discord.Member) == False:
            if message.author.id != 932687176997687316:
                with open("banned_words.json") as oj: 
                        o = json.load(oj)
                        for word in o:
                            if word in message.content.lower():

                                if not os.path.isfile("incidents.json"):
                                    e[str(message.author.id)] = 1
                                    
                                    with open("incidents.json", mode='w') as f:
                                        f.write(json.dumps(e, indent=2))
                                
                                       
                                else: 
                                    with open("incidents.json") as feedsjson: 
                                        feeds = json.load(feedsjson)
                                    if str(message.author.id) in feeds:

                                        print(feeds[str(message.author.id)])
                                        feeds[str(message.author.id)] = feeds[str(message.author.id)] + 1
                                        for i in range(len(feeds)):
                                            with open("incidents.json", mode='w') as f:
                                                f.write(json.dumps(feeds, indent=2))  
                                    
                                    else:
                                        feeds[str(message.author.id)] = 1
                                        for i in range(len(feeds)):
                                            with open("incidents.json", mode='w') as f:
                                                f.write(json.dumps(feeds, indent=2)) 
                                    
                                    with open("incidents.json") as feedsjson: 
                                        feeds = json.load(feedsjson)

                                    if feeds[str(message.author.id)] == 1:
                                        await message.reply(f"{message.author.mention} That's a Banned word, this is your 1:st incident, this will be logged and after 4 incidents you will be timed out, 5: kicked and 6: then banned. use '?bws' to se a list of the banned words")
                                        await message.delete()

                                    if feeds[str(message.author.id)] == 2:
                                        await message.reply(f"{message.author.mention} That's a Banned word, this is your 2:nd incident, this will be logged and after 4 incidents you will be timed out, 5: kicked and 6: then banned. use '?bws' to se a list of the banned words")
                                        await message.delete()

                                    elif feeds[str(message.author.id)] == 3:
                                        await message.reply(f"{message.author.mention} That's a Banned word, this is your 3:d incident, this will be logged and after 4 incidents you will be timed out, 5: kicked and 6: then banned. use '?bws' to se a list of the banned words")
                                        await message.delete()

                                    elif feeds[str(message.author.id)] == 4:
                                        await message.reply(f"{message.author.mention} That's a Banned word, this is your 4:th incident, you will be timed out for 24 hours")
                                        await message.reply("BAD BOII!!, you can't say that without consequences")
                                        await message.delete()
                                        await message.author.edit(timeout=nextcord.utils.utcnow()+datetime.timedelta(seconds=86400), reason="BAD BOII!!, you can't say that without consequences")
                                    
                                    elif feeds[str(message.author.id)] == 5:
                                        await message.reply(f"{message.author.mention} That's a Banned word, this is your 5:th incident, you will now be kicked from the server. next time this happens you will be banned!")
                                        await message.author.kick(reason="BAD BOII!!, you can't say that without consequences")
                                        await message.delete()

                                    elif feeds[str(message.author.id)] == 6:
                                        await message.reply(f"{message.author.mention} That's a Banned word, this is your 6:th incident, you will now be banned from the discord server. Good bye!")
                                        await message.delete()
                                        time.sleep(15)
                                        await message.author.ban(reason="BAD BOII!!, you can't say that without consequences")
                                    
                                    elif feeds[str(message.author.id)] <= 0:
                                        await message.reply(f"{message.author.mention} That's a Banned word but you've been graced with negative incidents, this means you won't be disciplined untill your negative incidents run out.")
                                        await message.delete()

                                    try: 
                                        Strimis = "<@427822985102098434>"
                                        Harry = "<@386826952599928842>"
                                        await message.reply(f"{Strimis} {Harry}; {message.author.mention} said a banned word but something has gone wrong, and needs to be fixed")
                                        await message.delete()

                                    except:
                                        pass



                                    
                                        


                                    # try:
                                    #     message.author.id = data[message.author.id] + 1
                                    #     with open("incidents.json", mode='w') as r:
                                    #         r.write(json.dumps(message.author.id, indent=2)) 

                                    # except KeyError:
                                    #     data[message.author.id] = 1
                                    #     with open("incidents.json", mode='w') as r:
                                    #         r.write(json.dumps(data, indent=2))  


                                    # with open("incidents.json") as feedsjson: 
                                    #     feeds = json.load(feedsjson)

                                    # feeds[message.author.name] = text.lower()
                                    # for i in range(len(feeds)):
                                    #     print(feeds)
                                    #     with open("incidents.json", mode='w') as f:
                                    #         f.write(json.dumps(feeds, indent=2))  
                                   
                
                                   

    
       


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
