from discord.ext import commands
import discord
import discord.utils
import random

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='Am_I_alive',aliases=["aia", "am_i_alive"],brief="tells you if you're dead")
    async def say(self, ctx, *, text: commands.clean_content = ''):
        bpm = random.randint(0, 270)
        if bpm > 200:
            await ctx.send(f"Your heartrate is {bpm} BPM, you've strained your heart and it's now slowing down... in a minute it will have stopped.")
            await ctx.send("If you didn't already figure that out; you're dead. The entire DEV team sends their condolences")
        elif bpm < 35 and bpm > 0:
            await ctx.send(f"Your heartrate is {bpm} BPM, you're not getting enough oxygen, you will soon faint, your heart will slow down more and more untill... BBBBBEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
            await ctx.send("If you didn't already figure that out; you're dead. The entire DEV team sends their condolences")
        elif bpm == 0:
            await ctx.send(f"Your heartrate is {bpm} BPM, how did you even write that command?")
            await ctx.send("If you didn't already figure that out; you're dead. The DEV team sends their condolences")
        elif bpm > 100 and bpm < 160:
            await ctx.send(f"Your heartrate is {bpm} BPM, (That is normal if you're exercising)")
        elif bpm > 160 and bpm < 200:
            await ctx.send(f"Your heartrate is {bpm} BPM, (That's very high, you should go and see a doctor)")
        elif bpm < 60 and bpm > 38:
            await ctx.send(f"Your heartrate is {bpm} BPM, (That's a normal resting rate if you're a good athleate)")
        else:
            await ctx.send(f"Your heartrate is {bpm} BPM, (That's normal)")


    

def setup(bot):
    bot.add_cog(fun(bot))