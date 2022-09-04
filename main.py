import discord
import random
from env import TOKEN
from src.quotation import get_quote
from src.random import sad_words, comfort_word

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    # Message on channel: discord-bot
    if message.channel.name == 'discord-bot':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'See you later {username}!')
            return
        elif user_message.lower() == '!random':
            response = f'This is your random number: {random.randrange(1000000)}'
            await message.channel.send(response)
            return

    # Message on all channels
    if user_message.lower() == '!anywhere':
        await message.channel.send('This can be used anywhere!')
        return

    if message.content.startswith('!quotation'):
        await message.channel.send(get_quote())
        return

    msg = message.content  # message on chat
    if any(word in msg for word in sad_words):
        await message.channel.send(comfort_word)
        return


client.run(TOKEN)
