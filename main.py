# mapBot
# By: William Elias (howlcipher)
# Repository: https://github.com/howlcipher/mapBot
# LinkedIn: https://www.linkedin.com/in/wylelias/
# Created 05/2020

# imports

from discord.ext import commands

# custom modules
from botTime import botTime
from clear import clear
from help import helpCommands
from maps import availableMaps, mapCommands, lastten
from users import usersCommands

bot = commands.Bot(command_prefix='.')
bot.remove_command('help')

# signal for bot online

@bot.event
async def on_ready():
    print(f'Bot Name: {bot.user.name} - ID: {bot.user.id} is ready')


# initialized variables
currentMaps = mapCommands.Maps("No map set", "No map set", "No map set", "No botTime set")
setTime = botTime.sTime("no time set")
hostTime = botTime.sTime("")
currentHost = usersCommands.Host("No host set")
vsMapList = availableMaps.vsmapsdb

# commands
# custom help
@bot.command(pass_context=True)
async def help(ctx):
    await ctx.message.delete()
    await helpCommands.help(ctx)


# map commands
# sets maps to display if none picks randomly
@bot.command(name='setMapsRandom', help='Sets the maps to be played - RANDOM Modifiers(3,4,5)')
async def setMapsRandom(ctx, mapcount1=None, mapcount2=None, mapcount3=None):
    mapCommands.randomMapFilter(currentMaps, mapcount1, mapcount2, mapcount3)
    setTime.ct = botTime.currentTime()
    mapSetMessage = "@every1 maps are set at " + setTime.ct + '👍'
    print("setMapsRandom was run")
    await ctx.message.delete()
    await ctx.send(mapSetMessage)


@bot.command(name='setMap', help='Sets the maps to be played')
async def setMap(ctx, mapNum, mapID):
    if (int(mapNum) < 4):
        mapCommands.setMap(currentMaps, mapNum, mapID)
        setTime.ct = botTime.currentTime()
        mapSetMessage = (f"@every1 map {mapNum} is set at " + setTime.ct + '👍')
        print(f"setMap {mapNum} was run")
        await ctx.message.delete()
        await ctx.send(mapSetMessage)
    else:
        await ctx.message.delete()
        print(f"setMap {mapNum} was run")
        await ctx.send(f"Map {mapNum} is not a valid, try 1, 2, or 3.")

# display the maps selected and what botTime they were set
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
    print("displayMaps was run")
    await ctx.message.delete()


# display all maps
@bot.command(name='vsMaps', help='Displays all VS Maps')
async def vsMaps(ctx):
    # display all maps - limit of 2000 characters on discord
    author = ctx.message.author
    await author.send("ID, Map Name, Map Count")
    await author.send(availableMaps.vsmapsdbID)
    print("vsMaps was run")
    await ctx.message.delete()


# displays botTime and game botTime
@bot.command(name="gameTime", help="Displays current botTime and game botTime")
async def time(ctx):
    gameTime = "```Game botTime is at 21:30:00 EASTERN TIMEZONE```"
    curTime = botTime.currentTime()
    author = ctx.message.author
    print("gameTime was run")
    await author.send(curTime)
    await author.send(gameTime)
    await ctx.message.delete()


# Displays the last 10 maps
@bot.command(name="last10", help="Displays last 10 maps")
async def time(ctx):
    author = ctx.message.author
    await ctx.message.delete()
    print("last10 was run")
    await author.send(lastten.displayLastTen())


# Sends maps to lastten DB
@bot.command(name="played", help="Updates lastten DB with maps played")
async def time(ctx):
    author = ctx.message.author
    await ctx.message.delete()
    lastten.updateDB(currentMaps.m1)
    lastten.updateDB(currentMaps.m2)
    lastten.updateDB(currentMaps.m3)
    print("played was run")
    await author.send(lastten.displayLastTen())


# Host Commands
# host assigned
@bot.command(name='setHost', help='sets the host if not in the user_account database no host is set')
# @commands.has_role("testRole")
async def setHost(ctx, user):
    # # if user is in host list
    if (user in usersCommands.userDB):
        currentHost.host = user
        hostTime.ct = botTime.currentTime()

        theHost = currentHost.host + " will host"
        hostSetAt = "set at " + hostTime.ct
        await ctx.message.delete()
        print("setHost was run")
        await ctx.send(theHost)
        await ctx.send(hostSetAt)
    else:
        await ctx.message.delete()
        print("setHost was run")
        currentHost.host = "no host set"
        await ctx.send(currentHost.host)


# host display hosts
@bot.command(name='displayHosts', help='Displays possible hosts')
async def distplayHosts(ctx):
    author = ctx.message.author
    await author.send("USERNAME - BOT ADMIN - SERVER ROLE")
    await author.send(usersCommands.userDB)
    await ctx.message.delete()


# Clear commands
# clears the host
@bot.command(name='clearHost', help='clears the host')
async def clearHost(ctx):
    hostTime.ct = botTime.sTime("")
    clear.clearHost(currentHost)
    await ctx.message.delete()
    await ctx.send("Host is reset")


# clears maps
@bot.command(name='clearMaps', help='clears the maps')
async def clearMaps(ctx):
    hostTime.ct = botTime.sTime("")
    clear.clearMaps(currentMaps)
    await ctx.message.delete()
    print("clearMaps was run")
    await ctx.send("Maps are reset")


# clears a specific Map (1, 2, or 3)
@bot.command(name='clearMap', help='clears the maps')
async def clearMap(ctx, mapNum):
    hostTime.ct = botTime.sTime("")
    clear.clearMap(currentMaps, ctx, mapNum)
    await ctx.message.delete()
    print("clearMap was run")
    if (int(mapNum) < 4):
        await ctx.send(f"Map {mapNum} was reset")
    else:
        await ctx.send(f"Map {mapNum} is not valid")


# clears all
@bot.command(name='clearAll', help='clears the host and maps')
async def clearAll(ctx):
    hostTime.ct = botTime.sTime("")
    clear.clearHost(currentHost)
    clear.clearMaps(currentMaps)
    await ctx.message.delete()
    print("clearAll was run")
    await ctx.send("Maps and Host are reset")


# hide the token when committing
bot.run("TOKEN")
