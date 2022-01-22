from textwrap import indent
from aiohttp import client
from discord.ext import commands
import discord
import discord.utils
import json
import os
a = []
import random



class usefull(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='ban_word',aliases=["bw"],description='Bot bans a word from being used in text chat')        
    async def banWord(self, ctx, *, text):  
        if commands.is_owner() or commands.has_role([786014220721979445, 786014064533831690, 933127964248375337, "Administrator", "Developers"]) or commands.has_permissions(administrator=True):
                if not os.path.isfile("banned_words.json"):
                    a.append(text)
                    with open("banned_words.json", mode='w') as f:
                        f.write(json.dumps(a, indent=2))
                else:
                    with open("banned_words.json") as feedsjson:
                        feeds = json.load(feedsjson)

                    feeds.append(text)
                    for i in range(len(feeds)):
                        feeds[i] = feeds[i].lower()
                        print(feeds)
                        with open("banned_words.json", mode='w') as f:
                            f.write(json.dumps(feeds, indent=2))  

        else:
            await ctx.send(bool(commands.is_owner))
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
        if commands.is_owner() == True or commands.has_role([786014220721979445, 786014064533831690, 933127964248375337, "Administrator", "Developers"]) == True or commands.has_permissions(administrator=True) == True:
            with open("banned_words.json") as feedsjson:
                feeds = json.load(feedsjson)
                
                try: 
                    text2 = text.lower()
                    yes = feeds.index(text2)
                    del feeds[yes] 



                except ValueError:
                    await ctx.send(f"'{text}' is not a Banned word")
        else:
            await ctx.send(commands.is_owner)
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
        if "i'm not happy" in message.content.lower():
            if message.author.id != 932687176997687316:
                rand2 = random.randint(0, 1)
                if rand2 == 1:
                    await message.reply("EEVEE: Dead")
    
       


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
