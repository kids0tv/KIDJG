import discord

client = discord.Client()


@client.event
async def on_ready():
    print("ready")

@client.event
async def on_message(message):
    if message.content.startswith("KIDJG"):
        await message.channel.send("진단아 자가진단")





client.run("ODAxMzkwMTk1Mzg3NzkzNDIw.YAf-xw.Q5uosuIKWiT853o8ZwdiOmr1GME")
