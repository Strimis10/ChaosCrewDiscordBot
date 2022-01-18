from discord.ext import commands
import discord
import discord.utils

class HumiliateStrimis(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='sus',description='sus')
    async def sus(self, ctx):
        file = discord.File("james_crossdress_pokemon.gif")
        await ctx.send(file=file)






def setup(bot):
    bot.add_cog(HumiliateStrimis(bot))