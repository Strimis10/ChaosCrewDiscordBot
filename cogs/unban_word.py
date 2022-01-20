from textwrap import indent
from discord.ext import commands
import discord
import discord.utils
import json
import os
a = []



class usefull(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='unban_word',description='Bot unbans a word from being used in text chat')
    @commands.is_owner()
    async def unban_word(self, ctx, *, text: commands.clean_content = ''):
        with open("banned_words.json") as feedsjson:
            feeds = json.load(feedsjson)
         
        try: del feeds[text]

        except KeyError:
            await ctx.send("That is not a Banned word")



        # feeds.append(text)
        # for i in range(len(feeds)):
        #     feeds[i] = feeds[i].lower()
        #     print(feeds)
        #     with open("banned_words.json", mode='w') as f:
        #         f.write(json.dumps(feeds, indent=2)) 
       


def setup(bot):
    bot.add_cog(usefull(bot))



    
    
    
   