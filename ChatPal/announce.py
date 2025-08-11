"""
announce.py
Cog providing /announce (slash) and !announce (prefix) using a Modal and a button view.
"""
import discord
from discord import app_commands
from discord.ext import commands


class AnnounceModal(discord.ui.Modal, title="📢 Tạo thông báo"):

    def __init__(self, interaction: discord.Interaction):
        super().__init__()
        self.interaction_user = interaction.user
        self.interaction_channel = interaction.channel

        self.title_input = discord.ui.TextInput(
            label="Tiêu đề",
            placeholder="Nhập tiêu đề thông báo...",
            max_length=200)
        self.add_item(self.title_input)

        self.content_input = discord.ui.TextInput(
            label="Nội dung",
            style=discord.TextStyle.paragraph,
            placeholder="Nhập nội dung thông báo...",
            max_length=2000)
        self.add_item(self.content_input)

        self.image_url_input = discord.ui.TextInput(
            label="Link ảnh (tùy chọn)",
            placeholder="Nhập URL ảnh hoặc để trống",
            required=False)
        self.add_item(self.image_url_input)

        self.color_input = discord.ui.TextInput(
            label="Màu embed (HEX, ví dụ #ff0000)",
            placeholder="Mặc định là xanh lá",
            required=False)
        self.add_item(self.color_input)

    async def on_submit(self, interaction: discord.Interaction):
        try:
            color_value = self.color_input.value.strip().lstrip(
                "#") if self.color_input.value else None
            color = discord.Color(int(
                color_value, 16)) if color_value else discord.Color.green()
        except (ValueError, AttributeError):
            color = discord.Color.green()

        embed = discord.Embed(title=self.title_input.value,
                              description=self.content_input.value,
                              color=color)
        if self.image_url_input.value and self.image_url_input.value.strip(
        ).startswith("http"):
            embed.set_image(url=self.image_url_input.value.strip())
        embed.set_footer(
            text=f"Thông báo bởi {self.interaction_user.display_name}")

        try:
            await self.interaction_channel.send(embed=embed)
            await interaction.response.send_message("✅ Thông báo đã được gửi!",
                                                    ephemeral=True)
        except discord.Forbidden:
            await interaction.response.send_message(
                "❌ Bot không có quyền gửi thông báo ở kênh này.",
                ephemeral=True)


class Announce(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="announce",
                          description="Tạo thông báo với embed")
    @app_commands.checks.has_permissions(administrator=True)
    async def announce_slash(self, interaction: discord.Interaction):
        await interaction.response.send_modal(AnnounceModal(interaction))

    @commands.command(name="announce")
    @commands.has_permissions(administrator=True)
    async def announce_prefix(self, ctx: commands.Context):
        view = discord.ui.View()
        button = discord.ui.Button(label="📢 Tạo thông báo",
                                   style=discord.ButtonStyle.primary)

        async def button_callback(interaction: discord.Interaction):
            if interaction.user.id != ctx.author.id:
                await interaction.response.send_message(
                    "❌ Bạn không thể dùng nút này.", ephemeral=True)
                return
            if not interaction.user.guild_permissions.administrator:
                await interaction.response.send_message(
                    "❌ Bạn cần quyền Quản trị viên để tạo thông báo.",
                    ephemeral=True)
                return
            await interaction.response.send_modal(AnnounceModal(interaction))

        button.callback = button_callback
        view.add_item(button)

        await ctx.send(
            f"{ctx.author.mention} bấm nút bên dưới để tạo thông báo:",
            view=view)


async def setup(bot: commands.Bot):
    await bot.add_cog(Announce(bot))
