import discord
import random
import asyncio
from discord.ext import commands
from model import get_class
import os, random
import requests
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
#consejos
@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')
    await bot.change_presence(activity=discord.Game(name='caring for the environment'))

@bot.command('test')
async def test(ctx):
    await ctx.send("Test done, completely functional!")
@bot.command('image')
async def image(ctx):
    await ctx.send("Envía una imagen de arquitectura inca o azteca: intentaré identificar cuál es!")
    x = ctx.message.attachments
    for i in (x):
        if i.content_type == 'image/png' or  i.content_type == 'image/jpg' or  i.content_type == 'image/jpeg' or  i.content_type == 'image/avif' or  i.content_type == 'image/webm': 
            print(f'An image! \nID: {i.id}\nURL:{i.url}. Saving...')
            file_name=i.filename
            image_path= f'./img/try/{file_name}' 
            await i.save(f'./img/try/{file_name}')
            await ctx.send(get_class("./keras_model.h5", "./labels.txt", image_path))
        else:
            await ctx.send("No image found.")


bot.run('TOKEN')