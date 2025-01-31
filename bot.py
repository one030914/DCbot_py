import discord
from discord.ext import commands
import os
import json

with open('data.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='[', intents=intents)

@bot.event
async def on_ready():
    print('Bot is online')

    for filename in os.listdir('./cmds'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == '__main__':
    bot.run(jdata["TOKEN"])