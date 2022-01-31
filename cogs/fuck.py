from discord.ext import commands
import discord
import discord.utils
import random as r

from numpy import random

class Ticket(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='CreateTicket',aliases= ["createTicket","Createticket","createticket", "ct"],brief='"?ct #your question" Creates a channel with you\'re suggestion/problem')
    async def createticket(self, ctx, *, text):
        guild = ctx.guild
        text_channel_list = []
        for channel in guild.text_channels:
            text_channel_list.append(channel)
        channelname = (f"{ctx.author.name}-{random.randint(100000,999999)}")
        channel = await guild.create_text_channel(channelname)
        print(text_channel_list)
        await channel.send(f"User's Ticket message: {text}")

    #@commands.command(name='CloseTicket', aliases=['Closeticket','closeTicket',)

def setup(bot):
    bot.add_cog(Ticket(bot))