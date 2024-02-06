# cogs/logger.py
import discord
from discord.ext import commands

blacklisted_reactions = ["🍑", "🍆"]
class lagger(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        channel = self.bot.get_channel("Channel")
        desc = f'A message has been deleted: {message.content}. Channel of message: {message.channel.mention}. Message author: {message.author.mention}'
        embed = discord.Embed(title="Deleted message",description=desc)
        await channel.send(embed=embed)

    #Reaction logger
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        log_channel = self.bot.get_channel("Channel")
        message_id=payload.message_id
        channel = self.bot.get_channel(payload.channel_id)
        user = self.bot.get_user(payload.user_id)
        message = await channel.fetch_message(message_id)
        reaction = discord.utils.get(message.reactions, emoji=payload.emoji.name)
        if str(payload.emoji) in blacklisted_reactions:
            await log_channel.send(f"{user.mention} reacted with the {payload.emoji} emoji on the message {message.jump_url}.")
            await reaction.remove(user)

async def setup(bot):
    await bot.add_cog(lagger(bot))