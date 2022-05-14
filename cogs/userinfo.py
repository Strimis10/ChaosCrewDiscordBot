##https://www.youtube.com/watch?v=k6eCJDSemu4

from datetime import datetime
from typing import Optional
from discord.ext import commands
import discord
import discord.utils


class userInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    #Command for everyone to get info about a users discord account
    @commands.command(name='User_info', aliases=["ui", "Memeber_info", "mi"], breif='gives a summary of the user')
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
                ("Admin", bool(target.guild_permissions.administrator), True),
                ("User created at", target.created_at.strftime("%d/%m/%Y %H:%M:%S"), False),
                ("Joined server at", target.joined_at.strftime("%d/%m/%Y %H:%M:%S"), True)
                ]

        for name, value, inline in fields: 
            embed.add_field(name=name, value=value, inline=inline)       
            embed.set_thumbnail(url=target.avatar_url)
        await ctx.send(embed=embed)


    # @commands.command(name='Server_info', aliases=["si"])
    # async def server_info(self, ctx):
    #     pass


def setup(bot):
    bot.add_cog(userInfo(bot))




