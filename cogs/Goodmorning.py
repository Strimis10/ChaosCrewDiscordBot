from discord.ext import commands
import discord
import discord.utils

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith("Good morning"):
            if message.author.id != 932687176997687316:
                await message.reply("Good morning")


def setup(bot):
    bot.add_cog(fun(bot))


