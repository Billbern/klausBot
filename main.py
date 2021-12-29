import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


client = discord.Client()

@client.event
async def on_member_join(member):
    await member.create_dm() 
    pass  


client.run(TOKEN) 