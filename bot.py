import discord
from discord.ext import commands


bot = commands.Bot(command_prefix = "-")

@bot.event
async def on_ready():
    print("Bot is online")  

@bot.command()
async def hi(ctx):
    await ctx.send("Hello")

bot.run("ODA2ODYyODA1NjcxMzQ2MTc2.YBvniw.doQCeucekigkZKAuGcOzFkfeF94")

