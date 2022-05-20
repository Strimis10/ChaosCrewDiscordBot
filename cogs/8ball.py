from discord.ext import commands
import discord
import discord.utils
import json
import random
from discord_slash import cog_ext, SlashContext 
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option

class EightBall(commands.Cog):
    def init(self, bot):
        self.bot = bot
        #I think this one is self explanatory
    
#     @cog_ext.cog_slash(
#     name="8ball", 
#     description="",
#     guild_ids=[932684556572700773,786013884216639509]
# #     options=[create_option(
# #         name="option",
# #         description="choose your word",
# #         required=True,
# #         option_type=3,
# #         choices=[
# #             create_choice(
# #                 name="world",
# #                 value="World"
# #             ),
# #             create_choice(
# #                 name="you",
# #                 value="You"
# #             )   
# #     ]
# # )]
# )
    @commands.command(name='8ball', aliases = ["EightBall"])
    async def EightBall(self, ctx, text: commands.clean_content = ''):
        with open("EightBall.json") as f:
            data =json.load(f)
        await ctx.send(f"{random.choice(data)}")


def setup(bot):
    bot.add_cog(EightBall(bot))
