from discord import Embed
from discord.ext.commands import Bot, Cog
from discord_slash import cog_ext, SlashContext
from discord.ext import commands
import discord
import discord.utils
import json

class reddit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    #responds with the amount of clips in the clips.json file 
    @commands.command(name="clip-amount", aliases=["ca"])
    async def clip_amount(self, ctx):
        with open("jsons/clips.json") as f:
            feeds = json.load(f)
        await ctx.send(len(feeds))
    
    #responds with the urls from the clips.json file
    @commands.command(name="clip-urls", alias="cus")
    async def clip_urls(self, ctx):
        with open("jsons/clips.json") as f:
            feeds = json.load(f)
        await ctx.send(feeds)

        
    #Command to add a clip to be posted to the reddit
    @cog_ext.cog_slash(name="add_clip",
        description="",
        guild_ids=[932684556572700773,786013884216639509,983015288910000188])
    async def add_clip(self, ctx: SlashContext,title : str, url: str):
        
        
        import what_server
        if what_server.Kennevo:
            guild = discord.utils.get(self.bot.guilds, id=int(786013884216639509))
            roles = [963554018154664068, 786014220721979445, 786014064533831690]
            self.channel = self.bot.get_channel(786013884737781872) 
        else:
            guild= discord.utils.get(self.bot.guilds, id=int(932684556572700773))
            roles = [932684901801660526]
            self.channel = self.bot.get_channel(934475802593091636) 
        
        #checks if the user has permission the use the command
        for role in ctx.author.roles:
            if role.id in roles:
                permission = True
                break
            else:
                permission = False
        if ctx.author.id == 427822985102098434:
            permission = True
        elif ctx.author.id == 457493058687205377:
            permission = True 
        


        if permission:
            try:
                link = url
                with open("jsons/clips.json") as feedsjson: 
                    feeds = json.load(feedsjson)
                if link not in feeds:
                    if "clips.twitch.tv" in link.lower():
                            
                        with open("jsons/clips.json") as f:
                            feeds = json.load(f)
                        
                        feeds[title] = link

                        with open("jsons/clips.json", mode='w') as f:
                            f.write(json.dumps(feeds, indent=2)) 
                        await ctx.send("Added clip")
                    
                    elif "twitch.tv/kennevo/clip/" in link.lower():
                            
                        with open("jsons/clips.json") as f:
                            feeds = json.load(f)
                        
                        feeds[title] = link

                        with open("jsons/Sclips.json", mode='w') as f:
                            f.write(json.dumps(feeds, indent=2)) 
                        await ctx.send("Added clip")
                    
                    else:
                        await ctx.send(f'"{link}" is not a valid twitch clip')
                else:
                    await ctx.send(f'"{link}" is already in the list')
            
            except:
                await ctx.send("error")

        else:
            await ctx.send("Permission denied")


def setup(bot):
    bot.add_cog(reddit(bot))
