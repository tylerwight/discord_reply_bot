# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


# print all servers bot is connected to on startup, just for reference
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    for guild in client.guilds:
        print(f'{guild}')


@client.event
async def on_message(message):
    channel = client.get_channel(message.channel.id) # get channel id from message and use it to create channel object
#    print (f'{channel}, {message.channel}')  # print some variables for debug
    textSearch = "Thanks"
    if message.content.find(textSearch) != -1: # serach message for anywhere
        print( f'{message.content}\n') # print the mesage that triggered our 
        await channel.send('You are welcome')

client.run(TOKEN)
