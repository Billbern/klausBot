import os

import discord
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_NAME')


# intents = discord.Intents.default()
# intents.members = True

client = discord.Client()


def get_members_count(gld):
    bots = 0
    humans = 0
    for guild in client.guilds:
        if guild.name == gld:
            humans += guild.member_count 
            for mem in guild.members:
                if mem.bot:
                    bots += 1
    return (bots, humans - bots)  

@client.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        text_str = f"Hello {member.mention},\nWelcome to {guild.name}\nPlease introduce yourself"
        await guild.system_channel.send(text_str)


@client.event
async def on_message(message):
    if message.content.startswith(";$"):
        if message.content.split("$")[1] == "count":
            memcount = get_members_count(message.guild.name)
            if memcount[1] == 1 and memcount[0] == 1:
                await message.channel.send("There is a member and a bot")
            elif memcount[1] > 1 and memcount[0] > 1:
                await message.channel.send(f"There are {memcount[1]} members and {memcount[0]} bots  so far") 
            elif memcount[1] > 1 and memcount[0] == 1:
                await message.channel.send(f"There are {memcount[1]} members and a bot  so far")
            elif memcount[1] == 1 and memcount[0] > 1:
                await message.channel.send(f"There is a member and {memcount[0]} bots  so far")
            
        if message.content.split("$")[1] == "Hi" or message.content.split("$")[1] == "Hello":
            await message.channel.send(f" {message.author.mention} Hello how are you")
    

client.run(TOKEN)