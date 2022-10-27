from nextcord import Intents
from nextcord.ext import commands

intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='hi',intents=intents)

@bot.command(name='dog')
async def SendMessage(ctx):
    await ctx.send("Hello")


@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name}")


if __name__ == '__main__':
    bot.run("Your token")