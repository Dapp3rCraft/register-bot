import discord
from discord.ext import commands
from mcstatus import MinecraftServer

class Stats(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.addr = 'play.dapp3rcraft.com:25565'

    @commands.command()
    async def stats(self, msg):
        server = MinecraftServer.lookup(self.addr)
        status = server.status()
        latency = int(status.latency)
        statsEmbed = discord.Embed(
            title=f'Dapp3rCraft\'s Stats', 
            color=discord.Colour.from_rgb(latency, 200, 0)
        )
        statsEmbed.add_field(
            name=f'Minecraft Ping',
            value=f'**{latency}**ms'
        )
        statsEmbed.add_field(
            name=f'Bot Ping',
            value=f'**{int(self.client.latency * 1000)}**ms'
        )
        await msg.send(embed=statsEmbed)

def setup(client):
    client.add_cog(Stats(client))
