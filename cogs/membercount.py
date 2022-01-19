from http import client
from discord.ext import commands
import discord
import discord.utils


class Members(commands.Cog):
    def init(self, bot):
        self.bot = bot

    @commands.command(name='membercount', aliases = ["Mcount"])
    async def membercount(self, ctx):
        await ctx.send(ctx.guild.member_count)
        
def setup(bot):
    bot.add_cog(Members(bot))