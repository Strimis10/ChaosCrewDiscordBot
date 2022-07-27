from ast import alias
from email import message
from discord.ext import commands
import discord
import discord.utils
import json
import os
from typing import Optional
from discord import Embed
from discord.ext.commands import Bot, Cog
from discord_slash import cog_ext, SlashContext
from discord.ext import commands
import discord
import discord.utils


a = {}



class Birthday(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    #command for everyone to set their birthday
    @cog_ext.cog_slash(name="setBirthday", description="['yyyy-mm-dd' if you don't want to share the year type '0000' as the year]",guild_ids=[932684556572700773,786013884216639509,983015288910000188])
    async def setBirthday(self, ctx: SlashContext, date:str):
    
            
            if date == '':
                await ctx.send("send your birthday like this: 'yyyy-mm-dd' if you don't want to share the year type '0000' as the year. Send this with the 'setBrithday' command (?setBirthday yyyy-mm-dd)")
            elif date[4] != "-":
                await ctx.send("send your birthday like this: 'yyyy-mm-dd' if you don't want to share the year type '0000' as the year. Send this with the 'setBrithday' command (?setBirthday yyyy-mm-dd)")
            elif date[7] != "-":
                await ctx.send("send your birthday like this: 'yyyy-mm-dd' if you don't want to share the year type '0000' as the year. Send this with the 'setBrithday' command (?setBirthday yyyy-mm-dd)")

            else:
                try:
                    int(date.replace("-", ""))
                except:
                    await ctx.send(f"{date} is not a valid date")
                else:

                    with open("jsons/user_info.json") as feedsjson: 
                        feeds = json.load(feedsjson)
                    feeds[str(ctx.author.id)]['birthday'] = date.lower()
                    
                        
                    with open("jsons/user_info.json", mode='w') as f:
                        f.write(json.dumps(feeds, indent=2)) 
                    Birthday = feeds[str(ctx.author.id)]["birthday"] 
                    await ctx.send(f"{ctx.author.name}'s birthday set to {Birthday}")





    #command for everyone to see what birthday someone has

    @commands.command(name='Bday_check',aliases=["Bdaycheck", "bdaycheck", "bday_check"], description='informs you of the persons birthday',brief='informs you of a persons birthday: "?Bdaycheck @Strimis10"')
    async def say(self, ctx, target: Optional[discord.Member]):
        target = target or ctx.author
        with open("jsons/user_info.json") as feedsjson: 
            feeds = json.load(feedsjson)
        name = target.name
        target_id = str(target.id)
        try:
            birthday = feeds[target_id]["birthday"]
            await ctx.send(f"{name}'s birthday is set to {birthday}")
        
        except KeyError:
            await ctx.send(f"{name} has not set their birthday yet...")


def setup(bot):
    bot.add_cog(Birthday(bot))
    