import discord
import random
from discord.ext import commands


def run():
    intents = discord.Intents.default()
    intents.message_content = True 

    bot = commands.Bot(command_prefix="!", intents=intents)    


    @bot.command(
            aliases=['p'],
            help = "This is hälp",
            description = "This is description",
            brief = "This is brief",
            enabled = True,
            hidden = False
    )
    async def ping(ctx):
        """Answers with pong"""
        await ctx.send("pong")

    @bot.command()
    async def say(ctx, what = "WHAT?!"):
        """WHAT?!"""
        await ctx.send("what")

    @bot.command()
    async def say2(ctx, *what):
        """what"""
        await ctx.send(" ".join(what))

    @bot.command()
    async def say3(ctx, what = "WHAT?!", why = "WHY?"):
        """WHAT?! WHY?"""
        await ctx.send(what + why)

    @bot.command()
    async def choises(ctx, *options):
        """Random shit"""
        await ctx.send(random.choice(options))
