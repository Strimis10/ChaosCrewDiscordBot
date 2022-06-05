from discord import Embed
from discord.ext.commands import Bot, Cog
from discord_slash import cog_ext, SlashContext
from discord.ext import commands
import discord
import discord.utils
import json
from discord_slash import SlashCommand, SlashContext
import random

best_games = ["Portal", "Portal 2", "Aperture Desk job", "Portal Stories: Mel", "Minecraft", "Grand theft auto V"]

best_games_prompts_i_guess = ["what is the best game", "what is the greatest game", "which are the best games", "best game", "greatest game", "best games", "greatest games"]

class EightBall(commands.Cog):
    def init(self, bot):
        self.bot = bot
    #I think this one is self explanatory
    @cog_ext.cog_slash(name="8ball", 
        description="I think this one is self explanatory",
        guild_ids=[932684556572700773,786013884216639509])
    async def EightBall(self, ctx: SlashContext, text: str):
        was = False
        question = text.lower()
        await ctx.send(f'"{text}":')
        for prompt in best_games_prompts_i_guess:
            if prompt in question:
                await ctx.send(str(best_games))
                was = True
                break
        
        if was == False:
            with open("EightBall.json") as f:
                data =json.load(f)
            await ctx.send(f"{random.choice(data)}")


def setup(bot):
    bot.add_cog(EightBall(bot))
