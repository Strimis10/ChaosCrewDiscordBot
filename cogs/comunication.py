from discord.ext import commands
import discord
import discord.utils
import asyncio

class coms(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    
    # CHAIR COLOR:
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #

    # @commands.command(name='chair_color',description='',brief='')
    # async def say(self, ctx, *, text: commands.clean_content = ''):
        
    #     #channel = await self.bot.fetch_channel(949590152202813453)
    #     #guild= discord.utils.get(self.bot.channels, id=int(949590152202813453))
    #     user = discord.utils.get(self.bot.get_all_members(), id=427822985102098434)
    #     # print(user)
    #     # print(user.status)
    #     # print(type(user.status))
    #     # print(type(user))

    #     if str(user.status) == "offline":
    #         print("what")
    #         await ctx.send(f"{user.name} is {user.status}; request cannot be fulfilled.")
    #     elif str(user.status) == "idle":
    #         await ctx.send(f"{user.name} is {user.status}: request can but won't be fulfilled.")
    #     elif str(user.status) == "dnd":
    #         await ctx.send(f"{user.name} is in {user.status} mode (do not disturb): request can but won't be fulfilled.")
    #     elif str(user.status) == "online":
    #         await ctx.send("Request sent to DAHH")
    #         await self.bot.get_channel(949590152202813453).send(f"69 {text.lower()}: requested by: {ctx.author} (:{ctx.author.id}:) channel.id :{ctx.channel.id}")
        
        
    #     try:
    #         msg = await self.client.wait_for("message", check=check, timeout=30) # 30 seconds to reply
    #     except asyncio.TimeoutError:
    #         await ctx.send("Sorry, you didn't reply in time!")
       





    @commands.command(name='Feed_Strimis',aliases=['FS','feed_strimis'],brief='Just think Snackaru with Skittles but worse')
    async def Feed_Strimis (self, ctx):
        
        #channel = await self.bot.fetch_channel(949590152202813453)
        #guild= discord.utils.get(self.bot.channels, id=int(949590152202813453))
        user = discord.utils.get(self.bot.get_all_members(), id=427822985102098434)
        # print(user)
        # print(user.status)
        # print(type(user.status))
        # print(type(user))

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

    @commands.command(name='Water_Strimis',aliases=['WS','water_strimis'],brief='Just think hydaru but worse')
    async def Feed_Strimis (self, ctx):
        
        #channel = await self.bot.fetch_channel(949590152202813453)
        #guild= discord.utils.get(self.bot.channels, id=int(949590152202813453))
        user = discord.utils.get(self.bot.get_all_members(), id=427822985102098434)
        # print(user)
        # print(user.status)
        # print(type(user.status))
        # print(type(user))

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
        
        
        # try:
        #     msg = await self.client.wait_for("message", check=check, timeout=30) # 30 seconds to reply
        # except asyncio.TimeoutError:
        #     await ctx.send("Sorry, you didn't reply in time!")



    
            


    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id != 932687176997687316:
        # import pdb
            num = 0
            ge = False
        # pdb.set_trace()
            error = ""
            ga = ""
            h = False
            for letter in message.content:
                #print(letter)
                if letter != " ":
                    #print(letter)
                    if letter != ":":
                        error = error + letter
                elif letter == " ":

                    break

            for letter in message.content:
                #print(letter)
                if letter == ":":
                    ge = True
                elif letter != " ":
                    if ge == True:
                        ga = ga + letter
                
                elif letter == " ":
                    num = num + 1
                    if num == 2:
                        break
                # print(num)
                # print(ge)
                # print(ga)

                
            if error == "Error:":
                await self.bot.get_channel(932684556572700776).send(f"{message.content}")
            elif ga == "Feed_Strimis":
                #print("hug")
                await self.bot.get_channel(int(error)).send(f"{message.content}")
            elif ga == "Air_raid":
                #print("hug")
                await self.bot.get_channel(int(error)).send(f"{message.content}")


        

       
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #

       


def setup(bot):
    bot.add_cog(coms(bot))