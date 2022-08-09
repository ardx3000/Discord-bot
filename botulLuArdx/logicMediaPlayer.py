import connectionAndCommands
import asyncio

import discord
from discord.ext import commands

client = connectionAndCommands.client


def nyan(ctx):
    user = ctx.message.author
    voice_channel = ctx.author.voice.channel
    channel = None
    if voice_channel is not None:
        channel = voice_channel.name
        vc = await voice_channel.connect()
        vc.play(
            discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source='C:/Users/ardx3/PycharmProjects'
                                                                                 '/botulLuArdx/nyanpass_2.mp3'))

        while vc.is_playing():
            await asyncio.sleep(1)
        await vc.disconnect()
    else:
        await ctx.send(str(ctx.author.name) + "is not in a channel.")
