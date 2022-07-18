from discord import Embed
from discord.ext.commands import Bot, Cog
from discord_slash import cog_ext, SlashContext
from discord.ext import commands
import discord
import discord.utils

class Members(commands.Cog):
    def init(self, bot):
        self.bot = bot


    @cog_ext.cog_slash(name="membercount", description="",guild_ids=[932684556572700773,786013884216639509,983015288910000188])
    async def membercount(self, ctx: SlashContext):
        await ctx.send(f"there are {ctx.guild.member_count} members in this guild")
        
def setup(bot):
    bot.add_cog(Members(bot))