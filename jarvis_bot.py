import discord
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
client = discord.Client(intents=intents)
BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!hello':
        await message.channel.send('Hello!')


client.run(BOT_TOKEN)
