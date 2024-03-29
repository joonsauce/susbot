# used to import all bot settings
from setting import *

# help command; makes bot send description of every command it accepts
@bot.command()
async def help(ctx, *, msg=''):
    # sets embed as the discord embed
    embed = discord.Embed(
        # sets the sidebar of Discord embed to whatever color you want. setting it to None sets it to black.
        # you can use discord.colors.___() to choose your own color
        color=None
    )
    # sets the title of the embed as "sus bot help"
    embed.set_author(name="sus bot help")
    # if there is no message following the command, it displays all commands this bot has
    if msg == '':
        embed.add_field(name="bal", value='Allows user to check how much susCash they have. Usage: s!bal', inline=False)
        embed.add_field(name="drip", value='Plays Among Us Drip if user is connected to a voice channel. Usage: s!drip', inline=False)
        embed.add_field(name="help", value="Displays the help menu. Usage: s!help", inline=False)
        embed.add_field(name="join", value='Makes bot join the voice channel the user is in. Usage: s!join', inline=False)
        embed.add_field(name="leave", value='Makes bot leave the voice channel it is in. Usage: s!leave', inline=False)
        embed.add_field(name="pp", value='Pauses and resumes music playing. Usage: s!pp', inline=False)
        embed.add_field(name="roll", value='Makes bot run a simulated game of dice roll. Usage: s!roll', inline=False)
        embed.add_field(name="scan", value='Makes bot run an Among Us style medbay scan. Usage: s!scan <user>*', inline=False)
        embed.add_field(name="stop", value='Makes bot stop whatever music is playing. Usage: s!stop', inline=False)
        embed.add_field(name="sus", value='Susses another user. Usage: s!sus <user> <action>', inline=False)
        embed.add_field(name="susimg", value='Returns avatar of tagged user in Among Us character. Usage: s!susimg <user>*', inline=False)
        embed.add_field(name="suslogo", value='Returns the image of susbot logo. Usage: s!suslogo', inline=False)
        embed.add_field(name="susmeme", value='Returns a random meme from r/amongusmemes. Usage: s!susmeme', inline=False)
        embed.add_field(name="susrate", value='Returns susrate of tagged user. Usage: s!susrate <user>*', inline=False)
    # below is all of the separate commands you can get info about 
    elif msg == 'bal':
        embed.add_field(name="bal", value='Allows user to check how much susCash they have. Usage: s!bal',
                        inline=False)
    elif msg == 'drip':
        embed.add_field(name="drip", value='Plays Among Us Drip if user is connected to a voice channel. Usage: s!drip',
                        inline=False)
    elif msg == 'help':
        embed.add_field(name="help", value="Displays the help menu. Usage: s!help", inline=False)
    elif msg == 'join':
        embed.add_field(name="join", value='Makes bot join the voice channel the user is in. Usage: s!join',
                        inline=False)
    elif msg == 'leave':
        embed.add_field(name="leave", value='Makes bot leave the voice channel it is in. Usage: s!leave',
                        inline=False)
    elif msg == 'pp':
        embed.add_field(name="pp", value='Pauses and resumes music playing. Usage: s!pp', inline=False)
    elif msg == 'roll':
        embed.add_field(name="roll", value='Makes bot run a simulated game of dice roll. Usage: s!roll', inline=False)
    elif msg == 'scan':
        embed.add_field(name="scan", value='Makes bot run an Among Us style medbay scan of the user. Usage: s!scan',
                        inline=False)
    elif msg == 'stop':
        embed.add_field(name="stop", value='Makes bot stop whatever music is playing. Usage: s!stop', inline=False)
    elif msg == 'sus':
        embed.add_field(name="sus", value='Susses another user. Usage: s!sus <user> <action>', inline=False)
    elif msg == 'susimg':
        embed.add_field(name="susimg", value='Returns avatar of tagged user in Among Us character. Usage: s!susimg <user>*', inline=False)
    elif msg == 'suslogo':
        embed.add_field(name="nathansus", value='Returns the image of susbot logo. Usage: s!suslogo', inline=False)
    elif msg == 'susmeme':
        embed.add_field(name="susmeme", value='Returns a random meme from r/amongusmemes. Usage: s!susmeme', inline=False)
    elif msg == 'susrate':
        embed.add_field(name="susrate", value='Returns susrate of tagged user. Usage: s!susrate <user>*', inline=False)
    else:
        embed.add_field(name="No command", value='There is no command with that name. Use ~help to view the full list of commands', inline=False)
    
    # adds line indicating that a star means the element is optional
    embed.add_field(name="OTHER THINGS TO NOTE", value='Any element with a * beside it means the element is optional.')
    # makes the bot send the embed as the message
    await ctx.send(embed=embed)
