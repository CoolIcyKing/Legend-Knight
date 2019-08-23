import discord
import asyncio
import random
import datetime
from discord.ext import commands
import os
import sys
import logging

client = commands.Bot(command_prefix = ',')
timenow = datetime.datetime.utcnow()
client.remove_command('help')

status2str = {
    discord.Status.dnd: 'Do Not Disturb',
    discord.Status.idle: 'Idle',
    discord.Status.online: 'Online',
    discord.Status.offline: 'Offline'
}

activity2str = {
    discord.ActivityType.playing: 'Playing ',
    discord.ActivityType.streaming: 'Streaming ',
    discord.ActivityType.watching: 'Watching ',
    discord.ActivityType.unknown: 'Unknown - '
}

@client.listen()
async def on_ready():
    game = discord.Game(name="Legends | ,help")
    await client.change_presence(status=discord.Status.online, activity=game)
    readymessage = "Hello, I'm up and running! It is " + str(timenow) + "\n" + "System version: " + (sys.version)
    uptimedict['timeuptime'] = timenow
    print(readymessage)


uptimedict = {
    'timeuptime': 0,
}


@client.event
async def on_ready():
  print('Bot is ready.')


@client.command()
async def ping(ctx):
  await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = [

        'It is certain.',

        'It is decidedly so.',

        'Without a doubt.',

        'Yes - definitely.',

        'You may rely on it.',

        'As I see it, yes.',

        'Most likely.',

        'Outlook good.',

        'Yes.',

        'Signs point to yes.',

        'Reply hazy, try again.',

        'Ask again later.',

        'Better not tell you now.',

        'Cannot predict now.',

        'Concentrate and ask again.',

        'Don\'t count on it.',

        'My reply is no.',

        'My sources say no.',

        'Outlook not so good.',

        'Very doubtful.'] 
        
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')       


@client.command()
async def repeat(ctx, *, args):
    embed=discord.Embed(title="Repeat", description=args, color="0xff0000")
    await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
  await member.kick(reason=reason)


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
  await member.ban(reason=reason)
   
@ban.error
async def ban_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send('You dont have permission to do that!')

@kick.error
async def kick_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send('You dont have permission to do that!')







@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
  await ctx.channel.purge(limit=amount)

@clear.error
async def clear_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send('You dont have permission to do that!')



client.(str(os.environ.get('NTY0MTAyMTA5ODIyMzIwNjYx.XV3cRg.zBIpFm_BQysSkkVnp6pfCJg05OY')))
