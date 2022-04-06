import json
from discord.ext import commands
import discord
import discord.utils
json

class dead(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id != 932687176997687316:
            with open("last_active.json") as feedsjson: 
                data = json.load(feedsjson)
            data[f"{message.author.id}"] = 0
            with open("last_active.json", mode='w') as f:
                f.write(json.dumps(data, indent=2)) 
                
        
      


def setup(bot):
    bot.add_cog(dead(bot))