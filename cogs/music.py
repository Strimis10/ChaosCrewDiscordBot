from discord.ext import commands
import discord
import discord.utils

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx):
        connected = ctx.author.voice
        if connected:
            await connected.channel.connect()
    @commands.command(pass_context=True)
    async def leave(self, ctx):
        connected = ctx.author.voice
        if connected:
            await connected.channel.disconnect()

def setup(bot):
    bot.add_cog(fun(bot))