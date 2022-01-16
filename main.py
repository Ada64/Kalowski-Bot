import discord, os, keep_alive, json, asyncio, aiofiles
from discord.ext import commands, tasks
from keep_alive import keep_alive
from replit import db
import requests
import aiohttp
import datetime
import time

start_time = time.time()

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=commands.when_mentioned_or('+'), intents=intents)
client.remove_command('help')
token = os.environ.get('DISCORD_BOT_SECRET')
client.warnings = {}

@client.event
async def on_ready():
  for guild in client.guilds:
        client.warnings[guild.id] = {}
    
        async with aiofiles.open(f"./data/{guild.id}.txt", mode="a") as temp:
            pass

        async with aiofiles.open(f"./data/{guild.id}.txt", mode="r") as file:
            lines = await file.readlines()

            for line in lines:
                data = line.split(" ")
                member_id = int(data[0])
                admin_id = int(data[1])
                reason = " ".join(data[2:]).strip("\n")

                try:
                    client.warnings[guild.id][member_id][0] += 1
                    client.warnings[guild.id][member_id][1].append((admin_id, reason))

                except KeyError:
                    client.warnings[guild.id][member_id] = [1, [(admin_id, reason)]] 

  print('bot online!')

  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name='a food fight'))


@client.event
async def on_reaction_add(reaction, user):
  if str(reaction.emoji) == "<:Retweet:846635554204287006>":
    if reaction.count >= 4:
      try:
        print(db["rt"][str(reaction.message.id)])
      except KeyError:
        channel = client.get_channel(895406253822595082)
        embed = discord.Embed(title='Trending message', color=0xE4F5F2, url=reaction.message.jump_url)
        embed.add_field(name='Message:', value=reaction.message.content, inline=False)
        embed.set_author(name=reaction.message.author, icon_url=reaction.message.author.avatar_url)
        await channel.send(content=f"{reaction.message.author.mention} your message is now trending!", embed=embed)
        db["rt"][str(reaction.message.id)] = "yes"

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user:discord.User=None, *, reason=None):
  if reason == None:
    reason = '(none provided)'
  if user == None:
    await ctx.send('You forgot to mention a user!')
  elif user.id == ctx.author.id:
    await ctx.message.reply("You can't ban yourself moron")
  else:
    try:
      embed = discord.Embed(title='Banned', description='You have been banned from **The Cloud Network**', color=0xFF0000)
      embed.add_field(name='Moderator:', value=ctx.author)
      embed.add_field(name='Reason:', value=reason)
      await user.send(embed=embed)
      message = f'Successfully banned **{user}** for *{reason}*!'
    except:
      message = f'Failed to send message to {user}, but banned anyways.'
    guild1 = client.get_guild(762659154976047166)
    guild2 = client.get_guild(798268275167461417)
    with open('./data/warns.json', 'r') as f:
      warns = json.load(f)
      warns[str(user.id)] = 0
    with open('./data/warns.json', 'w') as f:
      json.dump(warns, f, indent=4)
    try:
      await guild1.ban(user, reason=f'Banned by {ctx.author} for {reason}')
      await guild2.ban(user, reason=f'Banned by {ctx.author} for {reason}')
      await ctx.send(message)
      embed = discord.Embed(title='Ban', color=0xFF0000)
      embed.add_field(name='Moderator:', value=ctx.author)
      embed.add_field(name='Reason:', value=reason)
      embed.set_author(name=user, icon_url=user.avatar_url)
      channel1 = client.get_channel(857352076565020682)
      channel2 = client.get_channel(857350753202995210)
      await channel1.send(embed=embed)
      await channel2.send(embed=embed)
    except:
      await ctx.send(f'An error has occurred and I sadly could not ban **{user}**.')
      


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user:discord.User=None, *, reason=None):
  if reason == None:
    reason = '(none provided)'
  if user == None:
    await ctx.send('You forgot to mention a user!')
  elif user.id == ctx.author.id:
    await ctx.message.reply("You can't kick yourself moron")
  else:
    try:
      embed = discord.Embed(title='Kicked', description='You have been kicked from **The Cloud Network**', color=0xFF0000)
      embed.add_field(name='Moderator:', value=ctx.author)
      embed.add_field(name='Reason:', value=reason)
      await user.send(embed=embed)
      message = f'Successfully kicked {user} for {reason}!'
    except:
      message = f'Failed to send message to {user}, but kicked anyways'
    guild1 = client.get_guild(762659154976047166)
    guild2 = client.get_guild(798268275167461417)
    try:
      await guild1.kick(user, reason=f'Kicked by {ctx.author} for {reason}')
      await guild2.kick(user, reason=f'Kicked by {ctx.author} for {reason}')
      await ctx.send(message)
      embed = discord.Embed(title='Kick', color=0xFF0000)
      embed.add_field(name='Moderator:', value=ctx.author)
      embed.add_field(name='Reason:', value=reason)
      embed.set_author(name=user, icon_url=user.avatar_url)
      channel1 = client.get_channel(857352076565020682)
      channel2 = client.get_channel(857350753202995210)
      await channel1.send(embed=embed)
      await channel2.send(embed=embed)
      try:
        del db["warns"][str(user.id)]
      except KeyError:
        pass
    except:
      await ctx.send(f'An error has occurred and i could not kick {user}')  

@client.command(help='Gives the user mentioned a warning. 5 warnings lead to a kick.')
@commands.has_permissions(kick_members=True)
async def warn(ctx, member: discord.Member=None, *, reason=None):
    if member is None:
        return await ctx.reply("The provided member could not be found or you forgot to provide one.")

    if reason is None:
        return await ctx.reply("Please provide a reason for warning this user.")

    try:
        client.warnings[ctx.guild.id][member.id][0] += 1
        client.warnings[ctx.guild.id][member.id][1].append((ctx.author.id, reason))

    except KeyError:
        client.warnings[ctx.guild.id][member.id] = [1, [(ctx.author.id, reason)]]

    count = client.warnings[ctx.guild.id][member.id][0]

    async with aiofiles.open(f"./data/{ctx.guild.id}.txt", mode="a") as file:
        await file.write(f"{member.id} {ctx.author.id} {reason}\n")

 
    await ctx.reply(f"Successfully warned **{member}**! They now have **{count}** warning(s).")
@client.command()
@commands.has_permissions(kick_members=True)
async def checkmerits(ctx, user:discord.User=None):
  if user == None:
    user = ctx.author
  try:
    if user == ctx.author:
      await ctx.send(f'You have {db["merits"][str(user.id)]} merits')
    else:
      await ctx.send(f'{user} has {db["merits"][str(user.id)]} merits') 
  except KeyError:
    if user == ctx.author:
      await ctx.send('You have no merits')
    else:
      await ctx.send(f'{user} has no merits') 
      if not ctx.guild_permissions.kick_members:
        await ctx.send("You do not have permission to run this command.")

@client.command(help='Clears the warns of the specified user')
@commands.has_permissions(kick_members=True)
async def clearwarns(ctx, user:discord.User=None):
  if user == None:
    await ctx.message.reply('You forgot to mention a user!')
  elif user == ctx.author:
    await ctx.message.reply("Stop trying to remove your own warns moron")
  else:
    if db["warns"][str(user.id)] == 0:
      await ctx.message.reply('User has no warns!')
    else:
      channel1 = client.get_channel(857352076565020682)
      channel2 = client.get_channel(857350753202995210)
      db["warns"][str(user.id)] = 0
      await ctx.send(f'Successfully removed warns from {user}!')

      

@client.command()
async def ping(ctx):
  await ctx.reply('Pong! :ping_pong:')
  await ctx.send(f'My current speed is `{round(client.latency * 1000)}ms`.')


@client.command()
@commands.has_permissions(kick_members=True)
async def warns(ctx, member: discord.Member=None):
    if member is None:
        return await ctx.reply("The provided member could not be found or you forgot to provide one.")

    embed = discord.Embed(title=f"Displaying Warnings for {member.name}", description="", colour=discord.Colour.red())
    try:
        i = 1
        for admin_id, reason in client.warnings[ctx.guild.id][member.id][1]:
            admin = ctx.guild.get_member(admin_id)
            embed.description += f"**Warning {i}** given by: {admin.mention} for: *'{reason}'*.\n"
            i += 1

        await ctx.reply(embed=embed)

    except KeyError: 
        await ctx.reply("This user has no warnings.")

@client.command()
async def vote(ctx):
  embed = discord.Embed(title='Voting Links', description='Use these links to upvote/rate the server', color=0xA9CCE3)
  embed.add_field(name='Links:',value='[Top.gg](https://top.gg/servers/798268275167461417)\n[Disboard](https://disboard.org/server/798268275167461417)\n[Discord.me](https://discord.me/everyone)')
  embed.set_footer(text='Please rate 5 star or upvote if you enjoy :)')
  embed.set_author(name="The Chat Cloud", icon_url=ctx.guild.icon_url)
  await ctx.reply(embed=embed)

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')
@client.command()
async def poll(ctx,*,message):
  emb=discord.Embed(title=f"Poll by {ctx.author.name}", description=f'{message}')
  msg=await ctx.reply(embed=emb)
   
  await msg.add_reaction('👍')
  await msg.add_reaction('👎')
@client.command()
async def cat(ctx):
            response = requests.get('https://aws.random.cat/meow')
            data = response.json()
            await ctx.reply(data['file'])
@client.command()
async def dadjoke(ctx):
     
        api = 'https://icanhazdadjoke.com/'
        async with aiohttp.request('GET', api, headers={'Accept': 'text/plain'}) as r:
            result = await r.text()
            await ctx.reply(result)
@client.command()
async def meme(ctx):
            response = requests.get('https://meme-api.herokuapp.com/gimme')
            data = response.json()
            await ctx.reply(data['url'])
@client.command()
async def uptime(ctx):
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        embed = discord.Embed(colour=ctx.message.author.top_role.colour)
        embed.add_field(name="Uptime", value=text)
        
        try:
            await ctx.reply(embed=embed)
         
        except discord.HTTPException:
            await ctx.reply("Current uptime: " + text)
@client.command()
async def members(ctx):
  mbed = discord.Embed(
    color=discord.Color(0xffff),
    title=f'{ctx.guild.name}'
  )
  
  mbed.add_field(name='Member Count', value=f'{ctx.guild.member_count}')
  
  await ctx.reply(embed=mbed)

keep_alive()
client.run(token)
