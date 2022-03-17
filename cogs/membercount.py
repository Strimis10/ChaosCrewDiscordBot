from http import client
from discord.ext import commands
import discord
import discord.utils


class Members(commands.Cog):
    def init(self, bot):
        self.bot = bot

    @commands.command(name='membercount', aliases = ["Mcount", "mcount", "mc"])
    async def membercount(self, ctx):
        await ctx.send(f"there are {ctx.guild.member_count} members in this guild")
        
def setup(bot):
    bot.add_cog(Members(bot))