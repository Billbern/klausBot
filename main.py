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
            return len(guild.members)


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f"Hello {member.name}, welcome to Programmer's Hub GH\nPlease introduce yourself " )

@client.event
async def on_message(message):
    if message.content.startswith(";$"):
        if message.content.split("$")[1] == "count":
            memcount = getmembercount(message.guild)
            await message.channel.send(memcount)
        if message.content.split("$")[1] == "Hi" or message.content.split("$")[1] == "Hello":
            await message.channel.send(f"{message.user} Hello how are you")
    

client.run(TOKEN)