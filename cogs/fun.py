#Import MP from MPmath and get 1k digits of pi
from mpmath import mp
mp.dps = 1000
# Get pi as a string
pi_str = str(mp.pi)
# Remove the first digit
pi_str = pi_str[2:]
#All the lines for !rizzme command
slaps = ["with a big fish","with a nokia","","with a spiky cactus","with a dog","with a piece of air, Dafuq?"]     
rizzes =["Can I be your snowflake? I promise to never melt away from your heart.","Are you French? Because Eiffel for you.","Are you a Wi-Fi signal? Because I’m feeling a strong connection.","No pen, no paper…but, you still draw my attention.",
"Are you a heart? Because I’d never stop beating for you.",
"I believe in following my dreams, so you lead the way.",
"If being beautiful was a crime, you’d be on the most wanted list.",
"Kissing is a love language. Want to start a conversation with me?",
"Are you iron? Because I don’t get enough of you.",
"Should we get coffee? Cause I like you a latte.",
"You should be Jasmine without the ‘Jas’.",
"Are you a Disney ride? Because I’d wait forever for you.",
"Are you water? Because I’d die without you.",
"I see you like tequila. Does that mean you’ll give me a shot?",
"Hey, I’m sorry to bother you, but my phone must be broken because it doesn’t seem to have your number in it.",
"Are you a boxer? Because you’re a total knockout.",
"Are you public speaking? Because you make me really nervous.",
"Are you good at math? Me neither, the only number I care about is yours.",
"I’m not religious, but you’re the answer to all of my prayers.",
"Is your name Elsa? Because I can’t let you go.",
"Do you know the difference between history and you? History is the past and you are my future.",
"Can I follow you home? My heart seems to have taken a detour since I met you.",
"Are you April 1st? Because I’m a fool for you.",
"Are you the Krabby Patty formula? Because I’m trying to steal you.",
"Is your name Chamomile? Because you’re a hot-tea!",
"Are you legos? Because I’d never lego of you",
"Do you work for NASA? Because your beauty is out of this world."]

import discord,random,requests,json,time
from discord.ext import commands
class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    #rizz command

    @commands.command()
    async def rizzme(self,ctx):
        rizz = random.choice(rizzes)
        await ctx.send(rizz)
    #command to get ping of self.bot.
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f"Pong: {round(self.bot.latency * 1000)}ms")
    #Slap command
    @commands.command()
    async def slap(self,ctx, *, user :discord.Member= None):
        await ctx.message.delete()
        if type(user) == discord.Member:
            await ctx.send(f'{ctx.message.author.mention} has slapped {user.mention} {random.choice(slaps)}')
        else:
            await ctx.send(f'{ctx.message.author.mention} got slapped {random.choice(slaps)}')
    #Kiss command.
    @commands.command()
    async def kiss(self,ctx, *,user : discord.Member=None):
        await ctx.message.delete()
        if type(user) == discord.Member:
            await ctx.send(f'{ctx.message.author.mention} kissed {user.mention}, What a simp...')
        else:
            await ctx.send(f'{ctx.message.author.mention} has kissed the mirror, loneliness hits.')
            time.sleep(.5)
    #Pi game, player guesses pi to 1k digits.
    @commands.command()
    async def pi(self,ctx):
        number = 1
        await ctx.send("You have started the 'Pi guessing game', your goal it to get as far as you can listing the correct digits of pi!\n I'll start, 3 point.")
        for digits in pi_str:
            guess = await self.bot.wait_for("message", check=lambda message: message.author == ctx.author,timeout= 30)
            print(guess.content,digits)
            if guess.content == digits:
                print(1)
                number += 1
                await ctx.send("Correct! Next digit?")
            else:
                print(1)
                await ctx.send(f"Whoops... You got it wrong. Your score was {number}.")
                break
    @commands.command()
    async def burger(self,ctx,*,Search:str=None):
        tenor_key="key"
        apikey = tenor_key # replace with your own API key
        lmt = 10 # number of GIFs to return
        # get the anonymous user ID from Tenor
        r = requests.get("https://tenor.googleapis.com/v2/anonid?key=%s" % apikey)
        if r.status_code == 200:
            anon_id = json.loads(r.content)["anon_id"]
        else:
            anon_id = ""
        # set the search term
        search_term = f'burger {Search}'
        media_filter="gif"
        # get the top 8 GIFs for the search term
        r = requests.get(
            "https://tenor.googleapis.com/v2/search?q=%s&key=%s&limit=%s&anon_id=%s&media_filter=%s" % (search_term, apikey, lmt, anon_id,media_filter))
        print(r.status_code)
        ball = json.loads(r.content)
        if r.status_code == 200:
            top_8gifs=ball
        else:
            top_8gifs = None
        results=top_8gifs["results"]
        image_links=[]
        for result in results: # loop through the list of results
            media = result["media_formats"] # get the list of media objects
            gif_url = media['gif']['url']
            image_links.append(gif_url)
        await ctx.send(f'{random.choice(image_links)}')
    @commands.command()
    async def pizza(self,ctx,*,Search:str=None):
        tenor_key="key"
        apikey = tenor_key # replace with your own API key
        lmt = 10 # number of GIFs to return
        # get the anonymous user ID from Tenor
        r = requests.get("https://tenor.googleapis.com/v2/anonid?key=%s" % apikey)
        if r.status_code == 200:
            anon_id = json.loads(r.content)["anon_id"]
        else:
            anon_id = ""
        # set the search term
        search_term = f'pizza {Search}'
        media_filter="gif"
        # get the top 8 GIFs for the search term
        r = requests.get(
            "https://tenor.googleapis.com/v2/search?q=%s&key=%s&limit=%s&anon_id=%s&media_filter=%s" % (search_term, apikey, lmt, anon_id,media_filter))
        print(r.status_code)
        ball = json.loads(r.content)
        if r.status_code == 200:
            top_8gifs=ball
        else:
            top_8gifs = None
        results=top_8gifs["results"]
        image_links=[]
        for result in results: # loop through the list of results
            media = result["media_formats"] # get the list of media objects
            gif_url = media['gif']['url']
            image_links.append(gif_url)
        await ctx.send(f'{random.choice(image_links)}')
async def setup(bot):
    await bot.add_cog(fun(bot))