import discord
intents = discord.Intents(messages=True, guilds=True, members=True)
intents.reactions = True
intents.members = True
from discord.ext import commands
import os
from dotenv import load_dotenv
client = commands.Bot(command_prefix="?",owner_ids=[386826952599928842, 427822985102098434], intents=discord.Intents.all())
load_dotenv()

token = ""

def get_token():
    ans = input("are you testing y/n: ")
    if ans == "y":
        return os.getenv("TOKEN")
    elif ans == "n":
        return os.getenv("testingTOKEN")
    else:
        print("Unexpected input try again")
        get_token()

token = get_token()


@client.event
async def on_ready():
    print("Ready")



@client.command(name="restart")
@commands.is_owner()
async def restart(ctx):
    await ctx.send("Restarting")
    os.system("python main.py")


    

@client.event
async def on_member_join(ctx):
    embed=discord.Embed(title=f"Welcome {ctx.name}", description=f"Thanks for joining {ctx.guild.name}, read the rules in <#799334905569345606> and enjoy your stay!!")
    embed.set_thumbnail(url=ctx.avatar_url)
    await ctx.send(embed=embed)

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

client.run(token)