import os
import discord
from discord_slash import SlashCommand
from discord_slash import SlashContext

bot = discord.Client()
slash = SlashCommand(bot)


def prettyprint_author(author):
    return f'{author.name}#{author.discriminator} ({author.id})'


@slash.slash(name='changenick')
async def changenick(ctx: SlashContext, user: str, nick: str):
    author = ctx.author
    if isinstance(author, int):
        author = await ctx.bot.fetch_user(author)
    await ctx.bot.http.edit_member(ctx.guild.id, user, reason=prettyprint_author(author), nick=nick)
    await ctx.ack()


@slash.slash(name='clearnick')
async def clearnick(ctx: SlashContext, user: str):
    author = ctx.author
    if isinstance(author, int):
        author = await ctx.bot.fetch_user(author)
    await ctx.bot.http.edit_member(ctx.guild.id, user, reason=prettyprint_author(author), nick=None)
    await ctx.ack()


def main(token=os.getenv('CRINGEBOT_TOKEN')):
    bot.run(token)
