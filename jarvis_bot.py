from api.openai_api import get_gpt_response
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
async def ask_gpt(ctx, *, question):
    response = get_gpt_response(question)
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
        response = "Line 1: Test successful!\nLine 2: Another line here\nLine 3: And one more line"
        await message.channel.send(response)

    await bot.process_commands(message)


@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise Exception


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')
    elif isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send('Please include a question to ask.')
    else:
        raise error


bot.run(BOT_TOKEN)
