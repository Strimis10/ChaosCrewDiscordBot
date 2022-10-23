##https://www.youtube.com/watch?v=k6eCJDSemu4

from datetime import datetime
from email.mime import message
from typing import Optional
from discord.ext import commands
import discord
import discord.utils
from discord import Embed
from discord.ext.commands import Bot, Cog
from discord_slash import cog_ext, SlashContext
from discord.ext import commands
import discord
import discord.utils
import json
from discord_slash import SlashCommand, SlashContext
import random


class userInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    #Command for everyone to get info about a users discord account
    @cog_ext.cog_slash(name="User_info", 
        description="gives a summary of the user",
        guild_ids=[932684556572700773,786013884216639509,983015288910000188])
    async def user_info(self, ctx, target: Optional[discord.Member]):
        target = target or ctx.author

        embed = discord.Embed(title="User information",
                                    colour=target.colour,
                                    )

        fields = [("ID", target.id, False),
                ("Username", str(target), True,),
                ("Bot", target.bot, True),
                ("Server Booster", bool(target.premium_since), True),  
                ("Top role", target.top_role.mention, True),
                ("Is Bot owner", bool(target.id in [427822985102098434, 386826952599928842]), True),
                ("Admin", bool(target.guild_permissions.administrator), True),
                ("User created at", target.created_at.strftime("%d/%m/%Y %H:%M:%S"), False),
                ("Joined server at", target.joined_at.strftime("%d/%m/%Y %H:%M:%S"), True)
                ]

        for name, value, inline in fields: 
            embed.add_field(name=name, value=value, inline=inline)       
            embed.set_thumbnail(url=target.avatar_url)
        await ctx.send(embed=embed)



    @cog_ext.cog_slash(name="requestData", 
        description="Recieve a DM containing the data that is associated with your user.",
        guild_ids=[932684556572700773,786013884216639509,983015288910000188])
    async def requestData(self, ctx):
        msg = await ctx.send("Gathering your info...")
        try:
            with open("jsons/user_info.json") as userData: 
            
                data = json.load(userData)
                if ctx.author.id in data:
                    pass
                else:
                    msg.edit("You are not in the database.")
            data = data[str(ctx.author.id)]
            await msg.edit(content="sending..")
            await ctx.author.send(data)
        except discord.errors.Forbidden:
            await msg.edit(content="Failed.")
            await ctx.send("Please make sure that you have 'Allow direct messages from server members' enabled in the discord settings")
        except:
            await msg.edit(content="Failed.")
        else:
            await msg.edit(content="Sent.")



    # @commands.command(name='Server_info', aliases=["si"])
    # async def server_info(self, ctx):
    #     pass


def setup(bot):
    bot.add_cog(userInfo(bot))




