import os
import os.path
import discord

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

client = commands.Bot(command_prefix="r!")
client.remove_command("help")

@client.event
async def on_ready():
    print("bot is ready")
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, 
            name="for new members!"
        )
    )

@client.event
async def on_member_join(member):
    channel = client.get_channel(708017717726150729)
    id = member.id
    await channel.send(f"<@{id}> **Welcome to Dapp3rCraft**\nRegister by typing `r!register <your mc username>` or just `r!register`")

@client.command()
async def ping(msg):
    await msg.send(f"{round(client.latency * 1000)}ms")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run(os.getenv("TOKEN"))