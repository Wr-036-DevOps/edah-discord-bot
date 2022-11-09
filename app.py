import asyncio
from datetime import date, datetime
from urllib import response
from nextcord import Intents
from nextcord.ext import commands
import requests, json
import random
import datetime

# store the json file in a dict to access its content
links = json.load(open("gifs.json"))

intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='dog ',intents=intents)

#user: dog pic

@bot.command(name='hi')
async def SendMessage(ctx):
    await ctx.send("Hello")


@bot.command(name="pic")
async def Dog(ctx):
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    image_link = response.json()["message"]
    await ctx.send(image_link)


@bot.command(name="gif", aliases=["feed", "play", "sleep"])
async def Gif(ctx):
    await ctx.send(random.choice(links[ctx.invoked_with]))

# bot sends message on schedule
async def schedule_daily_messages():
    now = datetime.datetime.now()
    #then = now+datetime.timedelta(days=1)
    then = now.replace(hour=19, minute=10)
    if then < now:
        then += now+datetime.timedelta(days=1)
    wait_time = (then-now).total_seconds()
    await asyncio.sleep(wait_time)

    channel = 1035105321233960983
    await channel.send("Good morning!!")
    await channel.send(random.choice(links["play"]))


# what if user schedules a message
@bot.command(name="daily")
async def daily(ctx, mystr:str, hour:int, minute:int, second:int):
	print(mystr, hour, minute, second)

	if not (0 < hour < 24 and 0 <= minute <= 60 and 0 <= second < 60):
		raise commands.BadArgument()

	time = datetime.time(hour, minute, second)
	timestr = time.strftime("%I:%M:%S %p")
	await ctx.send(f"A daily message will be sent at {timestr} everyday in this channel.\nDaily message:\"{mystr}\"\nConfirm by simply saying: `yes`")

@daily.error
async def daily_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		await ctx.send("""Incorrect format. Use the command this way: `dog daily "message" hour minute second`.
For example: `dog daily "good morning" 22 30 0` for a message to be sent at 10:30 everyday""")



@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name}")
    await schedule_daily_messages()


if __name__ == '__main__':
    bot.run("MTAzNTEwMjI5MjczMjU1MTE3Mg.GipkK9.sAjv5rObqd7HQH5RoAJRazdv28I5enESes8lBY")