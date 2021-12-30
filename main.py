import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_NAME')


intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)


@client.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        text_str = f"Hello @{member.name},\nWelcome to {guild.name}\nPlease introduce yourself"
        await guild.system_channel.send(text_str)


@client.event
async def on_message(message):
    if message.content.startswith(";$"):
        if message.content.split("$")[1] == "count":
            pass
            # await message.channel.send(memcount)
        if message.content.split("$")[1] == "Hi" or message.content.split("$")[1] == "Hello":
            await message.channel.send(f"@{message.author} Hello how are you")
    

client.run(TOKEN)