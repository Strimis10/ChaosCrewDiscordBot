from discord.ext import commands
import discord
import discord.utils

class HumiliateStrimis(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='Shoot_Strimis', aliases=["humiliateStrimis"], description='bot sends video of strimis getting shot',brief='bot sends video of strimis getting shot')
    async def Shoot_Strimis(self, ctx):
        file = discord.File("bootleg_gatharu.mp4")
        await ctx.send(file=file)






def setup(bot):
    bot.add_cog(HumiliateStrimis(bot))