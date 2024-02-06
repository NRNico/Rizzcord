import discord,datetime,time
from discord.ext import commands
 #function to check if member is muted
def check_timeout(member):
    if member.timed_out_until is not None:
        return True
    else:
        return False  
#Check if a user is banned
async def is_banned(guild,user):
    try:
        print("checking if user is banned")
        entry = await guild.fetch_ban(user)#checks if user is banned and returns false if not, and true if they are.
    except discord.NotFound:
        return False
    return True
#Get the guild ID from a message.
def getguildid(ctx):
    return ctx.guild.id#returns the guild ID to the commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #ban code
        
    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self,ctx, userid:int, *, reason=None):
        member = await self.bot.fetch_user(userid)  # fetches members user from userid
        if not member.bot:
            if member.name != ctx.message.author.name:
                if await is_banned(ctx.guild,member)==False: #check if member is already banned
                    await ctx.send(f'{member.mention} was banned. Reason: {reason}')
                    await member.send(f'You were banned from {ctx.guild.name}. Reason {reason}')
                    await ctx.guild.ban(member,reason=reason, delete_message_days=0)
                else:
                    await ctx.send("Unable to ban as user is banned.")
            else:
                await ctx.send("Unable to ban yourself.")
        else:
            await ctx.send("Unable to ban bot.")
    #unban code
        
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self,ctx, userid:int, *,reason=None):
        member = await self.bot.fetch_user(userid)#fetches members user from userid
        if not member.bot:
            if member.name != ctx.message.author.name:
                if await is_banned(ctx.guild,member): #check if member is already banned
                    await ctx.guild.unban(member,reason = reason)#unbans member
                    await ctx.send(f'{member.mention} was Unbanned')
                else:
                    await ctx.send("Unable to unban as user isnt banned.")
            else:
                await ctx.send("Unable to unban yourself.")
        else:
            await ctx.send("Unable to unban bot.")
    #kick code
        
    @commands.command()
    @commands.has_permissions(kick_members=True)        
    async def kick(self,ctx,userid:int, *, reason=None):
        invite = await ctx.channel.create_invite(max_age=10000)
        try:
            guild = await self.bot.fetch_guild(getguildid(ctx))#tries to call get guild id, and if fails errors.
        except Exception as e:
            print(f"Error: {e}")
        if ctx.guild.get_member(userid):
            member = ctx.guild.get_member(userid)
            if not member.bot:
                if member.name != ctx.message.author.name:
                    await member.send(f'You have been kicked from {ctx.guild.name} for {reason}. Join back {invite}.')
                    await member.kick(reason=reason)
                    await ctx.send(f'{member.mention} has been kicked successfully.')
                else:
                    await ctx.send("You can't kick yourself silly!")
            else:
                await ctx.send("Unable to kick, user is a bot.")
        else:
            await ctx.send("User is not in guild, unable to kick.")
    #mute code
        
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def mute(self,ctx,userid:str, duration:str, *, reason= None):
        duration_dict = {"d": 24*60*60, "h": 60*60}
        unit = duration[-1]
        value = int(duration[:-1])
        seconds = value * duration_dict[unit]
        try:
            guild = await self.bot.fetch_guild(getguildid(ctx))#tries to call get guild id, and if fails errors.
        except Exception as e:
            print(f"Error: {e}")
        if ctx.guild.get_member(int(userid)):
            member = ctx.guild.get_member(int(userid))
            check= check_timeout(member)
            if not member.bot:
                if check==False:
                    if member.name != ctx.message.author.name:
                        print(member,type(member))
                        await member.send(f'You were muted in {guild.name} for {duration} hours. Reason {reason}.')
                        await ctx.send(f'{member.mention} was muted for {duration}. Reason: {reason}')
                        timeout = datetime.timedelta(seconds=seconds)
                        await member.timeout(timeout)
                    else:
                        await ctx.send("Error: Cannot mute self.")
                else:
                    await ctx.send("Error: User is already muted.")
            else:
                await ctx.send("Error: Unable to mute bot")
        else:
            await ctx.send("User isnt in guild.")
    #unmute code
        
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unmute(self,ctx,userid, *, reason=None):
        try:
            guild = await self.bot.fetch_guild(getguildid(ctx))#tries to call get guild id, and if fails errors.
        except Exception as e:
            print(f"Error: {e}")
        if ctx.guild.get_member(int(userid)):
            member = ctx.guild.get_member(int(userid))
            if not member.bot:
                check = check_timeout(member)
                if check is not None:
                    if member.name != ctx.message.author.name:
                        await member.send(f'You were unmuted in {guild.name}. Reason {reason}.')
                        await ctx.send(f'{member.mention} was unmuted. Reason: {reason}')
                        await member.timeout(None)
                    else:
                        await ctx.send("Error: Cannot mute self.")
                else:
                    await ctx.send("Error: User is not muted.")
            else:
                await ctx.send("Error: Unable to mute bot.")
        else:
            await ctx.send("Error: User is not in this guild.")
async def setup(bot):
    await bot.add_cog(Moderation(bot))
