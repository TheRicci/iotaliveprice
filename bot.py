import discord
from discord import channel
from discord.ext import commands
from tools import *
from discord.ext import tasks
import random

client = commands.Bot(command_prefix = '.')

client.remove_command('help')


@client.event
async def on_ready():    
    change.start()
    coingecko2.start()
    coingecko.start()
    binanceP.start()

    print('Bot is Ready.')

data = {}

@tasks.loop(seconds=360)
async def change():
    try:
        rank,pricea,change1,change24 = cUSDD('miota')
        data['rank'] = rank
        if change1 > 0:
            data['change1hr'] = (str(f'{round(change1,3)}%➚'))
        else:
            data['change1hr'] = (str(f'{round(change1,3)}%➘'))
    except:
        pass

@tasks.loop(seconds=14)
async def coingecko():
    try:
        price,change24,vol24 = cUSD()
        data['price'] = price
        data['change24'] = change24
        data['vol24'] = vol24
    except:
        pass
    try:
        change = data['change1hr']
        price2= format(data['pricebtc'], '.8f')
        if data['changebtc'] > 0:
            price3 = f'{price2}➚'
        else:
            price3 = f'{price2}➘'
        if float(data['change24']) > 0:
            await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching,name=f'〉24h: {round(change24,3)}%➚, 1h: {change}, btc:  {price3} , 24h vol: {int(vol24):,} '))
        else:
            await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching,name=f'〉24h: {round(change24,3)}%➘, 1h: {change}, btc:  {price3} , 24h vol: {int(vol24):,} '))
    except:
        pass

@tasks.loop(seconds=30)
async def coingecko2():
    try:
        pricebtc,changebtc = cUSD2()
        data['pricebtc'] = pricebtc
        data['changebtc'] = changebtc
    except:
        pass


@tasks.loop(seconds=1)
async def binanceP():
    try:
        eita =random.uniform(0.0001, 0.0003)
        data['binance'] = binance() + eita
    except:
        pass 
    try:       
        price = data['binance']
        guild = client.get_guild(id=397872799483428865) 
        me = guild.me        
        if float(data['change24']) > 0:
            await me.edit(nick=f"${round(price,4)}➚ #{data['rank']}")
                    
        else:
            await me.edit(nick=f"${round(price,4)}➘ #{data['rank']}")
    except:
        pass            
    

client.run('Discord-key')



