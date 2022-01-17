from discord.ext import commands
import discord
import discord.utils

class thissaysstuff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='say',description='bot says [text]',brief='bot says [text]')
    async def say(self, ctx, *, text: commands.clean_content = ''):
        #                         ^^ This is for pings / mentions being cleaned so you can't do `a!say @everyone`.
        if text == '':
            await ctx.send("You need to say something")
        else:
            await ctx.send(text)
            await ctx.message.delete()

def setup(bot):
    bot.add_cog(thissaysstuff(bot))