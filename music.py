import discord, random,os
from discord.ext import commands
import youtube_dl

class music(commands.cog)
    def __init__(self, client)
        self.client = client 
    @commands.commands(
      async def join(self,ctx):
        if ctx.author.voice is none
           await ctx.send("your not in a voice channel")
       voice_channel = ctx.author.voice.channel
       if ctx.voice.client is None 
          await voice_channel.connect
       else: 
           await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def disconnect(self,ctx):
         await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self,ctx,url)
      ctx.voice.client.stop()
      FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -'}
    
def setup(Client)
    client.add_cog(music(client))