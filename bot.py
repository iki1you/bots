from discord.ext import commands
import discord
import asyncio
import random


TOKEN = "ODMxNDg3NDc1Mzc2ODQ4OTM3.YHV9Dg.oXrQttBczVNDDc8HQqBmixAeCTs"

dashes = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']


class RandomThings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='roll_dice')
    async def roll_dice(self, ctx, count):
        res = [random.choice(dashes) for _ in range(int(count))]
        await ctx.send(" ".join(res))

    @commands.command(name='randint')
    async def my_randint(self, ctx, min_int, max_int):
        num = random.randint(int(min_int), int(max_int))
        await ctx.send(num)


bot = commands.Bot(command_prefix='!#')
bot.add_cog(RandomThings(bot))
bot.run(TOKEN)