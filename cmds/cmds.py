import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Cmds(Cog_Extension):
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} ms')

    @commands.command()
    async def load(self, ctx, extension):
        await self.bot.load_extension(f'cmds.{extension}')
        await ctx.send(f'Loaded {extension} done.')
    
    @commands.command()
    async def unload(self, ctx, extension):
        await self.bot.unload_extension(f'cmds.{extension}')
        await ctx.send(f'Unoaded {extension} done.')

    @commands.command()
    async def reload(self, ctx, extension):
        await self.bot.reload_extension(f'cmds.{extension}')
        await ctx.send(f'Reoaded {extension} done.')

    @commands.command()
    async def limit(self, ctx):
        try:
            channel = ctx.author.voice.channel
        except:
            pass
        number = ctx.message.content[7:]
        print()
        await self.edit(channel,number)

async def setup(bot):
    await bot.add_cog(Cmds(bot))