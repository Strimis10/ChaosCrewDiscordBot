from textwrap import indent
from discord.ext import commands
import discord
import discord.utils
import json
import os
a = []



class usefull(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='Ban_word',description='Bot bans a word from being used in text chat')        
    if commands.is_owner == True or commands.has_role([786014220721979445, 786014064533831690, 933127964248375337, "Administrator", "Developers"]) == True or commands.has_permissions(administrator=True) == True:
        async def ban_word(self, ctx, *, text: commands.clean_content = ''):    
            if not os.path.isfile("banned_words.json"):
                a.append(text)
                with open("banned_words.json", mode='w') as f:
                    f.write(json.dumps(a, indent=2))
            else:
                with open("banned_words.json") as feedsjson:
                    feeds = json.load(feedsjson)

                feeds.append(text)
                for i in range(len(feeds)):
                    feeds[i] = feeds[i].lower()
                    print(feeds)
                    with open("banned_words.json", mode='w') as f:
                        f.write(json.dumps(feeds, indent=2))    




        # with open("banned_words.json", mode='w') as f:
        #     text = text.lower()
        #     f.append(text, indent=2)
            # json.dump(feeds, f)
        #  with open("banned_words.json", "r+") as file:
        #     data = json.load(file)
        #     data.update(text)
        #     file.seek(0)
        #     json.dump(data, file, indent=2)
        # with open('baned_words.json', 'w') as f:
        #     json.dump(text, f, indent=2)
       


def setup(bot):
    bot.add_cog(usefull(bot))


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
