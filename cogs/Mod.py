import discord
import os.path
import random
from config import info
from discord.utils import get
from discord.ext import commands

class Mod(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def kick(self, msg):
        user = msg.message.author
        mod_role = get(user.guild.roles, name="Mod")
        mc_username = msg.message.content.replace("r!kick ", "")
        console_channel = self.client.get_channel(707777532555952158)

        if mod_role in user.roles: 
            await console_channel.send(f"kick {mc_username}")
            await msg.send(f"**{mc_username}** has been kicked from the minecraft server.")
        else: 
            await msg.send("You do not have permission to use this command!")

def setup(client):
    client.add_cog(Mod(client))