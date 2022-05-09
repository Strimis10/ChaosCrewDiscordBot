from discord.ext import commands
import discord
import discord.utils
from typing import Optional



import get_twitch_info
import json
import os
Strimis = "<@427822985102098434>"

class twitch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='link_twitch',brief='''"?lt [Twitch_username]" links your twitch account to your discord account ''',aliases=["lt"])
    async def Link_twitch(self, ctx, *, text: commands.clean_content = ''):
        
        try:
            twitch_id = get_twitch_info.get_info(text)
            
            
            
            
                
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


        # if twitch_id == None:
        #     await ctx.send("Invalid username")
        # else:
        #     await ctx.send(f"Linked {text} to {ctx.author.id}")
        #     with open('twitch_links.json', 'r') as f:
        #         data = json.load(f)
        #     data[str(ctx.author.id)] = twitch_id
    # @commands.command(name='admin_link_twitch',brief='"?alt @strimis10 "[Twitch_username]" links the twitch account to the discord account',aliases=["alt"])
    # async def Link_twitch(self, ctx, *, target: Optional[discord.Member], text: commands.clean_content = ''):
    #     member = discord.utils.get(self.bot.get_all_members(), id=ctx.author.id)
    #     print(text)

    #     roles = [933127964248375337, 932684901801660526, 786014220721979445]

    #     for role in member.roles:
    #         if role.id in roles:
    #             permission = True
    #             break

    #         else:
    #             permission = False
    #     if ctx.author.id == 427822985102098434:
    #         permission = True
        
        
    #     if permission == True:
    #         try:
    #             twitch_id = get_twitch_info.get_info(text)
                
                
                
    #             if not os.path.isfile("twitch_ids.json"):
    #                 e = {}
    #                 e[str(target.id)] = twitch_id
                    
    #                 with open("twitch_ids.json", mode='w') as f:
    #                     f.write(json.dumps(e, indent=2))
    #             else:
                    
    #                 with open("twitch_ids.json") as feedsjson: 
    #                     feeds = json.load(feedsjson)

    #                 feeds[str(target.id)] = twitch_id

    #                 with open("twitch_ids.json", mode='w') as f:
    #                     f.write(json.dumps(feeds, indent=2))
    #             await ctx.send(f"{target.id} has been linked to {twitch_id}")  
                    
    #         except IndexError:
    #             await ctx.send("Invalid username")
    #             raise IndexError
    #         except:
    #             await ctx.send(f"{Strimis} Error")
                


def setup(bot):
    bot.add_cog(twitch(bot))