from discord.ext import commands
import discord
import discord.utils
import random


lyrics = '''Heard of a dude, that puts your mood up on a pedestal
Got me feeling better than me after eating edibles
Always on point like a decimal, we gotta let ‘em know
That you will never find a better soul than Kennevo’s

He got the vibe to make me say that guy is the bee’s knees
Aye, I love ‘em, hi Ava, Ivy and Eevee
Hope you love this song so much that you throw it on repeat
While staying hydrated drinking from BBCs

Tell me: make up or gatling, for real what kinda gun
Do you want to choose to shoot the shot before your skynet’s done
And every stroke of genius that he has is mighty fun
I said stroke, Eevee dont be calling 9 1 1


Kennevo BEEN a big bad baddy
Carrying the club better than every caddy
I use self destruct, he still helps me up
Got me laughing so much, I choke, me harder daddy'''
    
small_lyrics = "I choke, me harder daddy"
    
file = discord.File("kennevo_rough.mp3")

class Listener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.Cog.listener()
    async def on_message(self, message):
        if "choke me harder" in message.content.lower():
            if message.author.id != 932687176997687316:
                what = random.randint(0, 3)
                if what == 1:
                    await message.reply(f"{lyrics}: !!! SONG BY TizzyTheProphet")
                elif what == 2:
                    await message.reply(small_lyrics)
                elif what == 3 or 0:
                    await message.reply(file=file)
                    await message.channel.send("!!! SONG BY TizzyTheProphet")
                    await message.reply("https://www.twitch.tv/tizzytheprophet")
                    
                    


def setup(bot):
    bot.add_cog(Listener(bot))