import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run("ODgxNzQ5MjY3NTg3Mzk5NzMy.YSxW_w.vzc1jjY887pt2469E5-gHSTOO1w")