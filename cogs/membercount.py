from discord.ext import commands
import discord
import discord.utils


class Members(commands.Cog):
    def init(self, bot):
        self.bot = bot

    @commands.command(name='membercount')
    async def membercount(self, ctx):
        await ctx.send(ctx.guild.member_count)
    #    print(ctx.guild.member_count)
    #    await ctx.send(f'test{len(ctx.guild.member_count)}')
    # @commands.command(name='membercount')
    # async def get_guild_member_count(guild, self, ctx):
    #     """ returns the member count of a guild """
    #     ctx.send(len(guild.members))



def setup(bot):
    bot.add_cog(Members(bot))
