from discord.ext import commands
import discord
import discord.utils
import requests
import json


class id(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='id',description='bot says [text]',brief='bot says [text]')
    async def say(self, ctx, *, text: commands.clean_content = ''):
        
        client_id = ''
        client_secret = ''
        streamer_name = 'Kennevo'

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

        print(headers)

        stream = requests.get('https://api.twitch.tv/helix/streams?user_login=' + streamer_name, headers=headers)

        stream_data = stream.json()

        print(stream_data)

        if len(stream_data['data']) == 1:
            print(streamer_name + ' is live: ' + stream_data['data'][0]['title'] + ' playing ' + stream_data['data'][0]['game_name'])
        else:
            print(streamer_name + ' is not live')



def setup(bot):
    bot.add_cog(id(bot))


