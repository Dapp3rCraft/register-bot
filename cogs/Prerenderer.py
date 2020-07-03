import discord
import time
import threading
from mcstatus import MinecraftServer
from discord.ext import commands
from discord.utils import get

class Prerenderer(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.server_addr = 'play.dapp3rcraft.com:25565'
        self.is_prerendering = False

    @commands.command()
    async def renderstart(self, msg):
        user = msg.message.author
        admin_role = get(user.guild.roles, name="Admin")
        if admin_role in user.roles:
            if self.is_prerendering:
                return msg.send('Prerendering is already active!')
            self.set_interval(self.check_status, 300)
            msg.send('Prerendering will start when no one is online to prevent lag!')
        else: 
            return msg.send('You do not have permission to use this command!')

    def set_interval(self, func, sec):
        def func_wrapper():
            self.set_interval(func, sec)
            func()
        t = threading.Timer(sec, func_wrapper)
        t.start()
        return t

    def check_status(self):
        player_count = self.count_players_online(self.server_addr)
        if player_count == 0:
            return self.start_prerendering()
        elif self.is_prerendering:
            return self.stop_prerendering()

    def count_players_online(self, addr):
        server = MinecraftServer.lookup(addr)
        status = server.status()
        return status.players.online

    async def start_prerendering(self):
        self.is_prerendering = True
        await self.send_msg(707777532555952158, 'wb fill start')
        return print('Started prerendering...')

    async def stop_prerendering(self):
        self.is_prerendering = False
        await self.send_msg(707777532555952158, 'wb fill pause')
        return print('Stopped prerendering...')

    async def send_msg(self, channel_id, msg):
        channel = self.client.get_channel(channel_id)
        return await channel.send(msg)

def setup(client):
    client.add_cog(Prerenderer(client))
