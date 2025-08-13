import discord
from discord.ext import commands


class EmbedTool(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="embedtool1")
    async def send_embed(self, ctx):
        embed = discord.Embed(title="<a:pinkarrowright:1404588044522356746> UPDATE: Tuân AutoClick Tool v2",
                              description=("<a:cherryblossomspin:1404588026062962789> AutoClick không chiếm chuột\n"
                                           "<a:cherryblossomspin:1404588026062962789> AutoClick toàn màn hình\n"
                                           "<a:cherryblossomspin:1404588026062962789> AutoKey bàn phím\n\n"
                                           "Tải ngay phiên bản EXE ở dưới <a:pixelbluearrow:1404588071252398280>"),
                              color=discord.Color.green())
        embed.url = "https://drive.google.com/file/d/10xBCDVavnURPTnGcYAgNu7tnBHS19gPj/view?usp=sharing"
        embed.set_thumbnail(
            url="https://res.cloudinary.com/dvbjg6c6c/image/upload/v1754952936/cbca0f90-4008-4d6d-8b16-e9524d6a9b84_gbvyjb.png"
        )  # icon chuột
        embed.set_footer(text="Bot Ngu • AutoClick Tool v2")

        view = discord.ui.View()
        view.add_item(
            discord.ui.Button(
                label="Tải bản EXE",
                style=discord.ButtonStyle.link,
                url=
                "https://drive.google.com/file/d/10xBCDVavnURPTnGcYAgNu7tnBHS19gPj/view?usp=sharing"
            ))

        await ctx.send(embed=embed, view=view)
    @commands.command(name="ttstool")
    async def send_tts_embed(self, ctx):
        embed = discord.Embed(
            title="<a:bluearrowspin:1404588188592504883> Tool chuyển văn bản thành giọng nói đã ra mắt",
            description=(
                "<a:flowerswhite:1404588284931215410> Tuân TTS hoàn toàn FREE\n"
                "<a:flowerswhite:1404588284931215410> Hỗ trợ tải xuống hàng loạt"
            ),
            color=discord.Color.blue()
        )
        embed.url = "https://drive.google.com/file/d/1WKYk8CF6u5FpEnr2bYr2zHSK89hDKruL/view?usp=sharing"
        embed.set_thumbnail(
            url="https://res.cloudinary.com/dvbjg6c6c/image/upload/v1755086891/dea938da-7d4f-4928-8d13-974941e84e17_zrfohz.png"
        )
        embed.set_footer(text="Bot Ngu • Tuân TTS Tool")

        view = discord.ui.View()
        view.add_item(
            discord.ui.Button(
                label="Tải bản EXE",
                style=discord.ButtonStyle.link,
                url="https://drive.google.com/file/d/1WKYk8CF6u5FpEnr2bYr2zHSK89hDKruL/view?usp=sharing"
            )
        )

        await ctx.send(embed=embed, view=view)

async def setup(bot):
    await bot.add_cog(EmbedTool(bot))
