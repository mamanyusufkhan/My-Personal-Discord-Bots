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

  if message.content.startswith('-AdhipSympathize'):
    await message.channel.send('TBH tui o same jinish korti or jaygay thakle')


  if message.content.startswith('-AdhipTruth'):
    await message.channel.send('Maliha, Please respect Maman')

    
  
  
  
  


client.run('ODgwNDQ3MjM1OTkxNjY2NzQ4.YSeaYg.jY8iEGpxxGDSB-q_TxT_2veklLw')