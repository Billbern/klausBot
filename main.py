import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_NAME')


client = discord.Client()


def getmembercount(gld):
    for guild in client.guilds:
        if guild.name == gld:
            return guild


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f"Hello {member.name}, welcome to Programmer's Hub GH\nPlease introduce yourself " )

@client.event
async def on_message(message):
    if message.content.startswith(";$"):
        if message.content.split("$")[1] == "count":
            memcount = getmembercount(message.guild)
            print(memcount)
            await message.channel.send(9)
    

client.run(TOKEN)