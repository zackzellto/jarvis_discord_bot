from api.openai_api import get_gpt4_response
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')


@bot.command(name='ask')
async def ask_gpt4(ctx, *, question):
    response = get_gpt4_response(question)
    await ctx.send(response)


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the server, ask whatever you would like by using !ask'
    )


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == '!test':
        await message.channel.send('Test successful!')

    await bot.process_commands(message)  # Add this line to process commands

bot.run(BOT_TOKEN)
