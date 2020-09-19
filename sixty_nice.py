# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    for guild in client.guilds:
        print(f'{guild}')
@client.event
async def on_message(message):
    channel = client.get_channel(message.channel.id)
    print (f'{channel}, {message.channel}')
    textSearch = "69"
    print( f'{message.content}\n')
    if message.content.find(textSearch) != -1:
        await channel.send('Nice.')

client.run(TOKEN)
