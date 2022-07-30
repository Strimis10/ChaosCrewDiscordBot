from discord import Embed
from discord_slash import cog_ext, SlashContext
from discord.ext import commands
import discord
import os



class ISS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    
    @cog_ext.cog_slash(name="IssLocation", description="",guild_ids=[932684556572700773,786013884216639509,983015288910000188])
    async def IssLocation(self, ctx: SlashContext):
        from functions import get_ISS_location, get_map_view 
        picture_name = "ISS_map_view" #.png
        iss_lat, iss_lon = get_ISS_location()
        
        get_map_view(iss_lat,iss_lon,picture_name)
        
        embed = discord.Embed(title="The ISS:", description="Oh look, the fastest humans!", color=0x3c005a) 
        file = discord.File(f"{picture_name}.png", filename=f"{picture_name}.png")
        embed.set_image(url=f"attachment://{picture_name}.png")
        await ctx.send(file=file, embed=embed)
        if os.path.isfile(f"{picture_name}.png"):
            os.remove(f"{picture_name}.png")
        


def setup(bot):
    bot.add_cog(ISS(bot))
