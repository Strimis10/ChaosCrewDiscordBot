from ast import alias
from email import message
from telnetlib import COM_PORT_OPTION
from discord.ext import commands
import discord
import discord.utils
import json
import os

a = {}



class Birthday(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='setBirthday', aliases=["setBday"])
    async def set_Birthday(self, ctx, *, text: commands.clean_content = ''):
        #                         ^^ This is for pings / mentions being cleaned so you can't do `a!say @everyone`.
            # if "date:" not in text:
            #    await ctx.send("send your birthday like this: 'dd/mm/yyyy' if you don't want to share the year type '0000' as the year. Send this with the 'setBrithday' command (?setBirthday dd/mm/yyyy)")

            # elif "date:" in text:
            print(text)
            if text == '':
                await ctx.send("send your birthday like this: 'dd/mm/yyyy' if you don't want to share the year type '0000' as the year. Send this with the 'setBrithday' command (?setBirthday dd/mm/yyyy)")
            elif text[2] != "/":
                await ctx.send("send your birthday like this: 'dd/mm/yyyy' if you don't want to share the year type '0000' as the year. Send this with the 'setBrithday' command (?setBirthday dd/mm/yyyy)")
            elif text[5] != "/":
                await ctx.send("send your birthday like this: 'dd/mm/yyyy' if you don't want to share the year type '0000' as the year. Send this with the 'setBrithday' command (?setBirthday dd/mm/yyyy)")
            #for number in range(5, 9):
            #    if text[number] != 
            #elif text[10] != ".":
            #   await ctx.send("send your birthday like this: 'dd/mm/yyyy.' if you don't want to share the year type '0000' as the year. Send this with the 'setBrithday' command (?setBirthday dd/mm/yyyy.)")

            else:
                if not os.path.isfile("birthdays.json"):
                    a[ctx.author.name] = text
                    with open("birthdays.json", mode='w') as f:
                        f.write(json.dumps(a, indent=2))
                    await ctx.send(f"{ctx.author.name}'s birthday set to {f[ctx.author.name]}")
                else: 
                    with open("birthdays.json") as feedsjson: 
                        feeds = json.load(feedsjson)

                    feeds[ctx.author.name] = text
                    for i in range(len(feeds)):
                        feeds[i] = feeds[i].lower()
                        print(feeds)
                        with open("birthdays.json", mode='w') as f:
                            f.write(json.dumps(feeds, indent=2))  
                    await ctx.send(f"{ctx.author.name}'s birthday set to {feeds[ctx.author.name]}")




def setup(bot):
    bot.add_cog(Birthday(bot))
    