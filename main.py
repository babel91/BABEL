

import settings
import discord
from discord.ext import commands


logger = settings.logging.getLogger("bot")


def run():
    intents = discord.Intents.default()
    
    bot = commands.Bot(command_prefix="!", intents=intents)
    
    @bot.event
    async def on_ready():
        
        logger.info(f"User {bot.user}(ID: {bot.user.id})")

        channel = bot.get_channel(int(settings.CH_BOTS))
        await channel.send("Hello, I'm back!")

    @bot.command
    async def ping(ctx):
        await ctx.send("pong")
        
    
    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
    run()

