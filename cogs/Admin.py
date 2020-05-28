import discord
import os.path
import random
from config import info
from discord.utils import get
from discord.ext import commands

class Admin(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.admins = info.bot_admins
    

    @commands.command()
    async def ban(self, msg):
        user = msg.message.author
        admin_role = get(user.guild.roles, name="Admin")
        mc_username = msg.message.content.replace("r!ban ", "")
        console_channel = self.client.get_channel(707777532555952158)

        if admin_role in user.roles:
            await console_channel.send(f"ban {mc_username}")
            await msg.send(f"**{mc_username}** has been banned from the minecraft server.")
        else: 
            await msg.send("You do not have permission to use this command!")

    @commands.command()
    async def unban(self, msg):
        user = msg.message.author
        admin_role = get(user.guild.roles, name="Admin")
        mc_username = msg.message.content.replace("r!unban ", "")
        console_channel = self.client.get_channel(707777532555952158)

        if admin_role in user.roles: 
            await console_channel.send(f"pardon {mc_username}")
            await msg.send(f"**{mc_username}** has been unbanned from the minecraft server.")
        else: 
            await msg.send("You do not have permission to use this command!")

    @commands.command()
    async def kick(self, msg):
        user = msg.message.author
        admin_role = get(user.guild.roles, name="Admin")
        mc_username = msg.message.content.replace("r!kick ", "")
        console_channel = self.client.get_channel(707777532555952158)

        if admin_role in user.roles: 
            await console_channel.send(f"kick {mc_username}")
            await msg.send(f"**{mc_username}** has been kicked from the minecraft server.")
        else: 
            await msg.send("You do not have permission to use this command!")

def setup(client):
    client.add_cog(Admin(client))