import os
import os.path
import discord

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

client = commands.Bot(command_prefix="/")
client.remove_command("help")

async def remove_whitelist(mc_username, member, discord_id):
    console_channel = client.get_channel(707777532555952158)
    await console_channel.send(f"whitelist remove {mc_username}")
    new_line = str(discord_id)
    lines = open("registered.txt", "r").readlines()
    with open("registered.txt", "w") as f:
        for line in lines:
            if line.split(" ")[0] != new_line:
                f.write(line)

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
async def on_member_remove(member):
    general_channel = client.get_channel(361645469094379522)
    await general_channel.send(f"**{member.name}** left the server")
    registered = open("registered.txt", "r").readlines()
    for user in registered:
        user = user.split(" ")
        discord_id = user[0]
        mc_username = user[1]
        if int(discord_id) == member.id:
            await remove_whitelist(mc_username, member, discord_id)

@client.event
async def on_member_join(member):
    if member.bot:
        return
    channel = client.get_channel(708017717726150729)
    id = member.id
    await channel.send(f"<@{id}> **Welcome to Dapp3rCraft!**\nRegister by typing `/register <your mc username>` or just `/register`")

@client.command()
async def ping(msg):
    await msg.send(f"{round(client.latency * 1000)}ms")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run(os.getenv("TOKEN"))