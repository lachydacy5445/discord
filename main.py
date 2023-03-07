import discord, random
from discord.ext import commands 

TOKEN = "MTA3OTg5Njg4MTM5Nzc4MDYwMQ.GT3kqb.OLqOuYVN2no2ApOx2bCbO6nti4N5G4Xebj4Hwg"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = "$", intents = intents)

@bot.command(name = "roll")
async def roll(ctx):
  d = random.randint(1,450)
  await ctx.channel.send(f"Rolling a D450 : {d}")
  























bot.run(TOKEN)