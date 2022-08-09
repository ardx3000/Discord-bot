# discord imports
import discord
from discord.ext import commands
# async imports
import asyncio
# os imports
import os
from dotenv import load_dotenv
# personal files imports
import dataBase
import logicMGC
import CreateJsonEnt

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("Folositi .lmao pentru a vedea "
                                                                                   "comenzile. Sunt inca in "
                                                                                   "dezvoltare , si dezvoltator-ul "
                                                                                   "meu ardx"))


print("Bot is ready!")


@client.command(name='lmao',
                pass_context=True)
async def lmao(ctx):
    helpList = dataBase.helpL()
    await ctx.send('\n'.join(map(str, helpList)))


@client.command(name='utilitati',
                pass_context=True)
async def utilitati(ctx):
    utilList = dataBase.utilitatiS()
    await ctx.send('\n'.join(map(str, utilList)))


@client.command(name='casino',
                pass_context=True)
async def casino(ctx):
    casinoList = dataBase.casino()
    await ctx.send('\n'.join(map(str, casinoList)))


@client.command(name='hl',
                pass_context=True)
async def hl(ctx):
    hLList = dataBase.hl()
    await ctx.send('\n'.join(map(str, hLList)))


@client.command(name='profil',
                pass_context=True)
async def profil(ctx):
    profileList = dataBase.profil()
    await ctx.send('\n'.join(map(str, profileList)))


@client.command(name='ganduri',
                pass_context=True)
async def ganduri(ctx):
    gandurileLuiDanielList = dataBase.ganduri()
    await ctx.send('\n'.join(map(str, gandurileLuiDanielList)))


@client.command(name='misto',
                pass_context=True)
async def misto(ctx):
    mistoList = dataBase.misto()
    await ctx.send('\n'.join(map(str, mistoList)))


@client.command(name='echipa',
                pass_context=True)
async def echipa(ctx):
    religieList = dataBase.religie()
    await ctx.send('\n'.join(map(str, religieList)))

    len(religieList)
    x = len(religieList) - 2
    await ctx.send(x)


# comenzi cu logica

@client.command(name='roll',
                pass_context=True)
async def roll(ctx):
    await ctx.send(f"{ctx.author.mention}, a rulat XD: {logicMGC.rollM()}")


@client.command(name='banul',
                pass_context=True)
async def banul(ctx):
    await ctx.send(f" {ctx.author.mention}, a picat: {logicMGC.daCuBanul()}")


@client.command(name='precedent',
                pass_context=True)
async def precedent(ctx):  # comanda de a vedea nr precedent
    await ctx.send("Numarul precedent este:")
    await ctx.send(logicMGC.aHiLow())


@client.command(name='high',
                pass_context=True)
async def high(ctx):
    await ctx.send("Numarul precedent era:")
    await ctx.send(logicMGC.aHiLow())

    await ctx.send("{} rolled:".format(ctx.author.name()))
    await ctx.send(logicMGC.HLR())

    await ctx.send(logicMGC.highLogic())


@client.command(name='low',
                pass_context=True)
async def low(ctx):
    await ctx.send("Numarul precedent era:")
    await ctx.send(logicMGC.aHiLow())

    await ctx.send("Numarul nou este este:")
    await ctx.send(logicMGC.HLR())

    await ctx.send(logicMGC.lowLogic())


'''@client.command(name='nyan',
                pass_context=True)
async def nyan(ctx):
    logicMediaPlayer.nyan()'''

@client.command(name='join echipa', pass_context=True) # Nu mai stiu pt ce plm era asta
async def join(ctx):
   name = ctx.author.name()




@client.command(name='testRegister', pass_context=True) #Test pentru luat numele validation method
async def test(ctx):
    author =  ctx.author.name
    validation = CreateJsonEnt.validation(author)

    if validation == True:
        await ctx.send(ctx.author.name + "User Has been added to the database!")
    elif validation == False:
        await ctx.send(ctx.author.name + "User already exists, use (!showProfile) !")


@client.command(name='testRegister2', pass_context=True)  # Test pentru luat numele test method
async def test(ctx):
    author = ctx.author.name
    CreateJsonEnt.testMethod(author)


load_dotenv()
TOKEN = os.environ.get("DISCORD_TOKEN")
client.run(TOKEN)
