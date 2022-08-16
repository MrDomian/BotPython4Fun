import discord
import random

TOKEN = 'NzU5NDcxMzc1ODA2NzU5MDIy.GBW4U7.JgmUG4B1q2nrtqXm3wkHLBvJaIJvgA87sZpLvM'
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

client.run(TOKEN)
