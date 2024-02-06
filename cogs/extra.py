import discord,time
from discord.ext import commands
class extra(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    #Sync commands.
    @commands.command(name="sync")
    async def sync(self,ctx):
        try:
            fmt = await self.bot.tree.sync() #syncs bot tree when !sync is used
            await ctx.send(f"Synced {len(fmt)} command(s) to the current server")
        except Exception as e:
            await ctx.send(f"Error while syncing commands: {e}")
            return
    @commands.Cog.listener()
    async def on_member_join(self,member: discord.member):
        channel = await self.bot.fetch_channel("channel")
        guild = self.bot.get_guild("guild")
        role = guild.get_role("role")
        await channel.send(f'{member.mention} has joined the server! welcome, make sure to read rules!')
        await member.add_roles(role)
async def setup(bot):
    await bot.add_cog(extra(bot))