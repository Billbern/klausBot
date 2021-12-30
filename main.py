import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


client = discord.Client()

@client.event
async def on_member_join(member):
    print(f"{member} joined") 


client.run(TOKEN)