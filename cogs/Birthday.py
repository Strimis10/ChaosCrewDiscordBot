from ast import alias
from telnetlib import COM_PORT_OPTION
from discord.ext import commands
import discord
import discord.utils
import json

class Birthday(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='set_Birthday', aliases=["setBday"])
    async def set_Birthday(self, ctx, *, text: commands.clean_content = ''):
        #                         ^^ This is for pings / mentions being cleaned so you can't do `a!say @everyone`.
            await ctx.send("send your birthday like this: \a dd/mm/YYYY \a if you don't want to share the year type '0000' as the year. Send this with the 'setBrithdayfinal' command")

    @commands.command(name='setBrithdayfinal', aliases=["setBdayfinal"])
    async def setBrithdayfinal(self, ctx, *, text: commands.clean_content = ''):
        target = ctx.author
        dictionary ={
            target:{
                }} 

        json_object = json.dumps(dictionary)

        with open("sample.json", "W") as outfile:
            outfile.write(json_object)



def setup(bot):
    bot.add_cog(Birthday(bot))
    