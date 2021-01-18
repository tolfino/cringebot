import os
import discord
import requests
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash import SlashContext

bot = commands.Bot(command_prefix='!')
slash = SlashCommand(bot)


def prettyprint_author(author):
    return f'{author.name}#{author.discriminator} ({author.id})'


@slash.slash(name='changenick')
async def changenick(ctx: SlashContext, user: str, nick: str):
    author = ctx.author
    if isinstance(author, int):
        author = await bot.fetch_user(author)
    await bot.http.edit_member(ctx.guild.id, user, reason=prettyprint_author(author), nick=nick)
    await ctx.ack()


@slash.slash(name='clearnick')
async def clearnick(ctx: SlashContext, user: str):
    author = ctx.author
    if isinstance(author, int):
        author = await bot.fetch_user(author)
    await bot.http.edit_member(ctx.guild.id, user, reason=prettyprint_author(author), nick=None)
    await ctx.ack()


@bot.command()
async def changepfp(ctx):
    """change my pfp"""
    if not ctx.message.attachments:
        await ctx.send("you didn't attach an image.. cringe.......")
        return

    try:
        await bot.user.edit(avatar=requests.get(ctx.message.attachments[0].url).content)
    except Exception as e:
        await ctx.send(f"oopsie woopsie there was a fucky wucky:\n```\n{e}```")
        return

    await ctx.send("ok.. fine")


def main(token=os.getenv('CRINGEBOT_TOKEN')):
    bot.run(token)
