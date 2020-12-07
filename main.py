import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix=".")

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(
        type=discord.ActivityType.watching, name=f'{len(bot.guilds)} servers | .help'
    ))
    print("Notification | Bot has been turned on!")


@bot.command(aliases=['askk'])
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
    await ctx.send(f'{random.choice(responses)}')
@bot.command(aliases=['piing'])
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')
@bot.command(aliases=['howgayy'])
async def howgay(ctx):
    responses = ['You are 1 percent gay.',
    'You are 2 percent gay.',
    'You are 3 percent gay.',
    'You are 4 percent gay.',
    'You are 5 percent gay.',
    'You are 6 percent gay.',
    'You are 7 percent gay.',
    'You are 8 percent gay.',
    'You are 9 percent gay.',
    'You are 10 percent gay.',
    'You are 11 percent gay.',
    'You are 12 percent gay.',
    'You are 13 percent gay.',
    'You are 14 percent gay.',
    'You are 15 percent gay.',
    'You are 16 percent gay.',
    'You are 17 percent gay.',
    'You are 18 percent gay.',
    'You are 19 percent gay.',
    'You are 20 percent gay.',
    'You are 21 percent gay.',
    'You are 22 percent gay.',
    'You are 23 percent gay.',
    'You are 24 percent gay.',
    'You are 25 percent gay.',
    'You are 26 percent gay.',
    'You are 27 percent gay.',
    'You are 28 percent gay.',
    'You are 29 percent gay.',
    'You are 30 percent gay.',
    'You are 31 percent gay.',
    'You are 32 percent gay.',
    'You are 33 percent gay.',
    'You are 34 percent gay.',
    'You are 35 percent gay.',
    'You are 36 percent gay.',
    'You are 37 percent gay.',
    'You are 38 percent gay.',
    'You are 39 percent gay.',
    'You are 40 percent gay.',
    'You are 41 percent gay.',
    'You are 42 percent gay.',
    'You are 43 percent gay.',
    'You are 44 percent gay.',
    'You are 45 percent gay.',
    'You are 46 percent gay.',
    'You are 47 percent gay.',
    'You are 48 percent gay.',
    'You are 49 percent gay.',
    'You are 50 percent gay.',
    'You are 51 percent gay.',
    'You are 52 percent gay.',
    'You are 53 percent gay.',
    'You are 54 percent gay.',
    'You are 55 percent gay.',
    'You are 56 percent gay.',
    'You are 57 percent gay.',
    'You are 58 percent gay.',
    'You are 59 percent gay.',
    'You are 60 percent gay.',
    'You are 61 percent gay.',
    'You are 62 percent gay.',
    'You are 63 percent gay.',
    'You are 64 percent gay.',
    'You are 65 percent gay.',
    'You are 66 percent gay.',
    'You are 67 percent gay.',
    'You are 68 percent gay.',
    'You are 69 percent gay.',
    'You are 70 percent gay.',
    'You are 71 percent gay.',
    'You are 72 percent gay.',
    'You are 73 percent gay.',
    'You are 74 percent gay.',
    'You are 75 percent gay.',
    'You are 76 percent gay.',
    'You are 77 percent gay.',
    'You are 78 percent gay.',
    'You are 79 percent gay.',
    'You are 80 percent gay.',
    'You are 81 percent gay.',
    'You are 82 percent gay.',
    'You are 83 percent gay.',
    'You are 84 percent gay.',
    'You are 85 percent gay.',
    'You are 86 percent gay.',
    'You are 87 percent gay.',
    'You are 88 percent gay.',
    'You are 89 percent gay.',
    'You are 90 percent gay.',
    'You are 91 percent gay.',
    'You are 92 percent gay.',
    'You are 93 percent gay.',
    'You are 94 percent gay.',
    'You are 95 percent gay.',
    'You are 96 percent gay.',
    'You are 97 percent gay.',
    'You are 98 percent gay.',
    'You are 99 percent gay.',
    'You are 100 percent gay.']
    mbed = discord.Embed(
        title = 'HowGay Machine',
        description = f'{random.choice(responses)}'
    )
    await ctx.send(embed=mbed)

@bot.command(aliases=['yomamma'])
async def yomama(ctx):
    responses = ['Yo mama so fat, when she fell I did not laugh, but the sidewalk cracked up.',
'Yo mama so fat when she skips a meal the stock market drops.',
'Yo mama so fat, it took me two buses and a train to get to her good side.',
'Yo mama so fat, when she goes camping, the bears hide their food.',
'Yo mama so fat, if she buys a fur coat, a whole species will become extinct.',
'Yo mama so fat, she stepped on a scale and it said: To be continued.',
'Yo mama so fat, I swerved to miss her in my car and ran out of gas.',
'Yo mama so fat, when she wears high heels, she strikes oil.',
'Yo mama so fat, she was overthrown by a small militia group, and now she is known as the Republic of Yo Mama.',
'Yo mama so fat, when she sits around the house, she SITS AROUND the house.',
'Yo mama so fat, her car has stretch marks.',
'Yo mama so fat, she can not even jump to a conclusion.',
'Yo mama so fat, her blood type is Ragu.',
'Yo mama so fat, if she was a Star Wars character, her name would be Admiral Snackbar.',
'Yo mama so stupid, she stared at a cup of orange juice for 12 hours because it said concentrate.',
'Yo mama so stupid when they said it was chilly outside, she grabbed a bowl.',
'Yo mama so stupid, she put lipstick on her forehead to make up her mind.',
'Yo mama so stupid, she thought a quarterback was a refund.',
'Yo mama so stupid, she got hit by a parked car.',
'Yo mama so stupid, when I told her that she lost her mind, she went looking for it',
'Yo mama so stupid when thieves broke into her house and stole the TV, she chased after them shouting Wait you forgot the remote!',
'Yo mama so stupid, she went to the dentist to get a Bluetooth.',
'Yo mama so stupid, she took a ruler to bed to see how long she slept.',
'Yo mama so stupid, she got locked in the grocery store and starved to death.',
'Yo mama so stupid, when I said, drinks on the house she got a ladder.',
'Yo mama so stupid, it takes her two hours to watch 60 Minutes.',
'Yo mama so stupid, she put airbags on her computer in case it crashed.',
'Yo mama so ugly, she threw a boomerang and it refused to come back.',
'Yo mama so old, her social security number is one.',
'Yo mama so ugly, she made a blind kid cry.',
'Yo mama so ugly, her portraits hang themselves.',
'Yo mama so old, she walked out of a museum and the alarm went off.',
'Yo mama teeth are so yellow when she smiles at traffic, it slows down.',
'Yo mama armpits are so hairy, it looks like she got Buckwheat in a headlock.',
'Yo mama so ugly, when she was little, she had to trick-or-treat by phone.',
'Yo mama so ugly, her birth certificate is an apology letter.',
'Yo mama so ugly, she looked out the window and was arrested for mooning.',
'Yo mama so poor, the ducks throw bread at her.',
'Yo mama so poor, she chases the garbage truck with a grocery list.',
'Yo mama cooking so nasty, she flys got together and fixed the hole in the window screen.',
'Yo mama so depressing, blues singers come to visit her when they got writer block.',
'Yo mama so short, you can see her feet on her driver license.',
'Yo mama so poor, she can not even afford to pay attention.',
'Yo mama so big, her belt size is equator.',
'Yo mama so classless, she is a Marxist utopia.',
'Yo mama so short, she went to see Santa and he told her to get back to work.',
'Yo mama so scary, the government moved Halloween to her birthday.',
'Yo mama so nasty, they used to call them jumpolines til yo mama bounced on one.',
'Yo mama teeth so yellow, I can not believe it is not butter.',
'Yo mama so poor, Nigerian princes wire her money.',
'Yo mama so dumb, she went to the eye doctor to get an iPhone.',
'Yo mama so lazy, she stuck her nose out the window and let the wind blow it.']
    await ctx.send(f'{random.choice(responses)}')
@bot.command(aliases=['e'])
async def nuke(ctx, channel: discord.TextChannel):
    mbed = discord.Embed(
        title = 'Success',
        description = f'{channel} has been nuked.',
    )
    if ctx.author.guild_permissions.manage_channels:
        await ctx.send(embed=mbed)
        await channel.delete()
@bot.command(aliases=['i'])
async def createchannel(ctx, channelName):
    guild = ctx.guild

    mbed = discord.Embed(
        title = 'Success',
        description = "{} has been successfully created.".format(channelName)

    )
    if ctx.author.guild_permissions.manage_channels:
        await guild.create_text_channel(name='{}'.format(channelName))
        await ctx.send(embed=mbed)
@bot.command(aliases=['hackk'])
async def hack(ctx):
  await ctx.send('rick rolled')
  await ctx.send('https://tenor.com/view/dance-moves-dancing-singer-groovy-gif-17029825')
@bot.command(aliases=['githubb'])
async def github(ctx):
  await ctx.send('https://github.com/Ada64/Kalowski-Bot')
@bot.command(aliases=['polll'])
async def poll(ctx,*,message):
  emb=discord.Embed(title=f"Poll by {ctx.author.name}", description=f'{message}')
  msg=await ctx.send(embed=emb)
  await msg.add_reaction('👍')
  await msg.add_reaction('👎')
@bot.command(aliases=['serverinfoo'])
async def serverinfo(ctx):
  mbed = discord.Embed(
    color=discord.Color(0xffff),
    title=f'{ctx.guild.name}'
  )
  mbed.set_thumbnail(url=f'{ctx.guild.icon_url}')
  mbed.add_field(name='Region', value=f'`{ctx.guild.region}`')
  mbed.add_field(name='Member Count', value=f'{ctx.guild.member_count}')
  mbed.set_footer(icon_url=f'{ctx.guild.icon_url}', text=f'Guild ID: {ctx.guild.id}')
  await ctx.send(embed=mbed)
@bot.command(aliases=['av'])
async def avatar(ctx, user: discord.Member):
  mbed = discord.Embed(
    color=discord.Color(0xffff),
    title=f'{user}'

    )
  mbed.set_image(url=f'{user.avatar_url}')
  await ctx.send(embed=mbed)
@bot.command(aliases=['membercount'])
async def members(ctx):
  mbed = discord.Embed(
    color=discord.Color(0xffff),
    title=f'{ctx.guild.name}'
  )
  mbed.set_thumbnail(url=f'{ctx.guild.icon_url}')
  mbed.add_field(name='Member Count', value=f'{ctx.guild.member_count}')
  mbed.set_footer(icon_url=f'{ctx.guild.icon_url}',text=f'Guild ID: {ctx.guild.id}')
  await ctx.send(embed=mbed)
@bot.command(aliases=['kickk'])
async def kick(ctx, member: discord.Member, *, reason=None):
  if ctx.author.guild_permissions.kick_members:
   await member.kick(reason=reason)
  await ctx.send(f'Kicked {member}.')
@bot.command(aliases=['bann'])
async def ban(ctx, member: discord.Member, *, reason=None):
  if ctx.author.guild_permissions.ban_members:
   await member.ban(reason=reason)
  await ctx.send(f'Banned {member}.')
@bot.command(aliases=['unbann'])
async def unban(ctx, *, member):
  banned_users = await ctx.guild.bans()
  member_name, member_discriminator = member.split('#')

  for ban_entry in banned_users:
    user = ban_entry.user

    if (user.name, user.discriminator) == (member_name, member_discriminator):
      await ctx.guild.unban(user)
      await ctx.send(f'Unbanned {user.mention}.')
      return
@bot.command(aliases=['dicerolll'])
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

bot.run("token")
