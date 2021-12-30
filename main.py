import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_NAME')


client = discord.Client()

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f"Hello {member.name}, welcome to Programmer's Hub GH\nPlease introduce yourself " )

@client.event
async def on_message(message):
    if message.startswith(";$"):
        if message.split("$")[1] == "count":
            print(message)
            # message.channel.send()
    pass
    

client.run(TOKEN)