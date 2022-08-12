from ast import alias
import os
##install all the modules from dependencies.txt (basically only used for the server)
#os.system("pip install -r dependencies.txt")
import discord
#Kill me
from discord.ext import commands
import json
from discord import Embed
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from dotenv import load_dotenv
client = commands.Bot(command_prefix="?",owner_ids=[427822985102098434, 386826952599928842], intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True, sync_on_cog_reload=True)


load_dotenv()

token = ""

token = os.getenv("TOKEN") #get_token()

print('''  
  /$$$$$$$                                      /$$                   /$$    
 | $$__  $$                                    | $$                  | $$    
 | $$  \ $$  /$$$$$$  /$$    /$$ /$$$$$$       | $$$$$$$   /$$$$$$  /$$$$$$  
 | $$  | $$ |____  $$|  $$  /$$//$$__  $$      | $$__  $$ /$$__  $$l_  $$_/  
 | $$  | $$  /$$$$$$$ \  $$/$$/| $$$$$$$$      | $$  \ $$| $$  \ $$  | $$    
 | $$  | $$ /$$__  $$  \  $$$/ | $$_____/      | $$  | $$| $$  | $$  | $$ /$$
 | $$$$$$$/|  $$$$$$$   \  $/  |  $$$$$$$      | $$$$$$$/|  $$$$$$/  |  $$$$/
 |_______/  \_______/    \_/    \_______/      |_______/  \______/    \___/  ''')




@slash.slash(
name="hello", 
description="sends test message",
guild_ids=[932684556572700773,786013884216639509, 983015288910000188, 949590152202813450],
options=[create_option(
        name="option",
        description="choose your word",
        required=True,
        option_type=3,
        choices=[
            create_choice(
                name="world",
                value="World"
            ),
            create_choice(
                name="you",
                value="You"
            )
    ]
)]

)
async def hello(ctx: SlashContext, option: str):
    embed = Embed(title=option)
    await ctx.send(embed=embed)


@client.event
async def on_ready():
    print("Setting status from previous")
    with open('jsons/Presence.json', 'r') as json_file:
        data = json.load(json_file)
        if data["type"] == "streaming":
            await client.change_presence(activity=discord.Streaming(name=data["text"], url='https://twitch.tv/kennevo'))
            
        elif data["type"] == "watching":
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=data["text"]))
        
        elif data["type"] == "listening":
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=data["text"]))
        
        elif data["type"] == "playing":
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=data["text"]))
        else:
            print("No status to restore")

    print("Ready")



'''
@client.event 
async def on_command_error(ctx, error):
    channel = client.get_channel(1001880128269320335)
    await channel.send(f"```ctx: {ctx}\nerror: {error}```")
'''

# @client.event
# async def on_command_error(ctx, error):
#     channel = client.get_channel(1001880128269320335)
#     errortext = repr(error)
#     if "is not found" in errortext:
#         pass
#     else:
#         await channel.send(f"```ctx: {ctx}\nerror: {error}```")

@client.command(name="exception", aliases=["except","e"])
@commands.is_owner()
async def exception(ctx):
    await ctx.send("throwing an exception your way")
    raise TypeError

@client.command(name="restart")
@commands.is_owner()
async def restart(ctx):
    await ctx.send("Restarting")
    os.system("python main.py")


    
@client.command(name="set")
@commands.is_owner()
async def _set(ctx, *, args):
        args = args.split(' ')
        typeof = args.pop(0)
        args = ' '.join(args)
        # make the bot have the streaming activity with the text being the args, set the url to twitch.tv/kennevo
        
        
        if typeof == "streaming":
            await client.change_presence(activity=discord.Streaming(name=args, url='https://twitch.tv/kennevo'))
            await ctx.channel.send('Set the streaming activity to: ' + args)
            statusDict = {"type" : typeof,
                        "text" : args}
            with open('jsons/Presence.json', 'w') as json_file:
                json.dump(statusDict, json_file)
        
        
        elif typeof == "watching":
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=args))
            await ctx.channel.send('Set the watching activity to: ' + args)
            statusDict = {"type" : typeof,
                        "text" : args}
            with open('jsons/Presence.json', 'w') as json_file:
                json.dump(statusDict, json_file)
        
        
        elif typeof == "listening":
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=args))
            await ctx.channel.send('Set the listening activity to: ' + args)
            statusDict = {"type" : typeof,
                        "text" : args}
            with open('jsons/Presence.json', 'w') as json_file:
                json.dump(statusDict, json_file)
        
        elif typeof == "playing":
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=args))
            await ctx.channel.send('Set the playing activity to: ' + args)
            statusDict = {"type" : typeof,
                        "text" : args}
            with open('jsons/Presence.json', 'w') as json_file:
                json.dump(statusDict, json_file)
        
        elif typeof == "clear":
            await ctx.channel.send('Cleared the activity')
            await client.change_presence(activity=None)
            statusDict = {"type" : "N/A",
                        "text" : "N/A"}
            with open('jsons/Presence.json', 'w') as json_file:
                json.dump(statusDict, json_file)
        
        else:
            await ctx.channel.send(f"Type ( `{typeof}` ) or Args ( `{args}` ) are not valid. Try again.")


@client.command(name='kill', aliases=['k'])
@commands.is_owner()
async def kill(ctx):
    await ctx.send("Breaking")
    await client.close()
    print('''
    
                                                   -----
                                                 /      \\
                                                 )      |
          :================:                      "    )/
         /||              ||                      )_ /*
        / ||   Dave is    ||                          *
       |  ||     Down     ||                   (=====~*~======)
        \ ||   Goodbye    ||                  0      \ /       0
          ==================                //   (====*====)   ||
   ........... /      \.............       //         *         ||
   :\        ############            \    ||    (=====*======)  ||
   : ---------------------------------     V          *          V
   : |  *   |__________|| ::::::::::  |    o   (======*=======) o
   \ |      |          ||   .......   |    \\         *         ||
     --------------------------------- 8   ||   (=====*======)  //
                                        8   V         *         V
     --------------------------------- 8   =|=;  (==/ * \==)   =|=
     \   ###########################  \   / ! \     _ * __    / | \\
      \  +++++++++++++++++++++++++++   \  ! !  !  (__/ \__)  !  !  !
       \ ++++++++++++++++++++++++++++   \        0 \ \V/ / 0
        \________________________________\     ()   \o o/   ()
         *********************************     ()           ()
    ''')



@client.command(name='reload',aliases=["r"])
@commands.is_owner()
async def reload(ctx, extension):
    try:
        msg = await ctx.send(f'Reloading {extension}...')
        client.reload_extension(f'cogs.{extension}')
        await msg.edit(content=f"Reloaded {extension} succesfully")
    except Exception as error:
        await ctx.send(f'Error:\n```py\n{error}\n```')




@client.command(name='load', aliases=['l'])
@commands.is_owner()
async def load(ctx, extension):
    try:
        msg = await ctx.send(f'Loading {extension}...')
        client.load_extension(f'cogs.{extension}')
        await msg.edit(content=f"Loaded {extension} succesfully")
    except Exception as error:
        await ctx.send(f'Error:\n```py\n{error}\n```')



@client.command(name='unload', aliases=['u'])
@commands.is_owner()
async def unload(ctx, extension):
    try:
        msg = await ctx.send(f'Unloading {extension}...')
        client.unload_extension(f'cogs.{extension}')
        await msg.edit(content=f"Unloaded {extension} succesfully")
    except Exception as error:
        await ctx.send(f'Error:\n```py\n{error}\n```')





@client.command()
async def ping(ctx):
     await ctx.send(f'Pong! In {round(client.latency * 1000)}ms')


@client.command(name='Kennevo_rough', aliases=["kennevo_rough", "kr"])
@commands.is_owner()
async def Kennevo_rough(ctx):
    file = discord.File("kennevo_rough.mp3")
    await ctx.send(file=file)
    await ctx.send("!!! SONG BY TizzyTheProphet")


@client.command(name="admin_say", aliases = ["adminsay", "asay"])
@commands.is_owner()
async def admin_say(ctx, *, text: commands.clean_content = ''):
    await ctx.send(text)
    await ctx.message.delete()

@client.command(name='reloadall', aliases=['rla'])
@commands.is_owner()
async def reloadall(ctx):
        msg = await ctx.send(f"Reloading...")
        for filename in os.listdir('./cogs'):
                if filename.endswith('.py'):
                    try:
                        client.reload_extension(f'cogs.{filename[:-3]}')
                    except Exception as error:
                        await ctx.send(f'This cog couldn\'t be Reloaded :(\n```py\n{error}\n```')
        await msg.edit(content="Reloaded all extensions successfully")



# @client.command(name='Master_reloadall', aliases=['mrla'])
# @commands.is_owner()
# async def reloadall(ctx):
#         await client.get_channel(949590152202813453).send(f"69Master_reloadall")
#         msg = await ctx.send(f"Reloading...")
#         for filename in os.listdir('./cogs'):
#                 if filename.endswith('.py'):
#                     try:
#                         client.reload_extension(f'cogs.{filename[:-3]}')
#                     except Exception as error:
#                         await ctx.send(f'This cog couldn\'t be Reloaded :(\n```py\n{error}\n```')
#         await msg.edit(content="Reloaded all extensions successfully")


@client.command(name='loadall', aliases=['la'])
@commands.is_owner()
async def loadall(ctx):
        msg = await ctx.send(f"Unloading")
        for filename in os.listdir('./cogs'):
                if filename.endswith('.py'):
                    try:
                        client.load_extension(f'cogs.{filename[:-3]}')
                    except Exception as error:
                        await ctx.send(f'This cog couldn\'t be loaded :(\n```py\n{error}\n```')
        await msg.edit(content="Loaded all extensions successfully")

@client.command(name='unloadall', aliases=['ula'])
@commands.is_owner()
async def unloadall(ctx):
        msg = await ctx.send(f"Unloading")
        for filename in os.listdir('./cogs'):
                if filename.endswith('.py'):
                    try:
                        client.unload_extension(f'cogs.{filename[:-3]}')
                    except Exception as error:
                        await ctx.send(f'This cog couldn\'t be unloaded :(\n```py\n{error}\n```')
        await msg.edit(content="Unloaded all extensions successfully")


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        try:
            client.load_extension(f'cogs.{filename[:-3]}')
            print(f"Loaded {filename}")
        except Exception as e:
            print(f'\n!!!!!!!!!!!!!!!\nuwu you did a fuckie wuckie\n{e}\n!!!!!!!!!!!!!!!\n')


#adds the new user to the user_info.json file 
@client.event
async def on_member_remove(member):
    channel = client.get_channel(919347348012933191)
    await channel.send(f"@{member} left. :(")
    
@client.event
async def on_member_join(member):
    import what_server
    if what_server.Kennevo:
        guild = discord.utils.get(client.guilds, id=int(786013884216639509))
        role = discord.utils.get(guild.roles, id=int(953004596882702386))

    else:
        guild= discord.utils.get(client.guilds, id=int(932684556572700773))
        role = discord.utils.get(guild.roles, id=int(946936153687347230))

    

    with open("jsons/user_info.json") as fj: 
        feeds = json.load(fj)
        
    #checks if the user is already in the user_info.json file
    #if so it will do nothing
    
    if str(member.id) in feeds:
        print(f"{feeds[str(member.id)]['name']} has rejoined")
        
    
    #else it'll add the user to the user_info.json file and give them the "new_user" role


    else:
        #send welcome message to the new user
        print(f"{member} has joined the server")
        embed=discord.Embed(title=f"Welcome {member.name}", description=f'''Hey! Kenny Here!!
        Thanks for joining {guild.name}, read the rules in <#799334905569345606> and enjoy your stay!!\n
        Just wanted to remind you to visit the <#919356311043444847> channel in the discord to set your own notifications preferences! Please let me know what you'd like to get pings for so I don't spam you (I hate spamming people).
        Welcome to the server!''')
        embed.set_thumbnail(url=guild.icon_url)
        await member.send(embed=embed)

        feeds[int(member.id)] = {"new":1}

        with open("jsons/user_info.json", mode='w') as f:
            f.write(json.dumps(feeds, indent=2))
        await member.add_roles(role)

        with open("jsons/user_info.json") as fj: 
            feeds = json.load(fj)
        feeds[str(member.id)]["name"] = member.name 
        feeds[str(member.id)]["id"] = member.id
        feeds[str(member.id)]["last_active(days)"] = 0
        feeds[str(member.id)]["Timezone"] = []
        feeds[str(member.id)]["dataAccess"] = 0

    
        with open("jsons/user_info.json", mode='w') as f:
            f.write(json.dumps(feeds, indent=2))
        

@client.event
async def on_member_remove(member):
    with open("jsons/user_info.json") as fj: 
        feeds = json.load(fj)
    
    feeds.pop(str(member.id))

    with open("jsons/user_info.json", mode='w') as f:
        f.write(json.dumps(feeds, indent=2))





client.run(token)

