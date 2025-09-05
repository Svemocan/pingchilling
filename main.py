import random

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

bot = commands.Bot(command_prefix="~", intents=intents)

choices = [
    # Generické
    "Aha {role.mention}, ve Wargamingu zase něco vymyslely...běžte si to přečíst, než si to zmizí. :eyes:",
    "Hey ho {role.mention}, čerstvé zprávy z WG!",
    "{role.mention}, máme tu nové info – jestli dobré, nebo zabugované, to už musíte zjistit sami. :kek:",
    "Nové info {role.mention}, co to tak může být?",
    "{role.mention}, dorazil další update. Možná i funguje! :kekleo:",
    "Zprávy přímo z Wargamingu {role.mention}.",
    "{role.mention}, pozor! WG něco vypustilo do světa. Snad to nesmrdí. :pain:",
    "WG vydalo čerstvou dávku textu. {role.mention}, přečíst, nepřešíst, toť otázka. :pepeshrug:",
    "{role.mention}, další díl seriálu \"Co je nového ve WoT\". :tv:",
    "Hlášení z fronty: {role.mention}, na obzoru něco nového! Snad pozitivního... :doge:",
    "{role.mention}, čerstvé zprávy – nebo jen další changelog. Ja neznaju, ja jenom dumb bot :zany_face:",
    "Hlásim pohyb na radaru: WG news. {role.mention}, připravit rozkladací židle a dalekohledy! :satellite:",
    "{role.mention}, je to tu zas. Novinky, patch, update… hoďte si kostkou. :game_die:",
    "WG zmáčklo tlačítko ‚Publish‘. {role.mention}, tak se na to podívejme. :pepesearch:"
    "{role.mention}, update detekován! Beep Boop :robot:",

    # Satirické
    "{role.mention}, WG vydalo něco nového. Buď bugfix, nebo další důvod k smíchu :kekw:",
    "Pozor {role.mention}, další patch. Tipuju, že zase rozbije něco jiného :lulw:",
    "{role.mention}, nové novinky. Kurzy: 20% event, 30% bugfix, 50% monetizace. :BjarneKekLeft:",
    "WG zase něco přidalo. {role.mention}, asi další \"feature\". :smirk:",
    "{role.mention}, čerstvé zprávy – a možná i čerstvá dávka nas*ání. :pepeno:",
    "Breaking news: {role.mention}, WG našlo další důvod na restart klienta. :pog:",
    "{role.mention}, další novinka. Prosíme o potlesk, hoši ve WG makaj o sto šest! :pepewicked:",
    "{role.mention}, Wargaming vydaly něco zbrusu nového, again. Ako bonus: frustrace zdarma. :pepecool:",
    "Aha {role.mention}, Wargaming vydaly nějakou novinku, připravte si kreditku! :grin:"
]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


@bot.event
async def on_message(message):

    user = message.author
    #if user.bot:
    #    return

    if TEST_ID and message.channel.id == CHANNEL_ID and user.id == TEST_ID:
        if message.content.startswith("~test"):
            await message.channel.send(f'{user.mention} test :boykisser:')
            message = random.choices(choices)
            await message.channel.send(f"{message}")
            print('Test :3')

    if CHANNEL_ID and message.channel.id != CHANNEL_ID:
        return

    if SPECIFIC_USER_ID and message.author.id != SPECIFIC_USER_ID:
        return

    role = message.guild.get_role(ROLE_ID)
    if role:
        message = random.choices(choices)
        await message.channel.send(f"{message}")
        print(f'{bot.user} just sent a message.')


keep_alive()
bot.run(TOKEN)
