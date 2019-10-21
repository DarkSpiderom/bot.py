
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
@bot.command()
async def привет(ctx):
    await ctx.send('Здравствуй')
@bot.command()
async def дурак(ctx):
	await ctx.send('Сам дурак !')
@bot.command()
async def как_дела(ctx):
	await ctx.send('Нормально,нормально нереально')
@bot.command()
async def пока(ctx):
	await ctx.send('Гудбай')
@bot.command()
async def доброе_утро(ctx):
	await ctx.send("Hey,you.You're finaly awake.")
@bot.command()
async def добрый_день(ctx):
	await ctx.send('Мое почтение')
@bot.command()
async def добрый_вечер(ctx):
	await ctx.send('Я деспетчер.Составлю компанию на вечер.')
@bot.command()
async def жив(ctx):
	await ctx.send('Я живой детка')


#Эвенты
@bot.event
async def on_ready():
	print('Я готов к работе')#проверяем готов ли бот к роботе










bot.run('NjM1MDEzMTg2MDM0MzM1NzQ0.Xaq6xg.PZQEY2wfCx72S4BjRAvFMpuosI4' )
