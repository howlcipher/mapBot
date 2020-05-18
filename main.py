# mapBot
# By: William Elias (howlcipher)
# Repository: https://github.com/howlcipher/mapBot
# LinkedIn: https://www.linkedin.com/in/wylelias/
# Created 05/2020

# imports
import os

import discord
from discord.ext import commands

# custom modules
from botTime import botTime
from clear import clear
from maps import availableMaps, mapCommands
from users import usersCommands

vsMapList = availableMaps.vsmapsdb
bot = commands.Bot(command_prefix='.')
bot.remove_command('help')


# signal for bot online

@bot.event
async def on_ready():
    print(f'Bot Name: {bot.user.name} - ID: {bot.user.id} is ready')


# initialized variables
currentMaps = mapCommands.Maps("MAP1: is unset", "MAP2: is unset", "MAP3: is unset", "No botTime set")
setTime = botTime.sTime("no botTime set")
hostTime = botTime.sTime("")
currentHost = usersCommands.Host("No host set")


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
        embed.add_field(name='.setMapsRandom',
                        value='Sets 3 random maps - 3,4,5 can be used to limit the number of rounds',
                        inline=False)
        embed.add_field(name='.vsMaps', value='Displays all VS maps', inline=False)

        # user help
        embed.add_field(name='.addUser', value='Adds user_account to the database !!COMING SOON!!', inline=False)
        embed.add_field(name='.displayHosts', value='Displays possible hosts', inline=False)
        embed.add_field(name='.setHost', value='Sets the host if not in the user_account database no host is set',
                        inline=False)

        embed.add_field(name='.clearHost', value='Clears the host', inline=False)
        embed.add_field(name='.clearMaps', value='Clears the maps', inline=False)
        embed.add_field(name='.clearAll', value='Clears the maps and host', inline=False)

        # misc help
        embed.add_field(name='.gameTime', value='Displays current time and game time', inline=False)

        # dm the user asking for help
        author = ctx.message.author
        await author.send(author, embed=embed)


# sets maps to display if none picks randomly
@bot.command(name='setMapsRandom', help='Sets the maps to be played - RANDOM Modifiers(3,4,5)')
async def setMapsRandom(ctx, mapcount1=None, mapcount2=None, mapcount3=None):
    mapCommands.randomMapFilter(currentMaps, mapcount1, mapcount2, mapcount3)
    setTime.ct = botTime.currentTime()
    mapSetMessage = "@every1 maps are set at " + setTime.ct + '👍'
    await ctx.send(mapSetMessage)


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


# display all maps
@bot.command(name='vsMaps', help='Displays all VS Maps')
async def vsMaps(ctx):
    # display all maps - limit of 2000 characters on discord
    author = ctx.message.author
    await author.send(availableMaps.vsmapsdb[1:20])
    await author.send(availableMaps.vsmapsdb[21:40])
    await author.send(availableMaps.vsmapsdb[41:60])
    await author.send(availableMaps.vsmapsdb[61:])


# displays botTime and game botTime
@bot.command(name="gameTime", help="Displays current botTime and game botTime")
async def time(ctx):
    gameTime = "```Game botTime is at 21:30:00 EASTERN TIMEZONE```"
    curTime = botTime.currentTime()
    author = ctx.message.author
    await author.send(curTime)
    await author.send(gameTime)


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
    await author.send(usersCommands.userDB)


# clears the host
@bot.command(name='clearHost', help='clears the host')
async def clearHosts(ctx):
    hostTime.ct = botTime.sTime("")
    clear.clearHost(currentHost)
    await ctx.send("Host is reset")


@bot.command(name='clearMaps', help='clears the maps')
async def clearMaps(ctx):
    hostTime.ct = botTime.sTime("")
    clear.clearMaps(currentMaps)
    await ctx.send("Maps are reset")


@bot.command(name='clearAll', help='clears the host and maps')
async def clearAll(ctx):
    hostTime.ct = botTime.sTime("")
    clear.clearHost(currentHost)
    clear.clearMaps(currentMaps)
    await ctx.send("Maps and Host are reset")


# token
token = os.environ.get("DISCORD_BOT_SECRET")
# hide the token when committing
bot.run("TOKEN")
