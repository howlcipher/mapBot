# imports
import os
import random
from datetime import datetime

import psycopg2
import pytz
from discord.ext import commands

# other files
import available_maps

# discord api
vsMapList = available_maps.vsmaps
bot = commands.Bot(command_prefix='.')

tdb = available_maps.vsmaps4
print(tdb[0])


# load_dotenv()
# TOKEN = os.getenv('DISCORD_TOKEN')

# signal for bot online
@bot.event
async def on_ready():
    print('bot is ready')


# database
conn = psycopg2.connect(
    database="mapBot",
    user="postgres",
    password="54321",
    host="localhost",
    port=5432
)

# testing sql query
print("connected to postgres SQL DB")
cur = conn.cursor()
data = cur.execute("SELECT * FROM maps")
stuff = cur.fetchall()


# testing database
@bot.command(name='testdb', help='database test')
async def databasetest(ctx):
    await ctx.send(stuff[1][2])


# map class
class Maps:
    def __init__(self, m1: str, m2: str, m3: str, ct: str):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.ct = ct


# host class
class Host:
    def __init__(self, host: str):
        self.host = host


# time class
class sTime:
    def __init__(self, ct: str):
        self.ct = ct


# initialized variables
currentMaps = Maps("MAP1: is unset", "MAP2: is unset", "MAP3: is unset", "No time set")
setTime = sTime("no time set")
hostTime = sTime("")
currentHost = Host("No host set")
hosts = ["howlcipher", "MaShiro", "Merim", "$antic $pirit", "Sirius", "Cody", "KrayOn", "YourNameHere", "liqouridge",
         "PFletchJ", "shuppy30"]


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
    maptotal = 1
    mapNums = {"map1": randomNumber(maptotal),
               "map2": randomNumber(maptotal),
               "map3": randomNumber(maptotal)}
    return mapNums



# set maps to be used with time stamp
@bot.command(name='setMaps', help='Sets the maps to be played - MUST BE HOST or HIGHER')
@commands.has_role("testRole")
async def Mapset(ctx):
    mn = randomMaps()

    currentMaps.m1 = vsMapList[mn["map1"]]
    currentMaps.m2 = vsMapList[mn["map2"]]
    currentMaps.m3 = vsMapList[mn["map3"]]
    setTime.ct = currentTime()
    mapSetMessage = "@every1 maps are set at " + setTime.ct + '👍'
    await ctx.send(mapSetMessage)


# display the maps selected and what time they were set
@bot.command(name='displayMaps', help='Displays the current maps to be played')
async def displayMaps(ctx):
    hostHelp = "To host copy the command: mm_dedicated_force_servers 74.91.124.232:27025 and paste into your in game console."
    tnMaps = "Tonight's maps are: \nMAP1: " + currentMaps.m1 + "\nMAP2: " + currentMaps.m2 + "\nMAP3: " + currentMaps.m3 + "\nMaps set at: " + setTime.ct
    cHost = "The host will be " + currentHost.host

    await ctx.send(hostHelp)
    await ctx.send(tnMaps)
    await ctx.send(cHost)


# display all maps
@bot.command(name='vsMaps', help='Displays all VS Maps - MUST BE HOST or HIGHER')
@commands.has_role("testRole")
async def vsMaps(ctx):
    for x, y in vsMapList.items():
        await ctx.send(x + ":" + y)


# displays time and game time
@bot.command(name="gameTime", help="Displays current time and game time")
async def time(ctx):
    # use NY time zone

    gameTime = "```Game time is at 21:30:00 EASTERN TIMEZONE```"
    cur_time = currentTime()
    await ctx.send(cur_time)
    await ctx.send(gameTime)


# host assigned
@bot.command(name='setHost', help='sets the host - MUST BE HOST or HIGHER')
@commands.has_role("testRole")
async def setHost(ctx, user):
    # if user is in host list
    if (user in hosts):
        currentHost.host = user
        hostTime.ct = currentTime()

        theHost = currentHost.host + " will host"
        hostSetAt = "set at " + hostTime.ct

        await ctx.send(theHost)
        await ctx.send(hostSetAt)
    else:
        currentHost.host = "no host set"
        await ctx.send(currentHost.host)


# host display hosts
@bot.command(name='displayHosts', help='displays possible hosts')
async def distplayHosts(ctx):
    await ctx.send(hosts)


# token
token = os.environ.get("DISCORD_BOT_SECRET")
# hide the token when committing
bot.run(TOKEN HERE)
