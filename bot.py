from discord.ext import commands
import discord
import asyncio
import pymorphy2


TOKEN = ""

dashes = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']


class YLBotClient(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help_bot')
    async def help_bot(self, ctx):
        await ctx.send("Commands:\n"
                       "!#numerals for agreement with numerals\n"
                       "!#alive for define alive or not alive\n"
                       "!#noun for noun case (nomn,gent,datv,accs,abit,loct) and number state(single,plural)\n"
                       "!#inf for infinitive state\n"
                       "!#morph for full morphological analysis")

    @commands.command(name='alive')
    async def help_bot(self, ctx, word):
        morph = pymorphy2.MorphAnalyzer()
        res = morph.parse(word)[1]
        if res.tag.animacy == 'inan':
            await ctx.send(word + ' не живой')


bot = commands.Bot(command_prefix='!#')
bot.add_cog(YLBotClient(bot))
bot.run(TOKEN)