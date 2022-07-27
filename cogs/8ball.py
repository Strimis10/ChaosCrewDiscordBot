from discord import Embed
from discord.ext.commands import Bot, Cog
from discord_slash import cog_ext, SlashContext
from discord.ext import commands
import discord
import discord.utils
import json
from discord_slash import SlashCommand, SlashContext
import random

best_games = ["Portal", "Portal 2", "Aperture Desk job", "Portal Stories: Mel", "Minecraft", "Grand theft auto V", "Super Mario bros 3"]

best_games_prompts_i_guess = ["what is the best game", "what is the greatest game", "which are the best games", "best game", "greatest game", "best games", "greatest games"]

class EightBall(commands.Cog):
    def init(self, bot):
        self.bot = bot
    #I think this one is self explanatory
    @cog_ext.cog_slash(name="8ball", 
        description="I think this one is self explanatory",
        guild_ids=[932684556572700773,786013884216639509,983015288910000188])
    async def EightBall(self, ctx: SlashContext, text: str):
        was = False
        question = text.lower().removesuffix("?")
        print(question)
        
        if question in best_games_prompts_i_guess:
            await ctx.send(f'"{text}": {str(best_games)}')
            was = True

        
        else:
            with open("jsons/EightBall.json") as f:
                data =json.load(f)
            await ctx.send(f'"{text}": {random.choice(data)}')
            


def setup(bot):
    bot.add_cog(EightBall(bot))
