# imports
import os
import random
from datetime import datetime

import pytz
from discord.ext import commands

# other files
import available_maps
import users

# discord api
vsMapList = available_maps.vsmapsdb
bot = commands.Bot(command_prefix='.')

# connect to databases of maps and useraccounts
# maps db

# all maps
vsmapsDB = available_maps.vsmapsdb
# maps with 3
mappool3 = available_maps.vsmapsdb3
# maps with 4
mappool4 = available_maps.vsmapsdb4
# maps with 5
mappool5 = available_maps.vsmapsdb5

# users db
usersDB = users.userdb


# signal for bot online
@bot.event
async def on_ready():
    print('bot is ready')


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
def randomMaps(mapTotal):
    mapNums = {"map1": randomNumber(mapTotal),
               "map2": randomNumber(mapTotal),
               "map3": randomNumber(mapTotal)}
    return mapNums


# setting the map
def setMap(mapcount=None):
    if (mapcount is not None):
        # set map
        mapcount = int(mapcount)
        if (mapcount == 3):
            mn = randomMaps(len(mappool3) - 1)
            return mappool3[mn["map1"]][0] + ": " + mappool3[mn["map1"]][1] + "MAP COUNT:" + mappool3[mn["map1"]][2]
        elif (mapcount == 4):
            mn = randomMaps(len(mappool4) - 1)
            return mappool4[mn["map1"]][0] + ": " + mappool4[mn["map1"]][1] + "MAP COUNT:" + mappool4[mn["map1"]][2]
        elif (mapcount == 5):
            mn = randomMaps(len(mappool5) - 1)
            return mappool5[mn["map1"]][0] + ": " + mappool5[mn["map1"]][1] + "MAP COUNT:" + mappool5[mn["map1"]][2]
        else:
            mn = randomMaps(len(vsmapsDB) - 1)
            return vsmapsDB[mn["map1"]][0] + ": " + vsmapsDB[mn["map1"]][1] + "MAP COUNT:" + vsmapsDB[mn["map1"]][2]
    else:
        mn = randomMaps(len(vsmapsDB) - 1)
        return vsmapsDB[mn["map1"]][0] + ": " + vsmapsDB[mn["map1"]][1] + "MAP COUNT:" + vsmapsDB[mn["map1"]][2]


# sets maps to display if none picks randomly
@bot.command(name='setMapsRandom', help='Sets the maps to be played - RANDOM Modifiers(3,4,5)')
async def setMapsRandom(ctx, mapcount1=None, mapcount2=None, mapcount3=None):
    m1 = mapcount1
    m2 = mapcount2
    m3 = mapcount3

    if (mapcount1 is not None):
        m1 = int(mapcount1)
    if (mapcount2 is not None):
        m2 = int(mapcount2)
    if (mapcount3 is not None):
        m3 = (mapcount3)

    currentMaps.m1 = setMap(m1)
    currentMaps.m2 = setMap(m2)
    currentMaps.m3 = setMap(m3)

    setTime.ct = currentTime()
    mapSetMessage = "@every1 maps are set at " + setTime.ct + '👍'
    await ctx.send(mapSetMessage)


# display the maps selected and what time they were set
@bot.command(name='displayMaps', help='Displays the current maps to be played')
async def displayMaps(ctx):
    hostHelp = "To host copy the command: mm_dedicated_force_servers 74.91.124.232:27025 and paste into your in game console."
    tnMaps = "Tonight's maps are: \nMAP1: " + str(currentMaps.m1) + "\nMAP2: " + str(currentMaps.m2) + "\nMAP3: " + str(
        currentMaps.m3) + "\nMaps set at: " + setTime.ct
    cHost = "The host will be " + currentHost.host

    await ctx.send(hostHelp)
    await ctx.send(tnMaps)
    await ctx.send(cHost)


# display all maps
@bot.command(name='vsMaps', help='Displays all VS Maps')
async def vsMaps(ctx):
    # display all maps - limit of 2000 characters on discord
    await ctx.send(vsmapsDB[1:20])
    await ctx.send(vsmapsDB[21:40])
    await ctx.send(vsmapsDB[41:60])
    await ctx.send(vsmapsDB[61:])


# displays time and game time
@bot.command(name="gameTime", help="Displays current time and game time")
async def time(ctx):
    # use NY time zone

    gameTime = "```Game time is at 21:30:00 EASTERN TIMEZONE```"
    cur_time = currentTime()
    await ctx.send(cur_time)
    await ctx.send(gameTime)


# host assigned
@bot.command(name='setHost', help='sets the host if not in the user_account database no host is set')
# @commands.has_role("testRole")
async def setHost(ctx, user):
    # # if user is in host list
    if (user in usersDB):
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
@bot.command(name='displayHosts', help='Displays possible hosts')
async def distplayHosts(ctx):
    await ctx.send("USERNAME - BOT ADMIN - SERVER ROLE")
    await ctx.send(usersDB)


# token
token = os.environ.get("DISCORD_BOT_SECRET")
# hide the token when committing
bot.run("INSERT TOKEN HERE")
