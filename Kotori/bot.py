import discord
import time
from discord.ext import commands

def get_prefix(bot, message):
    prefixes = ['K!', 'k!']
    if not message.guild:
        return 'k!', 'K!'
    return commands.when_mentioned_or(*prefixes)(bot, message)

bot = commands.Bot(command_prefix=get_prefix)
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Kotori | k!help'))
    print('Kotori is online')

# ================= Owner ================= #
@bot.command()
async def owner(ctx):
    await ctx.send(f'My owner is <@444797124656365569>')
# ================= Owner ================= #

# ================= Autorole ================= #
@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name="Kotori")
    await ctx.add_roles(member, role)
# ================= Autorole ================= #

# ================= Avatar ================= #
@bot.command()
async def avatar(ctx, member: discord.Member):
    show_avatar = discord.Embed(
        color = discord.Color.blue()
        )
    show_avatar.set_image(url='{}'.format(member.avatar_url))
    await ctx.send(embed=show_avatar)
# ================= Avatar ================= #

# ================= Ping ================= #
@bot.command(pass_context=True)
# @commands.has_permissions(manage_messages=True)
async def ping(ctx): # {0.author.mention}
    before = time.monotonic()
    message = await ctx.send("Waiting...")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"Your ping is `{int(ping)}ms`")
# ================= Ping ================= #

# ================= Say ================= #
@bot.command(pass_context=True)
async def say(ctx, *, msg):
    await ctx.send(msg)
# ================= Say ================= #

# ================= Help ================= #
@bot.command()
async def help(ctx):
    embed=discord.Embed(title="", description="Type k!Help to view the commands", color=0x3498db)
    embed.set_author(name="Kotori", icon_url="https://cdn.discordapp.com/avatars/480770098152603648/3824002b3ec43bfb7b4512c945eb97bb.webp?size=1024")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/721026081502527619/729217099678875708/download_1.jpg")
    embed.add_field(name="✨Member✨", value="Owner\nPing\nSay\nAvatar\nClear", inline=True)
    embed.add_field(name="👑Owner👑", value="Kick\nBan\nRero\nGiverole", inline=True)
    await ctx.send(embed=embed)
# ================= Help ================= #
# ✨👑💎
# ================= Music ================= #
# ================= Play/Leave ================= #
# @bot.command(pass_context=True)
# async def join(ctx):
#     channel = ctx.message.author.voice.voice_channel
#     await bot.join_voice_channel(channel)

# @bot.command(pass_context=True)
# async def disconnect(ctx):
#     server = ctx.message.server
#     voice_bot = bot.voice_bot_in(server)
#     await voice_bot.disconnect()
# ================= Play/Leave ================= #
# ================= Music ================= #

# for cog in os.listdir(".\\cogs"):
#     if cog.endswith(".py"):
#         try:
#             cog = f"cogs.{cog.replace('.py', '')}"
#             bot.load_extension(cog)
#         except Exception as e:
#             print(f"{cog} can not be loaded:")
#             raise e

bot.load_extension('cogs.mod')

bot.run('NDgwNzcwMDk4MTUyNjAzNjQ4.Xwj88A.VgMY0Krb_MGt0Ynwcj7Zb_mOgl4')