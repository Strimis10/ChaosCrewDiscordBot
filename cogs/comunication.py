from discord.ext import commands
import discord
import discord.utils

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

    @commands.command(name='chair_color',description='',brief='')
    async def say(self, ctx, *, text: commands.clean_content = ''):
        
        #channel = await self.bot.fetch_channel(949590152202813453)
        #guild= discord.utils.get(self.bot.channels, id=int(949590152202813453))
        await ctx.send("Request sent to ")
        
        await self.bot.get_channel(949590152202813453).send(f"69:{text.lower()}: requested by: {ctx.author} :{ctx.author.id}")


    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id != 932687176997687316:
        # import pdb
        # pdb.set_trace()
            error = ""
            for letter in message.content:
                #print(letter)
                if letter != " ":
                    error = error + letter
                elif letter == " ":
                    break
            if error == "Error:":
                await self.bot.get_channel(932684556572700776).send(f"{message.content}")


        

       
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