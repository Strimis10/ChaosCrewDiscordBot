
from discord.ext import commands
import discord
import discord.utils
from discord.ext.commands import bot, Bot
from discord import Member

class HumiliateStrimis(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    #@commands.command(name='Shoot_Strimis')
    #async def Shoot_Strimis(ctx):


    #    for user in ctx.guild.members:
     #       if user.status != discord.Status.offline:
      #          if user.id == 427822985102098434:
       #             print (user.name+"#"+user.discriminator)
    #@commands.command(pass_context=True, name='Shoot_Strimis')
    #async def Shoot_Strimis(ctx, member: 427822985102098434):
    #    print(str(member.status))

    #@Bot.command(pass_context=True, name='Shoot_Strimis', aliases=["humiliateStrimis"], brief='bot sends video of strimis getting shot')
    #async def Shoot_Strimis(ctx, member: Member):
    #    await Bot.say(str(member.status))
        #file = discord.File("bootleg_gatharu.mp4")
        #await ctx.send(file=file)






def setup(bot):
    bot.add_cog(HumiliateStrimis(bot))