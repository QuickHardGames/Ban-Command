#Just the part of a  code not a code itself!!!!

@client.command(aliases=['b'])
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="Fear of spiders"):
    await member.ban(reason=reason)
    embed = discord.Embed(title="Banned!",
                          description=f"{member.mention} ate a frog and died ",
                          colour=discord.Colour.blue())
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.ban(reason=reason)
