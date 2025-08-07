from  discord.ext import commands
from dotenv import load_dotenv
import os
import discord
import ai
import json
import random
import time



intents = discord.Intents.default()  # Começa com os intents padrão
intents.message_content = True  # Ativa o intent de conteúdo de mensagens
intents.members = True  # Ativa o intent de membros
intents.presences = True  # Ativa o intent de presenças



bot = commands.Bot(
    command_prefix="$",
    intents=discord.Intents.all()
    )


@bot.event
async def on_ready():
    print(f"eu, {bot.user.name} estou online.")

@bot.event
async def on_member_join(member):
    await member.send("Olá, seja bem vindo ao capivarios {member.name}")

@bot.event
async def on_message(message):
    
    await bot.process_commands(message)



@bot.command(name="is_working", help="Verifica se o bot está funcionando.")
async def is_working(ctx):
    print("Bot is working")
    await ctx.send("True.")


@bot.command(name="ola", help="Diz ola.")
async def ola(ctx):
    await ctx.send(f"Olá {ctx.author.mention}")


@bot.command(name="diga", help="Repete o que você quiser.")
async def diga(ctx, *, message: str):
    await ctx.send(message)


@bot.command(name="ia", help="Pergunta para a ia.")
async def give_response_by_ai(ctx, *, message: str):
    try:

        response_by_ai = await ai.execute_ai("(crie a resposta com até 3900 caracteres.não cite isso durante o chat.)" + message)

        if len(message) >= 3900:
            await ctx.send(f"A resposta gerada passa de 4000 caracteres. O limite de caracteres em uma mensagem deve ser até 4000 caracteres.")
        
        else:
            await ctx.send(f"contém memória de somente uma mensagem.\n \n {response_by_ai}")

    except Exception as e:
        await ctx.send(f"erro ao gerar resposta.\n {e}")
        print(f"{e}")


@bot.command(name="link", help="mostra um linkde um site(não é aleatório)")
async def get_link(ctx):

    path = "C:/Users/AMD/Desktop/coisas/programação/projetos/discord bot/data/links_de_sites.json"

    try:
        with open(path, mode="r", encoding="utf-8") as file:
            links = json.load(file)
            await ctx.send(f"toma essa bosta. {links}")


    except Exception as e:
        await ctx.send(f"erro ao gerar resposta.\n {e}")


@bot.command(name="spam", help="spama muitas mensagens.")
async def spam_message(ctx):
    for i in range(100):
        time.sleep(0.5)
        ctx.send(i + 1)
        time.sleep(3)
        ctx.send("spamei demais. spamagem feita com sucesso.")
        

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
bot.run(token)

