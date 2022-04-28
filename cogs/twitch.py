from discord.ext import commands
import discord
import discord.utils
import get_twitch_info
import json

class twitch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='Link_twitch',brief='''links your twitch account to your discord account, ?lt [Twitch_username]''',aliases=["lt"])
    async def Link_twitch(self, ctx, *, text: commands.clean_content = ''):
        twitch_id = get_twitch_info.get_info(text)
        if twitch_id == None:
            await ctx.send("Invalid username")
        else:
            await ctx.send(f"Linked {text} to {ctx.author.id}")
            with open('twitch_links.json', 'r') as f:
                data = json.load(f)
            data[str(ctx.author.id)] = twitch_id
            


def setup(bot):
    bot.add_cog(twitch(bot))