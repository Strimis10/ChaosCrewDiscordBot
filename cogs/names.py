from click import pass_context
from discord.ext import commands
import discord
import discord.utils
from typing import Optional
import json

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(name='name_update')
    async def name_update(self, ctx):
        print(discord.Guild.members)
        # for user in discord.Guild.members:
        #     print(user)

    @commands.command(name='name',brief='?name @Strimis10 The tragical sorcerer    ---Strimis10')
    async def name(self, ctx, target: Optional[discord.Member]):
        target = target or ctx.author

        with open("names.json") as feedsjson: 
            feeds = json.load(feedsjson)

        # print(feeds)
        # print(target.id)
        # print(feeds[str(target.id)])

        
        try:
            await ctx.send(f"{target.display_name}'s old name was: {feeds[str(target.id)]}")
        except KeyError:
            await ctx.send(f"{target.display_name}'s username is: {discord.utils.get(self.bot.get_all_members(), id=target.id)}")


                
 


        # with open("date.json", mode='w') as f:
        #     f.write(json.dumps(y, indent=2))


def setup(bot):
    bot.add_cog(fun(bot))