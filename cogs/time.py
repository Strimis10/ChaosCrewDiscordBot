from click import option
from discord import Embed
from discord.ext.commands import Bot, Cog
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from discord.ext import commands
import discord
import discord.utils

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    # @cog_ext.cog_slash(name="AM_PM_to_24h", description="converts am/pm to twentyfour hour format",guild_ids=[932684556572700773,786013884216639509,983015288910000188],
    # options=[create_option(
    #     name="option",
    #     description="Choose am or pm",
    #     required=True,
    #     option_type=3,
    #     choices=[
    #         create_choice(
    #             name="AM",
    #             value="AM"
    #         ),
    #         create_choice(
    #             name="PM",
    #             value="PM"
    #         )])]
    # )
    # async def AM_PM_to_24h(self, ctx: SlashContext, option:str, time: str):

    #     embed = Embed(title=time, footer=option)
    #     await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(fun(bot))
