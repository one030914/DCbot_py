import discord
from discord.ext import commands
from core.classes import Cog_Extension

class React(Cog_Extension):
    # your react
    # @commands.command()
    # async def fun(self, arg):
    pass

async def setup(bot):
    await bot.add_cog(React(bot))