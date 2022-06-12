from cgitb import text
import random
import re
import discord
from discord.ext import commands
from config import settings

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.command() # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def qq(ctx): # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.
    await ctx.send(f'Привет, {author.mention}!') # Выводим сообщение с упоминанием автора, обращаясь к переменной author.

@bot.command()
async def say(ctx, athor, *args):
    await ctx.message.delete()
    await ctx.send(' '.join(args))

@bot.command()
async def rul(ctx, count=3):
    if (int(count) >= 1 and int(count) <= 100):
            text = ""
            for n in range(count):
                ran = random.randint(1,2)
                if (ran == 1): text += "🟢"
                if (ran == 2): text += "🔴"
            embed = discord.Embed()
            if (text.find("🔴") == -1):
                embed = discord.Embed(
                title = f'Вы выйграли (Вероятность выйгрыша {0.25**int(count) * 100}%)',
                colour = discord.Colour.from_rgb(0, 255, 0),
                description = text)
            else:
                embed = discord.Embed(
                title = f'Вы проиграли (Вероятность выйгрыша {0.25**int(count) * 100}%)',
                colour = discord.Colour.from_rgb(255, 0, 0),
                description = text)
            await ctx.send(embed = embed)
    else: await ctx.send("Не допустимое число")


bot.run(settings['token']) # Обращаемся к словарю settings с ключом token, для получения токена