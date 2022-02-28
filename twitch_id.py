from discord.ext import commands
import discord
import discord.utils
#import get
import requests
import json

class twitch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='id',description='bot says [text]',brief='bot says [text]')
    async def say(self, ctx, *, text: commands.clean_content = ''):
        # GET https://api.twitch.tv/helix/users?login=<username>

        if text == '':
            ctx.send("you need to send your Twitch username")
        
        else:

            client_id = text
            client_secret = '(secret)'
            streamer_name = 'sasdaasdsdasad'

            body = {
                'client_id': client_id,
                'client_secret': client_secret,
                "grant_type": 'client_credentials'
            }
            r = requests.post('https://id.twitch.tv/oauth2/token', body)

            #data output
            keys = r.json()

            print(keys)

            headers = {
                'Client-ID': client_id,
                'Authorization': 'Bearer ' + keys['access_token']
            }
            r= requests.get("https://api.twitch.tv/helix/streams?user_login=kitboga",headers=headers)
            q=json.loads(r.text)

            print(q)


        #                         ^^ This is for pings / mentions being cleaned so you can't do `a!say @everyone`.
        #command content

def setup(bot):
    bot.add_cog(twitch(bot))


