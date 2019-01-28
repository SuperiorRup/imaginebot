import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='Superior Bot'))
    print('Ready') 


@client.event
async def on_message(message):
    if ('bitch') in message.content:
       await client.delete_message(message)
    if ('noob') in message.content:
       await client.delete_message(message)
    if ('cry') in message.content:
       await client.delete_message(message)
    if message.content == '!fortune':
        await client.send_message(message.channel,'you will go school today')
    if message.content == 'ping':
        await client.send_message(message.channel,'Pong')
    if message.content == 'lol':
        await client.send_message(message.channel,'Little Old Lady')
    if message.content == 'imagine':
        await client.send_message(message.channel,'Yes!')
    if message.content == 'igp':
        await client.send_message(message.channel,'What')
    if message.content == '@ıɱąɠıŋɛ ɠąɱıŋɠ ℘Ɩąy':
        await client.send_message(message.channel,'Why Did You Ping')
       
    Mike = Bot('+')

@Mike.command(pass_context = True)
async def say(ctx, *args):
    mesg = ' '.join(args)
return await Mike.say(mesg)

client.run('NTM5MDQwMTgwNjQwODA4OTc0.Dy8kLw.TcIofRa0MfvdM1gr7gkrBELhqNc')
