from discord.ext import commands
import discord
import discord.utils
from typing import Optional
import functions
import json
import os
Strimis = "<@427822985102098434>"

class twitch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    #Command for everyone to link thier twitch account to thier discord account
    @commands.command(name='link_twitch',brief='''"?lt [Twitch_username]" links your twitch account to your discord account ''',aliases=["lt"])
    async def Link_twitch(self, ctx, *, text: commands.clean_content = ''):
        try:
            twitch_id = functions.get_info(text)
            with open("user_info.json") as feedsjson: 
                feeds = json.load(feedsjson)
            try:
                k = feeds[str(ctx.author.id)]["twitch_id"]
                await ctx.send("You already have a twitch account linked to your discord account, if you need to change it please contact Strimis10#1439")
                
            except:
                available = True
                for user in feeds:
                    try:
                        print(feeds[user]["twitch_id"])
                        if feeds[user]["twitch_id"] == int(twitch_id):
                            available = False     
                    except:
                        pass
                    if available == False:
                        break

                if available:
                    feeds[str(ctx.author.id)]["twitch_id"] = int(twitch_id)
                    await ctx.send(f"{ctx.author.id} has been linked to {twitch_id}")
                else:
                    await ctx.send("That twitch account is already linked to another discord account")
            with open("user_info.json", mode='w') as f:
                f.write(json.dumps(feeds, indent=2))
                
        except IndexError:
            await ctx.send("Invalid username")
            raise IndexError
        except:
            await ctx.send(f"{Strimis} Error")



                


def setup(bot):
    bot.add_cog(twitch(bot))