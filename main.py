# imports
import os
import random
from datetime import datetime

import pytz
from discord.ext import commands

# other files
import available_maps

# discord api
vsMapList = available_maps.vsmaps
client = commands.Bot(command_prefix='.')


# load_dotenv()
# TOKEN = os.getenv('DISCORD_TOKEN')

# signal for bot online
@client.event
async def on_ready():
    print('bot is ready')


# variables
hosts = ["howlcipher", "MaShiro", "Merim", "$antic $pirit", "Sirius", "Cody", "KrayOn", "YourNameHere", "liqouridge",
         "PFletchJ", "shuppy30"]


# base Map
class Maps:
    def __init__(self, m1: str, m2: str, m3: str, ct: str):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.ct = ct


# base host
class Host:
    def __init__(self, host: str):
        self.host = host


# base ct
class sTime:
    def __init__(self, ct: str):
        self.ct = ct


# Null Object
currentMaps = Maps("MAP1: is unset", "MAP2: is unset", "MAP3: is unset", "No time set")
setTime = sTime("no time set")
hostTime = sTime("")
currentHost = Host("No host set")


# time
def currentTime():
    tz_NY = pytz.timezone('America/New_York')
    datetime_NY = datetime.now(tz_NY)
    return datetime_NY.strftime("%H:%M:%S")


# functions
# random number 1 - x
def randomNumber(x):
    return random.randint(1, x)


# random number
def randomMaps():
    maptotal = 65
    mapNums = {"map1": randomNumber(maptotal),
               "map2": randomNumber(maptotal),
               "map3": randomNumber(maptotal)}
    return mapNums


# set maps to be used with time stamp
@client.command(name='setMaps', help='Sets the maps to be played - MUST BE HOST or HIGHER')
@commands.has_role("testRole")
async def Mapset(ctx):
    mn = randomMaps()

    currentMaps.m1 = vsMapList[mn["map1"]]
    currentMaps.m2 = vsMapList[mn["map2"]]
    currentMaps.m3 = vsMapList[mn["map3"]]
    setTime.ct = currentTime()
    await ctx.send("@every1 maps are set at " + setTime.ct + '👍')


# display the maps selected and what time they were set
@client.command(name='displayMaps', help='Displays the current maps to be played')
async def displayMaps(ctx):
    await ctx.send(
        "To host copy the command: mm_dedicated_force_servers 74.91.124.232:27025 and paste into your in game console.")
    await ctx.send(
        "Tonight's maps are: \nMAP1: " + currentMaps.m1 + "\nMAP2: " + currentMaps.m2 + "\nMAP3: " + currentMaps.m3 + "\nMaps set at: " + setTime.ct)
    await ctx.send("The host will be " + currentHost.host)


# display all maps
@client.command(name='vsMaps', help='Displays all VS Maps - MUST BE HOST or HIGHER')
@commands.has_role("testRole")
async def vsMaps(ctx):
    for x, y in vsMapList.items():
        await ctx.send(x + ":" + y)


# displays time and game time
@client.command(name="gameTime", help="Displays current time and game time")
async def time(ctx):
    # use NY time zone
    cur_time = currentTime()
    await ctx.send(cur_time)
    await ctx.send("```Game time is at 21:30:00 EASTERN TIMEZONE```")


# host assigned
@client.command(name='setHost', help='sets the host - MUST BE HOST or HIGHER')
@commands.has_role("testRole")
async def setHost(ctx, user):
    # if user is in host list
    if (user in hosts):
        currentHost.host = user
        hostTime.ct = currentTime()
        await ctx.send(currentHost.host + " will host")
        await ctx.send("set at " + hostTime.ct)
    else:
        currentHost.host = "no host set"
        await ctx.send(currentHost.host)


# host display hosts
@client.command(name='displayHosts', help='displays possible hosts')
async def distplayHosts(ctx):
    await ctx.send(hosts)


# token
token = os.environ.get("DISCORD_BOT_SECRET")
client.run("YOUR TOKEN HERE")
