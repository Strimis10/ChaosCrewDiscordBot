from discord import Embed
from discord.ext.commands import Bot, Cog
from discord_slash import cog_ext, SlashContext
from discord.ext import commands
import discord
import discord.utils
import json

from discord_slash.utils.manage_commands import create_choice, create_option
from discord_slash import SlashCommand, SlashContext

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    #Command to add a clip to be posted to the reddit
    @cog_ext.cog_slash(name="add_clip",
    description="sends test message",
    guild_ids=[932684556572700773,786013884216639509])
    

    async def add_clip(self, ctx: SlashContext, option: str):
        import what_server
        if what_server.Kennevo:
            guild = discord.utils.get(self.bot.guilds, id=int(786013884216639509))
            roles = [963554018154664068, 786014220721979445, 786014064533831690]
            self.channel = self.bot.get_channel(786013884737781872) 
        else:
            guild= discord.utils.get(self.bot.guilds, id=int(932684556572700773))
            roles = [932684901801660526]
            self.channel = self.bot.get_channel(934475802593091636) 
        
        #checks if the user has permission th use the command
        for role in ctx.author.roles:
            if role.id in roles:
                permission = True
                break
            else:
                permission = False
        if ctx.author.id == 427822985102098434:
            permission = True
        


        if permission:
            print(option)
            #link = input("Enter the link: ")
            
            #with open("clips.json") as f:
           #     feeds = json.load(f)
            
            #feeds.append(link)

            #with open("clips.json", mode='w') as f:
            #    f.write(json.dumps(feeds, indent=2)) 
            print("Added clip")

        else:
            await ctx.send("Permission denied")


def setup(bot):
    bot.add_cog(fun(bot))