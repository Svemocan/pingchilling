import discord
from discord.ext import commands
import os
from webserver import keep_alive

TOKEN = os.environ['TOKEN']
ROLE_ID = int(os.environ['ROLE_ID'])
CHANNEL_ID = int(os.environ.get('CHANNEL_ID', 0))  # default 0 = no specific channel
SPECIFIC_USER_ID = int(os.environ.get('SPECIFIC_USER_ID', 0))  # default 0 = no specific user
TEST_ID = int(os.environ.get('TEST_ID', 0))

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    print(f"Message posted in specified channel.")
    #if message.author.bot:
    #    return

    if CHANNEL_ID and message.channel.id != CHANNEL_ID:
        return

    if SPECIFIC_USER_ID and message.author.id != SPECIFIC_USER_ID:
        return

    role = message.guild.get_role(ROLE_ID)
    if role:
        await message.channel.send(f'Aha {role.mention}, Wargaming vydaly nějakou novinku, připravte si kreditku! :grin:')
        print(f'{bot.user} just sent a message.')

    if message.author.id == TEST_ID:
        print('Test :3')
        
keep_alive()
bot.run(TOKEN)
