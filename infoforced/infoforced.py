import discord
from discord.ext import commands
from core import checks, utils
from core.models import PermissionLevel, getLogger

logger = getLogger(__name__)

class InfoForced(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["info"])
    @checks.has_permissions(PermissionLevel.REGULAR)
    @utils.trigger_typing
    async def about(self, ctx):
        embed = discord.Embed(color=self.bot.main_color, timestamp=discord.utils.utcnow())
        embed.set_author(name="Modmail - Information", icon_url=self.bot.user.display_avatar.url)
        embed.set_thumbnail(url=self.bot.user.display_avatar.url)

        desc = "This is an open source Discord bot that serves as a means for "
        desc += "members to easily receive support by administartors. "
        embed.description = desc

        embed.add_field(name="Uptime", value=self.bot.uptime)
        embed.add_field(name="Latency", value=f"{self.bot.latency * 1000:.2f} ms")
        embed.add_field(name="Version", value=f"`{self.bot.version}`")
        embed.add_field(name="Authors", value="`kyb3r`, `Taki`, `fourjr`")
        embed.add_field(name="Hosting Method", value="`UHHDANI-VPS-1`")
        embed.add_field(name="Dani's Hosting", value=f"Dani's Hosting is a service ran by <@1121435022734393429>. If you wish to have a" " Modmail/Custom bot of your own, Please contact him or join https://discord.gg/KVyCHm3Dd3 to place an order.", inline=False)
        footer = "Dani's Hosting"
        embed.set_footer(text=footer)
        await ctx.send(embed=embed)

async def setup(bot):
    res = bot.remove_command("about")
    if res is None:
        logger.error("Unable to remove `about` command.")
    await bot.add_cog(InfoForced(bot))
