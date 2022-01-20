from textwrap import indent
from discord.ext import commands
import discord
import discord.utils
import json

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='Ban_word',description='Bot bans a word from being used in text chat')
    async def say(self, ctx, *, text: commands.clean_content = ''):
        # with open('baned_words.json', 'w') as f:
        #     data = json.load(f)
        #     data.update(text)
        #     f.seek(0)
        #     json.dump(data, f, indent=2)
        with open('baned_words.json', 'w') as f:
            json.dump(text, f, indent=2)
       


def setup(bot):
    bot.add_cog(fun(bot))


# from discord.ext import commands
# import discord
# import discord.utils
# import json

# with open('states.json') as f:
#     data = json.load(f)



# for state in data['states']:
#     del state['area_codes']

# with open('new_states.json', 'w') as f:
#     json.dump(data, f, indent=2)
