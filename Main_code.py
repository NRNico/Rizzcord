#import all needed libraries
import discord,os
from discord.ext import commands

# Importing tracemalloc module
import tracemalloc

# Enabling tracemalloc to track memory allocations
tracemalloc.start()
# Creating a list of numbers
numbers = [i for i in range(1000000)]
# Printing the current memory usage
print(tracemalloc.get_traced_memory())
# Stopping tracemalloc and freeing memory
tracemalloc.stop()

#create command prefix and set intents
intents = discord.Intents.default()
intents.members = True
intents.message_content=True
bot = commands.Bot(command_prefix="!",intents=intents)

#Check for errors when commands are used.
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error,  commands.MissingRequiredArgument): #sends a error message when a command used is missing a argument
        await ctx.send("missing argument.")
    if isinstance(error, commands.MissingPermissions): #sends a error message when a member doesnt have permission to use a command.
        await ctx.send("missing perms")

@bot.command()
async def reload(ctx,*,cogname:str):
    try:
        await bot.reload_extension(f"cogs.{cogname}")  # Load the file as an extension
        await ctx.send("Cog reloaded successfully.")
    except commands.ExtensionNotLoaded:
        await ctx.send("Unable to reload unloaded cog.")
    except commands.ExtensionNotFound:
        await ctx.send("Invalid cog name.\n list of current names: fun, mod, extra, logs")
@bot.command()
async def load(ctx,*,cogname:str):
    try:
        await bot.load_extension(f"cogs.{cogname}")  # Load the file as an extension
        await ctx.send("Cog loaded successfully.")
    except commands.ExtensionAlreadyLoaded:
        await ctx.send("Cog is already loaded.")
    except commands.ExtensionNotFound:
        await ctx.send("Invalid cog name.\n list of current names: fun, mod, extra, logs")
@bot.command()
async def unload(ctx,*,cogname:str):
    try:
        await bot.unload_extension(f"cogs.{cogname}")  # Load the file as an extension
        await ctx.send("Cog unloaded successfully.")
    except commands.ExtensionNotLoaded:
        await ctx.send("Cog is not loaded.")
    except commands.ExtensionNotFound:
        await ctx.send("Invalid cog name.\n list of current names: fun, mod, extra, logs")
@bot.event
async def on_ready():
  print("Bot is running")
  for cog in os.listdir(r"cogs"): # Loop through each file in your "cogs" directory.
      if cog.endswith(".py"):
          try:
            cog = f"cogs.{cog.replace('.py', '')}"
            await bot.load_extension(cog) # Load the file as an extension.
          except Exception as e:
              print(f"{cog} has failed to load:")
              raise e
  print(f"Logged in as {bot.user}")

bot.run("token")