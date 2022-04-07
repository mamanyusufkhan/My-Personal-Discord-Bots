import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print("whassup! I am {0.user}".format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('-NafiaCat'):
    await message.channel.send('WHY ARE CATS SUCH GOOD HUMAN BEINGS')
  
  if message.content.startswith('-Nafiaply'):
    await message.channel.send('Ply anyone')
  
  


client.run('ODgwNDM5NzY0ODcwODg5NDcy.YSeTbQ.Yi6fonDwt5e8Q0gW4pWJv2o_ucs')