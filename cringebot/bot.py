import os
import discord
from discord_slash import SlashCommand
from discord_slash import SlashContext

bot = discord.Client()
slash = SlashCommand(bot)


@slash.slash(name='changenick')
async def changenick(ctx: SlashContext, user: str, nick: str):
    await bot.http.edit_member(ctx.guild.id, user, reason='cringebot', nick=nick)


@slash.slash(name='clearnick')
async def clearnick(ctx: SlashContext, user: str):
    await bot.http.edit_member(ctx.guild.id, user, reason='cringebot', nick=None)


def main(token=os.getenv('CRINGEBOT_TOKEN')):
    bot.run(token)
