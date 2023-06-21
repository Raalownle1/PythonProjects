import discord
import random

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('!cybersecurity'):
        tips = ['Use strong passwords and change them regularly']
        tip = random.choice(tips)
        await message.channel.send(tip)

client.run('YOUR_DISCORD_TOKEN')
