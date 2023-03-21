
import random
import settings
import discord
from discord.ext import commands


logger = settings.logging.getLogger("bot")


def run():
    intents = discord.Intents.default()
    intents.message_content = True 

    bot = commands.Bot(command_prefix="!", intents=intents)
    
    @bot.event
    async def on_ready():
        
        logger.info(f"User {bot.user}(ID: {bot.user.id})")

        channel = bot.get_channel(int(settings.CH_BOTS))
        await channel.send("Hello, I'm back!")

    @bot.command(
            
            #aliases=['p'],
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
        
        

    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
    run()

