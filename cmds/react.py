import discord
from discord.ext import commands
from core.classes import Cog_Extension

class React(Cog_Extension):
    pass

async def setup(bot):
    await bot.add_cog(React(bot))