import discord
import os
import requests
import json

client = discord.Client()

Nahiyan_words = ["Whoop Whopp", "whoop whopp", "ice", "sentinels"]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q']
  return quote

@client.event
async def on_ready():
  print("Whoop Whopp! I am {0.user}".format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('-Mijnplz'):
    await message.channel.send('Life Ka Maza Bhot Acci Hain\nIs Maza Bhot Alag He Hain\nHum Isko Pinic Kya Ta Hain')
  
  if message.content.startswith('-Mijnbreak'):
    await message.channel.send('Khara Cigarette khaya ashtesi')

  if message.content.startswith('-Mijnfuku'):
    await message.channel.send('Pandemic Fuck You')
  
  if message.content.startswith('-Mijnrank'):
    await message.channel.send('Plat')

  if message.content.startswith('-Mijnbobby'):
    await message.channel.send('Wow bobby shmruda, man got out of jail. As soon as he did he launches something, oh the shmruda kit, and thats pretty crazy. First photo of a free man with a kit and three pretty girls, well not pretty but horny looking girls.')
  
  if message.content.startswith('-EtimMijn'):
    await message.channel.send('মাধ্যমিক পরীক্ষায় ডাব্বা মেরে প্রথমে মারলো সে বাপ এর পুটকি! এরপর এক এক করে মানবজাতির তীর্থে পৌঁছলেন তিনি!! হ্যা!!! ঠিক ধরেছেন!!!! নাম তার এতিম মিজান. পুটকিমারা ওস্তাদ!!! একে একে সবাইকে পুটকি মেরে তার পরবর্তি লক্ষ্য দুই ব্যাক্তি কে একসঙ্গে পুটকিমারা. এ যেনো এতিম মিজানের জাদুর কাঠি মেযিক চক, "এক ঢিলে দুই পুটকি"!')
  
  if message.content.startswith('-DharMijn'):
    quote = get_quote()
    await message.channel.send(quote)
  
  if any(word in message.content for word in Nahiyan_words):
    await message.channel.send("Brother That is My Line")

  


client.run('ODgwMTAxMTUyNDY3ODczODkz.YSZYEg.9tqudEuVJoiFZO0LKeM_mGRs8xw')