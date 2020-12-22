import discord
from discord.ext import commands, tasks
from discord.voice_client import VoiceClient

from random import choice


client = commands.Bot(command_prefix='mr!')

client.remove_command('help')

status = ['MRadio|mr!help For Help|Join The Offical Server - https://discord.gg/fcCFtKWFb9']

@client.event
async def on_ready():
    change_status.start()
    print('Bot is online!')

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='general')
    await channel.send(f'Welcome {member.mention}!  Ready to jam out? See `mr!help` command for help!')
        
@client.command(pass_context=True)
async def invite(ctx):
    channel = ctx.message.channel
    embed = discord.Embed(
        colour = discord.Colour.blue()
    )
    embed.add_field(name="**Invite me!** ", value="[***CLICK ME***](https://discord.com/api/oauth2/authorize?client_id=779379817454895105&permissions=2147483639&scope=bot)")
    embed.set_footer(text="Mradio Offical Discord - https://discord.gg/hzDm9TBybq")
    await channel.send(embed=embed)


@client.command(aliases=["whois"])
async def userinfo(ctx, member: discord.Member = None):
    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=discord.Colour.purple(), timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}")

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Display Name:", value=member.display_name)

    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name="Roles:", value="".join([role.mention for role in roles]))
    embed.add_field(name="Highest Role:", value=member.top_role.mention)
    print(member.top_role.mention)
    await ctx.send(embed=embed)


@client.command(name='kick')
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    message = f"`You have been Kicked From {ctx.guild.name} For {reason}`"
    await member.send(message)
    await member.kick(reason=reason)
    await ctx.send(f'`User {member} Has Been Kicked.`')


@client.command(name='ping')
async def ping(ctx):
    await ctx.send(f'Latency: {round(client.latency * 1000)}ms')

@client.command(name='hello')
async def hello(ctx):
    responses = ['`Hello How You Doing`', '`Wussup`', '`How Is It Going`', '`Hi`', '`AYYY Hello`']
    await ctx.send(choice(responses))


@client.command() 
async def purge(ctx, *, limit: int): 
    await ctx.channel.purge(limit=limit + 1) 
    await ctx.send("`Purged Messages`")













@client.command()
async def help(ctx):

    embed = discord.Embed(
        colour=discord.Colour.blue(),
    )

    embed.set_author(name="Commands:")
    embed.add_field(name="mr!ping (website)", value="Pings A Website And Replys With Its Latency", inline=False)
    embed.add_field(name="mr!kick (User) (Reason)", value="Kicks A User From The Server", inline=False)
    embed.add_field(name="mr!join", value="Makes The Bot Join The Voice Channel You Are In", inline=False)
    embed.add_field(name="mr!leave", value="Makes The Bot Leave The Voice Channel You Are In", inline=False)
    embed.add_field(name="mr!queue (Song Name Or Youtube Link To Song)", value="Makes The Bot Add The Song To The Queue", inline=False)
    embed.add_field(name="mr!play (Song Name Or Link)", value="Makes The Bot Play The Song", inline=False)
    embed.add_field(name="mr!pause", value="Makes The Bot Stop The Song Playing", inline=False)
    embed.add_field(name="mr!resume", value="Makes The Bot Play The Paused Song", inline=False)
    embed.add_field(name="mr!stop", value="Makes The Bot Stop The Song That Is Playing", inline=False)
    embed.add_field(name="mr!view", value="Makes The Bot Show The Song Queue", inline=False)
    embed.add_field(name="mr!purge (Number Of Messages)", value="Makes The Bot Delete The Amount Of Messages Mentioned", inline=False)
    embed.add_field(name="mr!credits", value="Makes The Bot Show The Bot Credits", inline=False)
    embed.add_field(name="mr!hello", value="Makes The Bot Send A Random Welcome Message", inline=False)
    embed.add_field(name="mr!invite", value="Makes The Bot Send A Bot Invite link", inline=False)
    embed.add_field(name="mr!discord", value="Makes The Bot Send The Offical Mradio Server Link", inline=False)
    embed.add_field(name="More Commands", value="More Commands Will Be Added Soon", inline=False)
    embed.set_footer(text="Mradio Offical Discord - https://discord.gg/hzDm9TBybq")

    await ctx.send(embed=embed)

@client.command()
async def credits(ctx):

    embed = discord.Embed(
        colour=discord.Colour.blue(),
    )

    embed.set_author(name="Credits:")
    embed.add_field(name="Rush Mr.SA Weston#2725", value="Discord Server/Radio Owner", inline=False)
    embed.add_field(name="Nathan545#5134", value="Discord Server/Radio Owner", inline=False)
    embed.add_field(name="S1N Slinky#2922", value="Bot Developer", inline=False)
    embed.add_field(name="1Ace#0001", value="Bot Developer/Helped With Commands", inline=False)
    embed.add_field(name="**Discord Invite** ", value="[***CLICK ME***](https://discord.gg/hzDm9TBybq)")
    embed.set_footer(text="Mradio Offical Discord - https://discord.gg/hzDm9TBybq")

    await ctx.send(embed=embed)


@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))

client.run('Nzc5Mzc5ODE3NDU0ODk1MTA1.X7fsBA.6ltdBHQ1r_oZVRndCnwvk7z5K0M')