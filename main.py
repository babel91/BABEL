

import random
import settings
import discord
import openai

# import error_handling
# import bot_commands



from discord.ext import commands

intents = discord.Intents().all()
client = discord.Client(intents=intents)

logger = settings.logging.getLogger("bot")

class Slapper(commands.Converter):

    use_nicknames : bool

    def __init__(self, *, use_nicknames) -> None:
        self.use_nicknames = use_nicknames

    async def convert(self,ctx,argument):
        someone = random.choice(ctx.guild.members)
        nickname = ctx.author
        if self.use_nicknames:
            nickname = ctx.author.nick
        else:
            nickname = ctx.author
        return f"{nickname} slaps {someone} with {argument}"

def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = response.choices[0].text.strip()
    return message

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    if message.content.startswith("!chat"):
        prompt = message.content.replace("!chat", "")
        response = generate_response(prompt)
        await message.channel.send(response)


    client.run(settings.OPENAI_API_KEY)






def run(): 
    intents = discord.Intents.default()
    intents.message_content = True 

    bot = commands.Bot(command_prefix="!", intents=intents)

    
    @bot.event
    async def on_ready():

        logger.info(f"User {bot.user}(ID: {bot.user.id})")

        channel = bot.get_channel(int(settings.CH_BOTS))
        await channel.send("Hello, I'm back!"),
    
    @bot.command(
            aliases=['p'],
            help = "This is hälp",
            description = "This is description",
            brief = "Short Explained",
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
    
    @bot.command()
    async def add(ctx, one : int , two : int):
        """Adds two numbers"""
        await ctx.send(one + two)

    # @bot.error
    # async def add_error(ctx, error):
    #     if isinstance(error, commands.MissingRequiredArgument):
    #         await ctx.send("handled error locally")  
    
    @bot.command()
    async def joined(ctx, who : discord.Member):
        """Who joined when?"""
        await ctx.send(who.joined_at)

    @bot.command()
    async def slap(ctx, tool : Slapper(use_nicknames=False)):
        await ctx.send(tool)
    
    @bot.command()
    async def clear(ctx, amount=5):
        """Clears given number of messages"""
        await ctx.channel.purge(limit=amount+1)

    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Oops, something went wrong")





    bot.run(settings.DISCORD_API_SECRET, root_logger=True)


    


if __name__ == "__main__":
    run()




