import discord
from random import randint
from time import sleep

client = discord.Client()


@client.event
async def on_ready():
    print('------')
    print('Connected as user:')
    print(client.user.name)
    print("Using Discord version:")
    print(discord.__version__)
    print('------')
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="For posts.."))


@client.event
async def on_message(message):
    # The text between () is the discord server you want to use, add multiple for multiple servers
    id = client.get_guild(XXX)
    # Text in "" is channels you want the bot to work in
    channels = ["Insert-Channel-Name-Here"]

    # channels: = channels listed in channels = above
    if str(message.channel) in channels:
        # Author ID is USER ID of who you want to respond to
        if message.author.id == XXX:
            # Randomized sleep in seconds X = Low end,X = Max end
            sleep(randint(X, XXX))
            # Change text between "X" for title text, Color is any hex color with 0x in front
            embedvar = discord.Embed(title="Replace-What-You-Want-Said-Here", color=0x42C2CD)
            await message.channel.send(embed=embedvar)  # Sends your embed message

            # Send normal text instead of embed, Replace 'X'. Remove #.
            # await message.channel.send('Bump')


# Your bots token goes here, Replace X.
client.run('Replace with token')
