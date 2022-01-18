from ast import alias
from discord.ext import commands
import discord
import discord.utils

class Birthday(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='set_Birthday', aliases=["setBday"])
    async def say(self, ctx, *, text: commands.clean_content = '', message):
        #                         ^^ This is for pings / mentions being cleaned so you can't do `a!say @everyone`.
            await ctx.send("send your birthday like this: \a dd/mm/YYYY \a if you don't want to share the year type '0000' as the year. if you if you changed your mind write 'x' to cancel. send this with the 'setBrithdayfinal' command")
       

def setup(bot):
    bot.add_cog(Birthday(bot))