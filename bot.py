
from settings import settings
import discord

from bot_logic import *
intents = discord.Intents.default()

intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


# Cuando el bot reciba un mensaje, ¡enviará mensajes en el mismo canal!
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('¡Hola! Soy un bot')
    elif message.content.startswith('$smile'):
        await message.channel.send(gen_emodji())
    elif message.content.startswith('$coin'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10))
    else:
        await message.channel.send("No puedo procesar este comando, ¡lo siento!")

client.run(settings["TOKEN"])
