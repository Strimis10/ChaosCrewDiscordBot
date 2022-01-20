from ast import alias
from email import message
from telnetlib import COM_PORT_OPTION
from discord.ext import commands
import discord
import discord.utils
import json




class Birthday(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='setBirthday', aliases=["setBday"])
    async def set_Birthday(self, ctx, *, text: commands.clean_content = ''):
        #                         ^^ This is for pings / mentions being cleaned so you can't do `a!say @everyone`.
            # if "date:" not in text:
            #    await ctx.send("send your birthday like this: 'dd/mm/yyyy' if you don't want to share the year type '0000' as the year. Send this with the 'setBrithday' command (?setBirthday dd/mm/yyyy)")

            # elif "date:" in text:
            print(text)
            await ctx.send("Yes")






def setup(bot):
    bot.add_cog(Birthday(bot))
    