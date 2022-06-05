import os
##install all the modules from dependencies.txt (basically only used for the server)
#os.system("pip install -r dependencies.txt")
import discord
#Kill me
from discord.ext import commands
import time
import json
from discord import Client, Intents, Embed
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from dotenv import load_dotenv
client = commands.Bot(command_prefix="?",owner_ids=[386826952599928842, 427822985102098434], intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True, sync_on_cog_reload=True)

load_dotenv()

token = ""

token = os.getenv("TOKEN") #get_token()




@slash.slash(
name="hello", 
description="sends test message",
guild_ids=[932684556572700773,786013884216639509],
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
    print("Ready")



@client.command(name="restart")
@commands.is_owner()
async def restart(ctx):
    await ctx.send("Restarting")
    os.system("python main.py")


    



@client.command(name='kill', aliases=['k'])
@commands.is_owner()
async def unloadall(ctx):
    await ctx.send("Breaking")
    exit()



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
async def on_member_join(member):
    
    import what_server
    if what_server.Kennevo:
        guild = discord.utils.get(client.guilds, id=int(786013884216639509))
        role = discord.utils.get(guild.roles, id=int(953004596882702386))

    else:
        guild= discord.utils.get(client.guilds, id=int(932684556572700773))
        role = discord.utils.get(guild.roles, id=int(946936153687347230))


    


    print(f"{member} has joined the server")

    with open("user_info.json") as fj: 
        feeds = json.load(fj)
        
    #checks if the user is already in the user_info.json file
    #if so it will do nothing
    try:
        name = feeds[str(member.id)]['name']
        print(f"{name} has rejoined")

    #else it'll add the user to the user_info.json file and give them the "new_user" role
    except KeyError:
        #send welcome message to the new user
        embed=discord.Embed(title=f"Welcome {member.name}", description=f"Thanks for joining {guild.name}, read the rules in <#799334905569345606> and enjoy your stay!!")
        embed.set_thumbnail(url=member.avatar_url)
        await member.send(embed=embed)


        feeds[int(member.id)] = {"new":1}

        with open("user_info.json", mode='w') as f:
            f.write(json.dumps(feeds, indent=2))
        await member.add_roles(role)

        with open("user_info.json") as fj: 
            feeds = json.load(fj)
        feeds[str(member.id)]["name"] = member.name 
        feeds[str(member.id)]["id"] = member.id
        feeds[str(member.id)]["word_immunity"] = False

        with open("user_info.json", mode='w') as f:
            f.write(json.dumps(feeds, indent=2))
        
        

    









    
#g
client.run(token)
