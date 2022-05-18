from discord import Client, Intents, Embed
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from dotenv import load_dotenv
import os

load_dotenv()
token = ""
token = os.getenv("TOKEN")


client = commands.Bot(command_prefix="?", owner_ids=[386826952599928842, 427822985102098434], intents=Intents.all())
slash = SlashCommand(client, sync_commands=True)



@slash.slash(
name="hello", 
description="sends test message",
guild_ids=[932684556572700773],
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

client.run(token)