import random
import settings
import discord
import openai

from discord.ext import commands

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

def run(): 
    intents = discord.Intents.default()
    intents.message_content = True 

    bot = commands.Bot(command_prefix="!", intents=intents, logging=logger)

    
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

    @bot.command()
    async def chat(ctx, *prompt):
        # Join the prompt arguments into a single string
        prompt_text = " ".join(prompt)

        # Generate response using GPT
        response = generate_response(prompt_text)
        if len(response) <= 2000:
            await ctx.send(response)
        else:
            # break response into smaller chunks of 2000 characters or less
            for chunk in [response[i:i+2000] for i in range(0, len(response), 2000)]:
                await ctx.send(chunk)

        # Send the response message back to the channel
        await ctx.send(response)
    # async def chat(ctx, *prompt):
    #     response = generate_response(prompt)
    #     if len(response) <= 2000:
    #         await ctx.send(response)
    #     else:
    #     # break response into smaller chunks of 2000 characters or less
    #         for chunk in [response[i:i+2000] for i in range(0, len(response), 2000)]:
    #             await ctx.send(chunk)





    # @bot.event
    # async def on_command_error(ctx, error):
    #     if isinstance(error, commands.MissingRequiredArgument):
    #         await ctx.send("Oops, something went wrong")

    bot.run(settings.DISCORD_API_SECRET, reconnect=True)
    

#TEST

if __name__ == "__main__":
    run()



