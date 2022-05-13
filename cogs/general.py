from discord.ext import commands
import discord
import discord.utils
import json

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id != self.bot.user.id:
            with open("user_info.json") as oj: 
                feeds = json.load(oj)
            if str(message.author.id) not in feeds:
                
                feeds[message.author.id] = {"new":420.69}
                with open("user_info.json", mode='w') as f:
                    f.write(json.dumps(feeds, indent=2))
                with open("user_info.json") as oj: 
                    feeds = json.load(oj)
                feeds[str(message.author.id)]["name"] = message.author.name
                feeds[str(message.author.id)]["id"] = message.author.id
                feeds[str(message.author.id)]["word_immunity"] = False
                with open("user_info.json", mode='w') as f:
                    f.write(json.dumps(feeds, indent=2))


def setup(bot):
    bot.add_cog(fun(bot))
    
    
    