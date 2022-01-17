from discord.ext import commands
import discord
import discord.utils

class HumiliateStrimis(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='Shoot_Strimis',description='bot sends video of strimis getting shot',brief='bot sends video of strimis getting shot')
    async def say(self, ctx):
        file = discord.File("/bootleg-gatharu.mp4")
        await ctx.send(file=file)




        #                         ^^ This is for pings / mentions being cleaned so you can't do `a!say @everyone`.
        #command content


def setup(bot):
    bot.add_cog(HumiliateStrimis(bot))