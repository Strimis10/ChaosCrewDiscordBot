from discord.ext import commands
import discord
import discord.utils
from discord import client

class recieve(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @client.event
    async def on_message(message, ctx):
        if message.channel.id == message.author.dm_channel.id: # dm only
            ctx.send("recieved")
            pass
            # do stuff here #
        elif not message.guild: # group dm only
            pass
            # do stuff here #
        else: # server text channel
            pass
            # do stuff here #

        #if str(message.attachments) == "[]": # Checks if there is an attachment on the message
        #    return
        #else: # If there is it gets the filename from message.attachments
         #   split_v1 = str(message.attachments).split("filename='")[1]
          #  filename = str(split_v1).split("' ")[0]
           # if filename.endswith(".csv"): # Checks if it is a .csv file
            #    await message.attachments[0].save(fp="CsvFiles/{}".format(filename))


def setup(bot):
    bot.add_cog(recieve(bot))


#https://stackoverflow.com/questions/50601650/how-to-run-a-python-script-on-shutdown-of-systemwindows-7
#https://stackoverflow.com/questions/54418496/discord-py-how-do-i-send-private-message-to-someone-using-the-persons-id
#https://stackoverflow.com/questions/62075228/discord-py-on-message-but-only-for-private-messages
#https://stackoverflow.com/questions/53807024/how-would-i-detect-user-status-discord-py
#https://stackoverflow.com/questions/51853854/print-online-users-to-console-discord-py