from discord.ext import commands
import discord
import discord.utils


class Members(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='membercount')
    async def members(self, ctx, member):
        guild = member.guild
        await ctx.send(f'test{len(guild.member_count)}')




def setup(bot):
    bot.add_cog(Members(bot))
