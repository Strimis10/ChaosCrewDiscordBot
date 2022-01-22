##https://www.youtube.com/watch?v=k6eCJDSemu4

from datetime import datetime
from sqlite3 import Timestamp
from typing import Optional
from ast import alias
from discord.ext import commands
import discord
import discord.utils
import random



lyrics = '''Heard of a dude, that puts your mood up on a pedestal
Got me feeling better than me after eating edibles
Always on point like a decimal, we gotta let ‘em know
That you will never find a better soul than Kennevo’s

He got the vibe to make me say that guy is the bee’s knees
Aye, I love ‘em, hi Ava, Ivy and Eevee
Hope you love this song so much that you throw it on repeat
While staying hydrated drinking from BBCs

Tell me: make up or gatling, for real what kinda gun
Do you want to choose to shoot the shot before your skynet’s done
And every stroke of genius that he has is mighty fun
I said stroke, Eevee dont be calling 9 1 1


Kennevo BEEN a big bad baddy
Carrying the club better than every caddy
I use self destruct, he still helps me up
Got me laughing so much, I choke, me harder daddy'''

small_lyrics = "I choke, me harder daddy"

file = discord.File("kennevo_rough.mp3")




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





    @commands.Cog.listener()
    async def on_message(self, message):
        if "choke" in message.content.lower():
            if message.author.id != 932687176997687316:
                what = random.randint(0, 3)
                if what == 1:
                    await message.reply(f"{lyrics}: !!! SONG BY TizzyTheProphet")
                elif what == 2:
                    await message.reply(small_lyrics)
                elif what == 3 or 0:
                    await message.reply(file=file)
                    await message.reply("!!! SONG BY TizzyTheProphet")


    @commands.command(name='sus',description='sus')
    async def sus(self, ctx):
        file = discord.File("pokemon.gif")
        await ctx.send(file=file)




def setup(bot):
   bot.add_cog(fun(bot))