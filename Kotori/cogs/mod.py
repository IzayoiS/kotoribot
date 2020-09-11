import discord
from discord.ext import commands

class mod(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	def is_in_guild(guild_id):
	    async def predicate(ctx):
	        return ctx.guild and ctx.guild.id == guild_id
	    return commands.check(predicate)

# ================= Kick ================= #
	@commands.command()
	@commands.has_permissions(kick_members=True)
	@commands.is_owner()
	@is_in_guild(YOUR GUILD ID)
	async def kick(self, ctx, member: discord.Member, *, reason="No reason"):
		await member.kick(reason=reason)
		await ctx.send(f"{member.mention} Has been kick by {ctx.author.mention}. [{reason}]")

	@kick.error
	async def kick_error(self, ctx, error):
	    if isinstance(error, commands.CheckFailure):
	        await ctx.send("You don't have permission")
# ================= Kick ================= #

# ================= Ban ================= #
	@commands.command()
	@commands.has_permissions(ban_members=True)
	async def ban(self, ctx, member: discord.Member, *, reason="No reason"):
		await member.ban(reason=reason)
		await ctx.send(f"{member.mention} Has been banned by {ctx.author.mention}. [{reason}]")
# ================= Ban ================= #

# ================= Clear ================= #
	@commands.command()
	# @commands.has_permissions(manage_messages=True)
	async def clear(self, ctx, amount: int):
		await ctx.channel.purge(limit=amount + 1)
		await ctx.send(f"{amount} Message delete")

	@clear.error
	async def clear_error(self, ctx, error):
		# if isinstance(error, commands.ConversionError):
		# 	await ctx.send("Kamu siapa ya")
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send("You don't have permission")
		elif isinstance(error, commands.BadArgument):
			await ctx.send("Use a number")

		raise error
# ================= Clear ================= #

# ================= Remove Role ================= #
	@commands.command()
	@commands.has_permissions(manage_roles=True)
	@commands.is_owner()
	@is_in_guild(YOUR GUILD ID)
	async def rero(self, ctx, *,role: discord.Role):
	    if ctx.author.id == YOUR GUILD ID:
	        await role.delete()
	        await ctx.send(f'I **yeeted** {role}!')

	@rero.error
	async def rero_error(self, ctx, error):
	    if isinstance(error, commands.CheckFailure):
	        await ctx.send("You don't have permission")
# ================= Remove Role ================= #

# ================= Give Role ================= #
	@commands.command(pass_context=True)
	@commands.has_permissions(manage_roles=True)
	@commands.is_owner()
	@is_in_guild(YOUR GUILD ID)
	async def giverole(ctx, user: discord.Member, role: discord.Role):
	    await user.add_roles(role)
	    await ctx.send(f"hey {ctx.author.name}, {user.name} Success add role: {role.name}")

	@giverole.error
	async def giverole_error(self, ctx, error):
	    if isinstance(error, commands.CheckFailure):
	        await ctx.send("You don't have permission")
# ================= Give Role ================= #

def setup(bot):
	bot.add_cog(mod(bot))
