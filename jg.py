import discord
import os
client = discord.Client()


@client.event
async def on_ready():
    print("ready")

@client.event
async def on_message(message):
    if message.content.startswith("KIDJG"):
        await message.channel.send("진단아 자가진단")




access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
