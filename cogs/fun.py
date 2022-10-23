from discord.ext import commands
import discord
import discord.utils
import random
from discord_slash import cog_ext, SlashContext 
from discord_slash import SlashCommand, SlashContext



    


class funsies(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    #badly hidden Easter egg that sends a version of Kennevo rough whenerver someone says "choke me harder" 
    @commands.Cog.listener()
    async def on_message(self, message):
        if "choke me harder daddy" in message.content.lower():
            if message.author.id != 932687176997687316:
                what = random.randint(0, 3)
                if what == 3 or 0:
                    await message.reply(file=discord.File("kennevo_rough.mp3"))
                    await message.channel.send("!!! SONG BY TizzyTheProphet")


    #just a random "fun" command
    #@commands.command(name='Am_I_alive',aliases=["aia", "am_i_alive"],brief="tells you if you're dead")
    @cog_ext.cog_slash(
        name="Am_I_alive", 
        description="tells you if you're dead",
        guild_ids=[932684556572700773,786013884216639509])
    async def Am_I_alive(self, ctx):
        bpm = random.randint(0, 270)
        if bpm > 200:
            await ctx.send(f"Your heartrate is {bpm} BPM, you've strained your heart and it's now slowing down... in a minute it will have stopped.")
            await ctx.send("If you didn't already figure that out, you're dead.")
        elif bpm < 35 and bpm > 0:
            await ctx.send(f"Your heartrate is {bpm} BPM, you're not getting enough oxygen, you will soon faint, your heart will slow down more and more untill... BBBBBEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
            await ctx.send("If you didn't already figure that out, you're dead.")
        elif bpm == 0:
            await ctx.send(f"Your heartrate is {bpm} BPM, how did you even write that command?")
            await ctx.send("If you didn't already figure that out, you're dead.")
        elif bpm > 100 and bpm < 160:
            await ctx.send(f"Your heartrate is {bpm} BPM, (That is normal if you're exercising)")
        elif bpm > 160 and bpm < 200:
            await ctx.send(f"Your heartrate is {bpm} BPM, (That's very high, you should go and see a doctor)")
        elif bpm < 60 and bpm > 38:
            await ctx.send(f"Your heartrate is {bpm} BPM, (That's a normal resting rate if you're a good athleate)")
        else:
            await ctx.send(f"Your heartrate is {bpm} BPM, (That's normal)")


    

def setup(bot):
    bot.add_cog(funsies(bot))