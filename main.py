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
