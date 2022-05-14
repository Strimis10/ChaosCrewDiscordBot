from discord.ext import commands
import discord
import discord.utils
import asyncio

class coms(commands.Cog):
    def __init__(self, bot):
        self.bot = bot






    #Command for everyone to activate Strimis's bootleg Snackaru
    @commands.command(name='Feed_Strimis',aliases=['FS','feed_strimis'],brief='Just think Snackaru with Skittles but worse')
    async def Feed_Strimis(self, ctx):
        

        user = discord.utils.get(self.bot.get_all_members(), id=427822985102098434)

        if str(user.status) == "offline":
            print("what")
            await ctx.send(f"{user.name} is {user.status}; request cannot be fulfilled.")
        elif str(user.status) == "idle":
            await ctx.send(f"{user.name} is {user.status}: request can but won't be fulfilled.")
        elif str(user.status) == "dnd":
            await ctx.send(f"{user.name} is in {user.status} mode (do not disturb): request can but won't be fulfilled.")
        elif str(user.status) == "online":
            await ctx.send("Request sent to DAHH")
            await self.bot.get_channel(949590152202813453).send(f"69Feed_Strimis: requested by: {ctx.author} (:{ctx.author.id}:) channel.id :{ctx.channel.id}")


    #Command for everyone to activate Strimis's bootleg Hydaru
    @commands.command(name='Water_Strimis',aliases=['WS','water_strimis'],brief='Just think hydaru but worse')
    async def Water_Strimis(self, ctx):

        user = discord.utils.get(self.bot.get_all_members(), id=427822985102098434)


        if str(user.status) == "offline":
            print("what")
            await ctx.send(f"{user.name} is {user.status}; request cannot be fulfilled.")
        elif str(user.status) == "idle":
            await ctx.send(f"{user.name} is {user.status}: request can but won't be fulfilled.")
        elif str(user.status) == "dnd":
            await ctx.send(f"{user.name} is in {user.status} mode (do not disturb): request can but won't be fulfilled.")
        elif str(user.status) == "online":
            await ctx.send("Request sent to DAHH")
            await self.bot.get_channel(949590152202813453).send(f"69Water_Strimis: requested by: {ctx.author} (:{ctx.author.id}:) channel.id :{ctx.channel.id}")




    
            


    #Handels respnses from the "robot server"
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id != 932687176997687316:
            num = 0
            ge = False
            error = ""
            ga = ""
            h = False
            for letter in message.content:
                if letter != " ":
                    if letter != ":":
                        error = error + letter
                elif letter == " ":

                    break

            for letter in message.content:
                if letter == ":":
                    ge = True
                elif letter != " ":
                    if ge == True:
                        ga = ga + letter
                
                elif letter == " ":
                    num = num + 1
                    if num == 2:
                        break
                
            if error == "Error:":
                await self.bot.get_channel(932684556572700776).send(f"{message.content}")
            elif ga == "Feed_Strimis":
                await self.bot.get_channel(int(error)).send(f"{message.content}")
            elif ga == "Air_raid":
                await self.bot.get_channel(int(error)).send(f"{message.content}")


def setup(bot):
    bot.add_cog(coms(bot))