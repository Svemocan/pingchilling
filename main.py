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
    "{role.mention}, máme tu nové info – jestli dobré, nebo zabugované, to už musíte zjistit sami. <:kek:1231645829148971098>",
    "Nové info {role.mention}, co to tak může být?",
    "{role.mention}, dorazil další update. Možná i funguje! <:kekleo:1243212747181916282>",
    "Zprávy přímo z Wargamingu {role.mention}.",
    "{role.mention}, pozor! WG něco vypustilo do světa. Snad to nesmrdí. <:pain:1243213799264227431>",
    "WG vydalo čerstvou dávku textu. {role.mention}, přečíst, nepřešíst, toť otázka. <:pepeshrug:1367089196749160448>",
    "{role.mention}, další díl seriálu \"Co je nového ve WoT\". :tv:",
    "Hlášení z fronty: {role.mention}, na obzoru něco nového! Snad pozitivního... <:doge:1243211891116085319>",
    "{role.mention}, čerstvé zprávy – nebo jen další changelog. Ja neznaju, ja jenom dumb bot :zany_face:",
    "Hlásim pohyb na radaru: WG news. {role.mention}, připravit rozkladací židle a dalekohledy! :satellite:",
    "{role.mention}, je to tu zas. Novinky, patch, update… hoďte si kostkou. :game_die:",
    "WG zmáčklo tlačítko ‚Publish‘. {role.mention}, tak se na to podívejme. <:pepesearch:1367089084463583354>"
    "{role.mention}, update detekován! Beep Boop :robot:",

    # Satirické
    "{role.mention}, WG vydalo něco nového. Buď bugfix, nebo další důvod k smíchu <:kekw:1231355571400085634>",
    "Pozor {role.mention}, další patch. Tipuju, že zase rozbije něco jiného <:lulw:1243213559152775249>",
    "{role.mention}, nové novinky. Kurzy: 20% event, 30% bugfix, 50% monetizace. <:BjarneKekLeft:1231646307429388318>",
    "WG zase něco přidalo. {role.mention}, asi další \"feature\". :smirk:",
    "{role.mention}, čerstvé zprávy – a možná i čerstvá dávka nas*ání. <:pepeno:1367087667363315812>",
    "Breaking news: {role.mention}, WG našlo další důvod na restart klienta. <:pog:1243208206696845504>",
    "{role.mention}, další novinka. Prosíme o potlesk, hoši ve WG makaj o sto šest! <:pepewicked:1231645860077633567>",
    "{role.mention}, Wargaming vydaly něco zbrusu nového, again. Ako bonus: frustrace zdarma. <:pepecool:1367087798787637318>",
    "Aha {role.mention}, Wargaming vydaly nějakou novinku, připravte si kreditku! :grin:"
]


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


@bot.event
async def on_message(message):
    role = message.guild.get_role(ROLE_ID)

    user = message.author
    #if user.bot:
    #    return

    if TEST_ID and user.id == TEST_ID:
        if message.content.startswith("~pingchillingtest"):
            await message.channel.send(f'{user.mention} test <:boykisser:1243213206562799657>')
            message = random.choices(choices)
            await message.channel.send(f"{message}")
            print('Test :3')

    if CHANNEL_ID and message.channel.id != CHANNEL_ID:
        return

    if SPECIFIC_USER_ID and message.author.id != SPECIFIC_USER_ID:
        return

    role = message.guild.get_role(ROLE_ID)
    if role:
        chosen = random.choice(choices).format(role=role)
        await message.channel.send(chosen)
        print(f'{bot.user} just sent a message.')


keep_alive()
bot.run(TOKEN)
