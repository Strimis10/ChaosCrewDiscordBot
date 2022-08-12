from discord import Embed
from discord.ext.commands import Bot, Cog
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from discord.ext import commands
import discord
import discord.utils
import json




class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot






    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == 786013884737781872:
            h12 = False
            h24 = False
            istimezone = False
            splited =  message.content.lower().split(" ")

            if message.content.lower().startswith("timezone"):
                istimezone = True
            elif message.content.lower().startswith("good") and splited[1] == "timezone":
                istimezone = True
            
            if istimezone:
                time = ""
                for character in message.content.lower():
                    if character.isdigit():
                        time += character
                    elif character == ":": 
                        time += character
                    elif not character.isdigit():
                        if ":" in time:
                            break


                if len(message.content.lower()) > 14:
                    one = 0
                    for word in splited:
                        ampm = ["am", "pm"]
                        if splited[one] in ampm:
                            if one > 2:
                                h24 = True
                        one += 1
                            

                if not h24:
                    if "am" in message.content.lower():
                        h12 = "am"
                    elif "pm" in message.content.lower():
                        h12 = "pm"
                    elif len(time) == 5:
                        h24 = True
                


                timezone = 0
                try:
                    if h24:
                        from TimezoneTimeFinder import TimezoneTimeFinder24h
                        timezone = TimezoneTimeFinder24h.getTimezone(time)
                        
                    elif h12 != False:
                        if len(time) == 4:
                            time = f"0{time}"
                        from TimezoneTimeFinder import TimezoneTimeFinder12h
                        timezone = TimezoneTimeFinder12h.getTimezone(time,AmPm=h12)
                        
                    
                except:
                    pass
                if timezone != 0:
                    with open("jsons/user_info.json") as fj: 
                        feeds = json.load(fj)

                    if type(feeds[str(message.author.id)]["Timezone"]) != list:
                        feeds[str(message.author.id)]["Timezone"] = []
                    feeds[str(message.author.id)]["Timezone"].append(timezone)

                    if len(feeds[str(message.author.id)]["Timezone"]) >= 5:
                        feeds[str(message.author.id)]["Timezone"].pop(0)
                    
                    with open("jsons/user_info.json", mode='w') as f:
                        f.write(json.dumps(feeds, indent=2))
                    print(timezone)
                        
                    #print(max(feeds[str(message.author.id)]["Timezone"], key = feeds[str(message.author.id)]["Timezone"].count))




            # split = message.content.lower().split(" ")
            # if len(split) > 1:
            #     split.remove("timezone")
            #     print(split)


def setup(bot):
    bot.add_cog(fun(bot))
