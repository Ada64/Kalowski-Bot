import discord
from discord.ext import commands
import random
import requests
import datetime
import time
import json
import aiohttp









bot = commands.Bot(command_prefix=";")
bot.remove_command('help')
start_time = time.time()

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(
        type=discord.ActivityType.competing, name='a race | ;help'
    ))
    
    print("Notification | Bot has been turned on!")
    

    
        




@bot.command()
async def ping(ctx):
  
    await ctx.send(f'Pong! `{round(bot.latency * 1000)}ms`')
    
"""Gets the bot latency"""
  


@bot.command()
async def members(ctx):
  mbed = discord.Embed(
    color=discord.Color(0xffff),
    title=f'{ctx.guild.name}'
  )
  mbed.set_thumbnail(url=f'{ctx.guild.icon_url}')
  mbed.add_field(name='Member Count', value=f'{ctx.guild.member_count}')
  mbed.set_footer(icon_url=f'{ctx.guild.icon_url}',text=f'Guild ID: {ctx.guild.id}')
  await ctx.send(embed=mbed)
  
  
@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
  """Kicks the user mentioned."""
  if ctx.author.guild_permissions.kick_members:
   await member.kick(reason=reason)
  await ctx.send(f'Kicked {member}.')
  
  if not ctx.author.guild_permissions.kick_members:
    await ctx.send("You do not have permission to run this command.")
    



"""Kicks the user mentioned."""

@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
  """Bans the user mentioned."""
  if ctx.author.guild_permissions.ban_members:
   await member.ban(reason=reason)
  await ctx.send(f'Banned {member}.')

  
  if not ctx.author.guild_permissions.ban_members:
    await ctx.send("You do not have permission to run this command.")

    

@bot.command()
async def userinfo(ctx, user: discord.Member=None):

    if not user: # this command took forever to redo for the no user lol
        embed = discord.Embed(title="Your info", color=0x176cd5)
        embed.add_field(name="Username", value=ctx.message.author.name + "#" + ctx.message.author.discriminator, inline=True)
        embed.add_field(name="ID", value=ctx.message.author.id, inline=True)
        embed.add_field(name="Status", value=ctx.message.author.status, inline=True)
        embed.add_field(name="Highest role", value=ctx.message.author.top_role)
        embed.add_field(name="Roles", value=len(ctx.message.author.roles))
        embed.add_field(name="Game", value=ctx.message.author.game)
        embed.add_field(name="Joined", value=ctx.message.author.joined_at)
        embed.add_field(name="Created", value=ctx.message.author.created_at)
        embed.add_field(name="Bot?", value=ctx.message.author.bot)
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        await bot.say(embed=embed)
    
    else:
        embed = discord.Embed(title="{}'s info".format(user), color=0x176cd5)
        embed.add_field(name="Username", value=user.name + "#" + user.discriminator, inline=True)
        embed.add_field(name="ID", value=user.id, inline=True)
        embed.add_field(name="Status", value=user.status, inline=True)
        embed.add_field(name="Highest role", value=user.top_role)
        embed.add_field(name="Roles", value=len(user.roles))
        
        embed.add_field(name="Joined", value=user.joined_at)
        embed.add_field(name="Created", value=user.created_at)
        embed.add_field(name="Bot?", value=user.bot)
        embed.set_thumbnail(url=user.avatar_url)
        embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
       
      
@bot.command()
async def avatar(ctx, user: discord.Member=None):
    """Displays users avatar."""
    if not user:
        embed = discord.Embed(color=0x176cd5)
        embed = discord.Embed(title="View full image.", url=ctx.message.author.avatar_url, color=0x176cd5)
        embed.set_image(url=ctx.message.author.avatar_url)
        embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    
    else:
        embed = discord.Embed(color=0x176cd5)
        embed = discord.Embed(title="View full image.", url=user.avatar_url, color=0x176cd5)
        embed.set_image(url=user.avatar_url)
        embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
       
@bot.command()
async def diceroll(ctx):
    responses = ['You rolled a 1!',
    'You rolled a 2!',
    'You rolled a 3!',
    'You rolled a 4!',
    'You rolled a 5!',
    'You rolled a 6!',
    'You rolled a 7!',
    'You rolled a 8!',
    'You rolled a 9!']
    mbed = discord.Embed(
        title = 'Dice Rolled!',
        description = f'{random.choice(responses)}'
    )
    mbed.set_thumbnail(url='https://images-ext-2.discordapp.net/external/kAegJWUTO1muMX0U5mEKgKSmpHuNl4it6086g2F3pCw/https/gilkalai.files.wordpress.com/2017/09/dice.png?width=80&height=77')
    await ctx.send(embed=mbed)
    

@bot.command(aliases=["howgayy"])
async def howgay(ctx):
    mbed = discord.Embed(
        title="howgay machine",
        description=f'You are {random.randint(1, 100)}% gay.'

    )
    mbed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Gay_Pride_Flag.svg/640px-Gay_Pride_Flag.svg.png")
    await ctx.send(embed=mbed)
  
   
@bot.command()
async def unban(ctx, *, member):
  if ctx.author.guild_permissions.ban_members:
    
   banned_users = await ctx.guild.bans()
  member_name, member_discriminator = member.split('#')

  for ban_entry in banned_users:
    user = ban_entry.user


    if(user.name, user.discriminator) == (member_name, member_discriminator):
      await ctx.guild.unban(user)
      await ctx.send(f'Unbanned {member}.')
 
  if not ctx.author.guild_permissions.ban_members:
    await ctx.send("You do not have permission to run this command.")
    
 


@bot.command()
async def poll(ctx,*,message):
  emb=discord.Embed(title=f"Poll by {ctx.author.name}", description=f'{message}')
  msg=await ctx.send(embed=emb)
   
  await msg.add_reaction('ðŸ‘')
  await msg.add_reaction('ðŸ‘Ž')
@bot.command()
async def ask(ctx, *, question):
    responses = ["It is certain.",
"It is decidedly so.",
"Without a doubt.",
"Yes - definitely.",
"You may rely on it.",
"As I see it, yes.",
"Most likely.",
"Outlook good.",
"Yes.",
"Signs point to yes.",
"Reply hazy, try again.",
"Ask again later.",
"Better not tell you now.",
"Cannot predict now.",
"Concentrate and ask again.",
"Don't count on it.",
"My reply is no.",
"My sources say no.",
"Outlook not so good.",
"Very doubtful."]
    await ctx.send(f':8ball: {random.choice(responses)}')
    
@bot.command()
async def cat(ctx):
            response = requests.get('https://aws.random.cat/meow')
            data = response.json()
            await ctx.send(data['file'])
            

@bot.command()
async def dog(ctx):
            response = requests.get('https://dog.ceo/api/breeds/image/random')
            data = response.json()
            await ctx.send(data['message'])
           
@bot.command()
async def coinflip(ctx):
        """Flips a coin."""
        coinsides = ["Heads", "Tails"]
        await ctx.send(f"**{ctx.author.name}** flipped a coin and got **{random.choice(coinsides)}**!")

@bot.command()
async def help(ctx, args=None):
    help_embed = discord.Embed(title="Adurite's Commands")
    command_names_list = [x.name for x in bot.commands]

    # If there are no arguments, just list the commands:
    if not args:
        help_embed.add_field(
            name="List of supported commands:",
            value="\n".join([str(i+1)+". "+x.name for i,x in enumerate(bot.commands)]),
            inline=False
        )
        help_embed.add_field(
            name="Details",
            value="Type `;help <command name>` for more details about each command.",
            inline=False
        )

    # If the argument is a command, get the help text from that command:
    elif args in command_names_list:
        help_embed.add_field(
            name=args,
            value=bot.get_command(args).help
        )

    # If someone is just trolling:
    else:
        help_embed.add_field(
            name="Nope.",
            value="Don't think I got that command, boss!"
        )

    await ctx.send(embed=help_embed)
   

@bot.command()
async def createchannel(ctx, channelName):
    guild = ctx.guild

    mbed = discord.Embed(
        title = 'Success',
        description = "{} has been successfully created.".format(channelName)

    )
    if ctx.author.guild_permissions.manage_channels:
        await guild.create_text_channel(name='{}'.format(channelName))
        await ctx.send(embed=mbed)
    
    if not ctx.author.guild_permissions.manage_channels:
      await ctx.send("You do not have permission to run this command.")
   

@bot.command()
async def uptime(ctx):
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        embed = discord.Embed(colour=ctx.message.author.top_role.colour)
        embed.add_field(name="Uptime", value=text)
        
        try:
            await ctx.send(embed=embed)
         
        except discord.HTTPException:
            await ctx.send("Current uptime: " + text)
        
@bot.command()
async def deletechannel(ctx, channel: discord.TextChannel):
    mbed = discord.Embed(
        title = 'Success',
        description = f'{channel} has been deleted.',
    )
    if ctx.author.guild_permissions.manage_channels:
        await ctx.send(embed=mbed)
      
        await channel.delete()
    if not ctx.author.guild_permissions.manage_channels:
      await ctx.send("You do not have permission to run this command.")
  

@bot.command()
async def fox(ctx):
            response = requests.get('https://randomfox.ca/floof/')
            data = response.json()
            await ctx.send(data['image'])
            


@bot.command()
async def mock(ctx, *, message):
    out = ''.join(random.choice((str.upper, str.lower))(c) for c in message)

    await ctx.send(out)
@bot.command()
async def randomnum(ctx):
    svay = random.randint(1,2000)
    await ctx.send(f'The random number generated is: **{svay}**')
@bot.command()
async def vote(ctx):
    embed = discord.Embed(
    title = "Voting for Adurite",
    description = "We would really appreciate if you voted for Adurite [here](https://top.gg/bot/925509847364010054). Thanks!"
    )
    await ctx.send(embed=embed)



@bot.command()
async def joke(ctx):
     
        api = 'https://icanhazdadjoke.com/'
        async with aiohttp.request('GET', api, headers={'Accept': 'text/plain'}) as r:
            result = await r.text()
            await ctx.send(result)

bot.run("token")

