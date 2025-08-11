"""
commands.py
Một Cog chứa các lệnh cơ bản (hello, info, serverinfo, about, noiquy, tool, invite, payment)
Mô tả help đã được làm cute để khớp với help.py
"""

import discord
from discord.ext import commands
import random
import datetime
import platform
import logging

logger = logging.getLogger(__name__)


class CoreCommands(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        if not hasattr(self.bot, "start_time"):
            self.bot.start_time = datetime.datetime.utcnow()

    # --- Lệnh chào ---
    @commands.command(name="hello", help="🌸 Gửi lời chào ngọt ngào từ bot")
    async def hello(self, ctx: commands.Context):
        greetings = [
            f"Xin chào {ctx.author.mention}! 👋",
            f"Chào bạn, {ctx.author.display_name}! 😊",
            f"Rất vui được gặp bạn, {ctx.author.mention}! 🎉",
            f"Hey {ctx.author.display_name}! Hôm nay thế nào? 😄"
        ]
        await ctx.send(random.choice(greetings))

    # --- Lệnh thông tin bot ---
    @commands.command(name="info", help="💫 Hiển thị mọi thông tin về bot")
    async def info(self, ctx: commands.Context):
        bot_user = self.bot.user
        guild_count = len(self.bot.guilds)
        member_count = sum(g.member_count for g in self.bot.guilds)
        embed = discord.Embed(title="🤖 Thông tin Bot",
                              color=discord.Color.blue(),
                              timestamp=datetime.datetime.utcnow())
        avatar_url = bot_user.avatar.url if getattr(
            bot_user, "avatar", None) else getattr(bot_user, "default_avatar",
                                                   None).url
        embed.set_thumbnail(url=avatar_url)
        embed.add_field(name="Tên bot", value=bot_user.name, inline=True)
        embed.add_field(name="ID bot", value=bot_user.id, inline=True)
        embed.add_field(name="Số server", value=guild_count, inline=True)
        embed.add_field(name="Tổng thành viên",
                        value=member_count,
                        inline=True)
        embed.add_field(name="Phiên bản Python",
                        value=platform.python_version(),
                        inline=True)
        embed.add_field(name="Phiên bản Discord.py",
                        value=discord.__version__,
                        inline=True)
        if hasattr(self.bot, "start_time"):
            uptime = datetime.datetime.utcnow() - self.bot.start_time
            embed.add_field(name="Thời gian hoạt động",
                            value=str(uptime).split(".")[0],
                            inline=True)
        embed.set_footer(text=f"Yêu cầu bởi {ctx.author.display_name}")
        await ctx.send(embed=embed)

    # --- Lệnh thông tin server ---
    @commands.command(name="serverinfo", help="🏰 Hiển thị thông tin server")
    async def serverinfo(self, ctx: commands.Context):
        guild = ctx.guild
        if not guild:
            return await ctx.send("❌ Lệnh này chỉ dùng được trong server!")
        embed = discord.Embed(title=f"📊 {guild.name}",
                              color=discord.Color.green(),
                              timestamp=datetime.datetime.utcnow())
        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)
        embed.add_field(name="ID Server", value=guild.id, inline=True)
        embed.add_field(
            name="Chủ server",
            value=guild.owner.mention if guild.owner else "Không rõ",
            inline=True)
        embed.add_field(name="Thành viên",
                        value=guild.member_count,
                        inline=True)
        embed.add_field(name="Kênh văn bản",
                        value=len(guild.text_channels),
                        inline=True)
        embed.add_field(name="Kênh thoại",
                        value=len(guild.voice_channels),
                        inline=True)
        embed.add_field(name="Số role", value=len(guild.roles), inline=True)
        embed.add_field(name="Ngày tạo",
                        value=guild.created_at.strftime("%d/%m/%Y"),
                        inline=True)
        embed.add_field(name="Mức xác minh",
                        value=str(guild.verification_level).title(),
                        inline=True)
        if guild.description:
            embed.add_field(name="Mô tả",
                            value=guild.description,
                            inline=False)
        embed.set_footer(text=f"Yêu cầu bởi {ctx.author.display_name}")
        await ctx.send(embed=embed)

    # --- Lệnh giới thiệu bot ---
    @commands.command(name="about", help="📜 Giới thiệu về bot đáng iu này")
    async def about(self, ctx: commands.Context):
        embed = discord.Embed(
            title="🤖 Giới thiệu Bot",
            description="Một bot Discord đơn giản với các chức năng cơ bản!",
            color=discord.Color.blue())
        embed.add_field(
            name="Chức năng",
            value=
            "• Xử lý lệnh cơ bản\n• Phản hồi tin nhắn\n• Hiển thị thông tin server",
            inline=False)
        embed.add_field(name="Lệnh",
                        value="Dùng `!help` để xem tất cả các lệnh",
                        inline=False)
        embed.add_field(name="Công nghệ",
                        value="Python 3.8+ với thư viện discord.py",
                        inline=False)
        await ctx.send(embed=embed)

    # --- Nội quy server ---
    @commands.command(name="noiquy", help="📋 Xem nội quy server")
    async def noiquy(self, ctx: commands.Context):
        if not ctx.guild:
            return await ctx.send("❌ Lệnh này chỉ dùng được trong server!")
        embed = discord.Embed(title="🌸🌟 ︵‿︵‿︵‿︵‿︵‿︵ 🌟🌸",
                              description="🎀 **𝗡𝗢̣̂𝗜 𝗤𝗨𝗬** 🎀",
                              color=0xFFC0CB)
        embed.add_field(name="\u200b", value="🌸🌟 ︵‿︵‿︵‿︵‿︵‿︵ 🌟🌸", inline=False)
        embed.add_field(
            name="1️⃣ 🐰🤝 Tôn trọng là chìa khóa",
            value=
            "Hãy đối xử tử tế và lịch sự với mọi người.\nKhông toxic, không cà khịa quá đà.\nNếu không chắc → Đừng nói!",
            inline=False)
        embed.add_field(
            name="🔟 🌟🎉 Vui vẻ, hòa đồng",
            value=
            f"Hãy tạo bầu không khí thoải mái.\n**{ctx.guild.name}** là nhà của tất cả chúng ta!",
            inline=False)
        await ctx.send(embed=embed)

    # --- Hướng dẫn tải tool ---
    @commands.command(name="tool",
                      help="🖱 Hướng dẫn tải 'Tuân Auto Click Tool'")
    async def tool(self, ctx: commands.Context):
        await self._send_tutorial_embed(ctx)

    async def _send_tutorial_embed(self, ctx: commands.Context):
        embed = discord.Embed(
            title="➡️ Hướng dẫn tải Tuân Auto Click Tool 🐰",
            description=
            "✨ Dưới đây là hướng dẫn chi tiết giúp bạn tải và sử dụng tool nhé! ✨",
            color=0xFFC0CB)
        embed.add_field(
            name="📥 Tải AutoHotkey v2",
            value=
            "🔗 [Microsoft Store](https://apps.microsoft.com/detail/9plqfdg8hh9n?hl=vi-VN&gl=VN)\n🔗 [Trang chính thức AutoHotkey](https://www.autohotkey.com/v2/)",
            inline=False)
        embed.add_field(
            name="📥 Tải script tool",
            value=
            "💾 [Link tải Tuân Auto Click Tool](https://drive.google.com/file/d/1xMsBTgbioaRbZLtwSPkqrek_C5ogWO7L/view?usp=sharing) 🥳",
            inline=False)
        embed.set_footer(text="🐰 Chúc bạn dùng tool vui vẻ, hiệu quả nhé! ❤️")
        await ctx.send(embed=embed)

    @commands.command(name="tool1",
                      help="🖱 Hướng dẫn tải 'Tuân Auto Click Tool v1'")
    async def tool1(self, ctx: commands.Context):
        await self._send_tutorial_embed(ctx)

    async def _send_tutorial_embed(self, ctx: commands.Context):
        embed = discord.Embed(
            title="➡️ Hướng dẫn tải Tuân Auto Click Tool v1 🐰",
            description=
            "✨ Dưới đây là hướng dẫn chi tiết giúp bạn tải và sử dụng tool nhé! ✨",
            color=0xFFC0CB)
        embed.add_field(
            name="📥 Tải AutoHotkey v2",
            value=
            "🔗 [Microsoft Store](https://apps.microsoft.com/detail/9plqfdg8hh9n?hl=vi-VN&gl=VN)\n🔗 [Trang chính thức AutoHotkey](https://www.autohotkey.com/v2/)",
            inline=False)
        embed.add_field(
            name="📥 Tải script tool",
            value=
            "💾 [Link tải Tuân Auto Click Tool v1](https://drive.google.com/file/d/1SyHawrJM9bZlyZnMTCnIJnpYI6cQY5UE/view?usp=drive_link) 🥳",
            inline=False)
        embed.set_footer(text="🐰 Chúc bạn dùng tool vui vẻ, hiệu quả nhé! ❤️")
        await ctx.send(embed=embed)

    # --- Dịch vụ Web Design ---
    @commands.command(name="webdesign",
                      help="🌐 Quảng bá dịch vụ thiết kế website của bạn")
    async def webdesign(self, ctx: commands.Context):
        embed = discord.Embed(
            title="🌐 Thiết Kế Website Chuyên Nghiệp",
            description=
            ("<a:prettyarrowr:1403366231192502383> **Bạn cần một website ấn tượng, chuẩn SEO, tối ưu trải nghiệm người dùng?**\n"
             "<a:animatedarrowred:1403366364307001394> Thiết kế **theo yêu cầu**, hỗ trợ đa nền tảng (PC, mobile, tablet)\n"
             "<a:animatedarrowpink:1403366313002405980> Đa dạng cho mọi người\n"
             "<a:arrowgreen:1403713757670150144> Bảo mật cao, dễ quản lý\n\n"
             "> 🎁 **Ưu đãi tháng này**\n"
             "> 📅 Thời gian hoàn thiện: 3-7 ngày\n\n"
             "💬 Liên hệ ngay: [**Click đây để chat**](https://cdn.discordapp.com/attachments/758312868936155167/1403716702541316196/image.png)"
             ),
            color=0x00bfff)
        # Avatar làm thumbnail
        embed.set_thumbnail(
            url=
            "https://cdn.discordapp.com/attachments/758312868936155167/1403715405729501215/f7bff6e8-279b-4b16-808e-e0cad4497d8d.png"
        )
        # Banner làm ảnh lớn
        embed.set_image(
            url=
            "https://cdn.discordapp.com/attachments/758312868936155167/1403715405381636228/A_futuristic_neon_galaxy_banner_with_a_glowing_planet_at_the_center_surrounded_by_colorful_stars_and_cosmic_dust_with_a_glowing_purple-pink-ring._Include_the_text__TUAN_VERSE__in_bold_cyan_neon_letters._Add_a_Disc.jpg"
        )
        embed.set_footer(
            text=f"Dịch vụ bởi {ctx.author.display_name}",
            icon_url=
            "https://cdn.discordapp.com/attachments/758312868936155167/1403715405729501215/f7bff6e8-279b-4b16-808e-e0cad4497d8d.png"
        )
        embed.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=embed)

    # --- Link mời ---
    @commands.command(name="invite",
                      help="🔗 Lấy link mời tham gia server xinh đẹp")
    async def invite(self, ctx: commands.Context):
        server_name = ctx.guild.name if ctx.guild else "server của chúng tôi"
        embed = discord.Embed(
            title=f"🎉 Mời bạn tham gia {server_name}! 🎉",
            description=
            "Click vào nút bên dưới để tham gia cùng mọi người nhé! 💖",
            color=0xFF69B4)
        embed.set_thumbnail(
            url=
            "https://drive.google.com/uc?id=13I_Dzya77omYyjEOwdyXB9CumEF-hh29")
        embed.add_field(name="🔗 Link mời:",
                        value="https://discord.gg/q8JpN6phuR",
                        inline=False)
        embed.set_footer(text="Chúng tôi rất mong gặp bạn! 🐰🌸")
        await ctx.send(embed=embed)

    @commands.command(name="mousetool",
                      help="🖱️ Thông tin và link tải Mouse Tool đo DPI")
    async def mousetool(self, ctx: commands.Context):
        embed = discord.Embed(
            title="🖱️ Mouse Tool đo DPI cho chuột \"văn phòng\" đã ra mắt",
            description=
            ("<a:prettyarrowr:1403366231192502383> **Tính năng:**\n"
             "<a:animatedarrowpink:1403366313002405980> Chỉnh và đo DPI dựa trên tốc độ chuột của Windows"
             ),
            color=0x00FFAA)

        # Nút tải
        view = discord.ui.View()
        view.add_item(
            discord.ui.Button(
                label="📥 Tải bản Portable",
                url=
                "https://drive.google.com/file/d/1v06Ig9mDRp43eKYyCcnW1u-i2mTy48NR/view?usp=drive_link"
            ))

        await ctx.send(embed=embed, view=view)

    # --- Thông tin thanh toán ---
    @commands.command(name="payment", help="💳 Xem thông tin thanh toán")
    async def payment(self, ctx: commands.Context):
        embed = discord.Embed(
            title="💳 Thông tin thanh toán",
            description="Quét mã QR dưới đây để thanh toán nhanh chóng!",
            color=0x1abc9c)
        embed.add_field(name="👤 Họ tên",
                        value="Nguyễn Thành Tuân",
                        inline=False)
        embed.add_field(name="🏦 Ngân hàng", value="TP Bank", inline=True)
        embed.add_field(name="💳 Số tài khoản",
                        value="55883610302",
                        inline=True)
        embed.set_image(
            url=
            "https://cdn.discordapp.com/attachments/758312868936155167/1403374500548186122/image.png"
        )
        await ctx.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(CoreCommands(bot))
