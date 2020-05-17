# mapBot
# By: William Elias (howlcipher)
# Repository: https://github.com/howlcipher/mapBot
# LinkedIn: https://www.linkedin.com/in/wylelias/
# Created 05/2020

# imports
import os
import random
from datetime import datetime

import discord
import pytz
from discord.ext import commands

# other files
import available_maps
import users

# discord api
vsMapList = available_maps.vsmapsdb
bot = commands.Bot(command_prefix='.')
bot.remove_command('help')

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
    print(f'Bot Name: {bot.user.name} - ID: {bot.user.id} is ready')

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
def setMapRandom(mapcount=None):
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


# commands
# custom help
@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(
        colour=discord.Colour.green(),
        title="HELP COMMANDS FOR USING THE MAPBOT",
        description="How to use mapBot"
    )
    embed.set_author(name='mapBot')
    # map help
    embed.add_field(name='.addMap', value='adds a map to the database !!COMING SOON!!', inline=False)
    embed.add_field(name='.displayMaps', value='Displays current maps to be played', inline=False)
    embed.add_field(name='.setMaps', value='Sets specific maps !!COMING SOON!!', inline=False)
    embed.add_field(name='.setMapsRandom', value='Sets 3 random maps - 3,4,5 can be used to limit the number of rounds',
                    inline=False)
    embed.add_field(name='.vsMaps', value='Displays all VS maps', inline=False)

    # user help
    embed.add_field(name='.addUser', value='Adds user_account to the database !!COMING SOON!!', inline=False)
    embed.add_field(name='.displayHosts', value='Displays possible hosts', inline=False)
    embed.add_field(name='.setHost', value='Sets the host if not in the user_account database no host is set',
                    inline=False)

    # misc help
    embed.add_field(name='.gameTime', value='Displays current time and game time', inline=False)

    # dm the user asking for help
    author = ctx.message.author
    await author.send(author, embed=embed)


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
        m3 = int(mapcount3)

    currentMaps.m1 = setMapRandom(m1)
    currentMaps.m2 = setMapRandom(m2)
    currentMaps.m3 = setMapRandom(m3)

    setTime.ct = currentTime()
    mapSetMessage = "@everyone maps are set at " + setTime.ct + '👍'
    await ctx.send(mapSetMessage)


# sets maps to specific choices
@bot.command(name='setMaps', help='Sets the maps to be played !!COMING SOON!!')
async def setMaps(ctx):
    await ctx.send("setMaps Message")


# adds map to database
@bot.command(name='addMap', help='adds maps to the database !!COMING SOON!!')
async def setMaps(ctx):
    await ctx.send("addMap Message")


# adds user_account to database
@bot.command(name='addUser', help='adds user_account to the database !!COMING SOON!!')
async def setMaps(ctx):
    await ctx.send("addUser Message")


# display the maps selected and what time they were set
@bot.command(name='displayMaps', help='Displays the current maps to be played')
async def displayMaps(ctx):
    hostHelp = "To host copy the command: mm_dedicated_force_servers 74.91.124.232:27025 and paste into your in game console."
    tnMaps = "Tonight's maps are: \nMAP1: " + str(currentMaps.m1) + "\nMAP2: " + str(currentMaps.m2) + "\nMAP3: " + str(
        currentMaps.m3) + "\nMaps set at: " + setTime.ct
    cHost = "The host will be " + currentHost.host
    author = ctx.message.author
    await author.send(hostHelp)
    await author.send(tnMaps)
    await author.send(cHost)


# display all maps
@bot.command(name='vsMaps', help='Displays all VS Maps')
async def vsMaps(ctx):
    # display all maps - limit of 2000 characters on discord
    author = ctx.message.author
    await author.send(vsmapsDB[1:20])
    await author.send(vsmapsDB[21:40])
    await author.send(vsmapsDB[41:60])
    await author.send(vsmapsDB[61:])


# displays time and game time
@bot.command(name="gameTime", help="Displays current time and game time")
async def time(ctx):
    # use NY time zone

    gameTime = "```Game time is at 21:30:00 EASTERN TIMEZONE```"
    cur_time = currentTime()
    author = ctx.message.author
    await author.send(cur_time)
    await author.send(gameTime)


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
    author = ctx.message.author
    await author.send("USERNAME - BOT ADMIN - SERVER ROLE")
    await author.send(usersDB)


# token
token = os.environ.get("DISCORD_BOT_SECRET")
# hide the token when committing
bot.run("")
