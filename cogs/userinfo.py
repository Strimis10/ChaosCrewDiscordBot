##https://www.youtube.com/watch?v=k6eCJDSemu4

from datetime import datetime
from sqlite3 import Timestamp
from typing import Optional
from ast import alias
from discord.ext import commands
import discord
import discord.utils

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='User_info', aliases=["ui", "Memeber_info", "mi"],description='gives a summary of the user')
    async def user_info(self, ctx, target: Optional[discord.Member]):
        target = target or ctx.author

        embed = discord.Embed(title="User information",
                                    colour=target.colour,
                                    Timestamp=datetime.utcnow())

        fields = [("ID", target.id, False),
                ("Username", str(target), True,),
                ("Bot?", target.bot, True),
                ("Server Booster", bool(target.premium_since), True),  
                ("Top role", target.top_role.mention, True),
                #("Status", str(target.status).title(), True),
                # ("Activity", f"{target.activity.name} {str(getattr(target.activity, 'type')).title()}", True)
                ("Is Admin", bool(target.guild_permissions.administrator), True),
                ("Created at", target.created_at.strftime("%d/%m/%Y %H:%M:%S"), False),
                ("Joined at", target.joined_at.strftime("%d/%m/%Y %H:%M:%S"), True),
                
                
                ]

        for name, value, inline in fields: 
            embed.add_field(name=name, value=value, inline=inline)       
            embed.set_thumbnail(url=target.avatar_url)
        await ctx.send(embed=embed)


    @commands.command(name='Server_info', aliases=["si"])
    async def server_info(self, ctx):
        pass
        # embed = discord.Embed(title="server information",
        #                             colour=target.colour,
        #                             Timestamp=datetime.utcnow())

        # embed.set_thumbnail(url=ctx.guild.icon_url)
        


        #                         ^^ This is for pings / mentions being cleaned so you can't do `a!say @everyone`.
        #command content


def setup(bot):
   bot.add_cog(fun(bot))