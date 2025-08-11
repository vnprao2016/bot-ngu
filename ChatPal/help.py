import discord
from discord.ext import commands


class CuteHelpCommand(commands.HelpCommand):

    def __init__(self):
        super().__init__()

    async def send_bot_help(self, mapping):
        embed = discord.Embed(
            title="🎀︱ H ư ớ n g   D ẫ n   C u t e   C ủ a   B o t 🎀",
            description="──────────────────────────────",
            color=0xFFC0CB)

        # Announce Commands
        embed.add_field(
            name="💌 Announce Commands:",
            value="📢  **announce**   ｜ Gửi thông báo dễ thương đến server",
            inline=False)

        # Core Commands
        core_cmds = [
            "📜  **about**       ｜ Giới thiệu về bot đáng iu này",
            "🌸  **hello**       ｜ Gửi lời chào ngọt ngào từ bot",
            "💫  **info**        ｜ Hiển thị mọi thông tin về bot",
            "🔗  **invite**      ｜ Lấy link mời tham gia server xinh đẹp",
            "📋  **noiquy**      ｜ Xem nội quy server",
            "💳  **payment**     ｜ Xem thông tin thanh toán",
            "🏰  **serverinfo**  ｜ Hiển thị thông tin server",
            "🖱  **tool**        ｜ Hướng dẫn tải \"Tuân Auto Click Tool\""
        ]
        embed.add_field(name="💖 Core Commands:",
                        value="\n".join(core_cmds),
                        inline=False)

        # No Category
        embed.add_field(
            name="🧸 No Category:",
            value="📚  **help**        ｜ Hiển thị menu hướng dẫn này",
            inline=False)

        # Footer
        embed.add_field(
            name="\u200b",
            value="──────────────────────────────\n"
            "💡 Gõ `!help <lệnh>` để xem chi tiết từng lệnh  \n"
            "💡 Hoặc `!help <danh mục>` để biết thêm về danh mục đó",
            inline=False)

        channel = self.get_destination()
        await channel.send(embed=embed)


async def setup(bot):
    bot.help_command = CuteHelpCommand()
