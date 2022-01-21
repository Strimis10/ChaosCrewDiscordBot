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
    async def unban_word(self, ctx, *, text: commands.clean_content = ''):
        if commands.is_owner or commands.has_role([786014220721979445, 786014064533831690, 933127964248375337, "Administrator", "Developers"]) or commands.has_permissions(administrator=True):
            with open("banned_words.json") as feedsjson:
                feeds = json.load(feedsjson)
                
                try: 
                    text2 = text.lower()
                    yes = feeds.index(text2)
                    del feeds[yes] 



                except ValueError:
                    await ctx.send(f"'{text}' is not a Banned word")



        # feeds.append(text)
        # for i in range(len(feeds)):
        #     feeds[i] = feeds[i].lower()
        #     print(feeds)
        #     with open("banned_words.json", mode='w') as f:
        #         f.write(json.dumps(feeds, indent=2)) 
       


def setup(bot):
    bot.add_cog(usefull(bot))



    
    
    
   