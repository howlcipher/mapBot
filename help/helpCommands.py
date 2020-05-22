import discord


async def help(self):
    embed = discord.Embed(
        colour=discord.Colour.green(),
        title="HELP COMMANDS FOR USING THE MAPBOT",
        description="How to use mapBot"
    )
    embed.set_author(name='mapBot')
    # map help
    embed.add_field(name='###MAPS COMMANDS###', value='-----', inline=False)
    embed.add_field(name='.displayMaps', value='Displays current maps to be played', inline=False)
    embed.add_field(name='.setMaps', value='Sets specific maps based on ID.  Use .vsMaps to see ID', inline=False)
    embed.add_field(name='.setMapsRandom',
                    value='Sets 3 random maps - 3,4,5 can be used to limit the number of rounds',
                    inline=False)
    embed.add_field(name='.last10', value='Displays the last ten maps that were set using .played', inline=False)
    embed.add_field(name='.played', value='Stores all .displayMaps into the lastten database', inline=False)
    embed.add_field(name='.vsMaps', value='Displays all VS maps', inline=False)

    # user help
    embed.add_field(name='###USER / HOST COMMANDS###', value='-----', inline=False)
    embed.add_field(name='.displayHosts', value='Displays possible hosts', inline=False)
    embed.add_field(name='.setHost', value='Sets the host if not in the user_account database no host is set',
                    inline=False)

    # clear help
    embed.add_field(name='###CLEAR COMMANDS###', value='------', inline=False)
    embed.add_field(name='.clearHost', value='Clears the host', inline=False)
    embed.add_field(name='.clearMaps', value='Clears all maps', inline=False)
    embed.add_field(name='.clearAll', value='Clears the maps and host', inline=False)

    # misc help
    embed.add_field(name='###MISC COMMANDS###', value='-----', inline=False)
    embed.add_field(name='.gameTime', value='Displays current time and game time', inline=False)

    # dm the user asking for help
    author = self.message.author
    await author.send(author, embed=embed)
    print("help was run")
    # await self.message.delete()
