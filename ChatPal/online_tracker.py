import discord
from discord.ext import commands, tasks


class OnlineTracker(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        # ID các channel voice/text muốn đổi tên
        self.total_members_channel_id = 1404589964959813735
        self.total_bots_channel_id = 1404592278055686165
        self.online_members_channel_id = 1404592321374191738

        self.guild_id = 1307021640026165330  # ID server
        self.role_member_id = 1403143938151415889  # ID role Member
        self.role_bot_id = 1403144924957900920  # ID role Bot

        self.update_status.start()

    def cog_unload(self):
        self.update_status.cancel()

    @tasks.loop(minutes=1)
    async def update_status(self):
        guild = self.bot.get_guild(self.guild_id)
        if guild is None:
            return

        # Tổng số thành viên
        total_members = guild.member_count

        # Số bot dựa trên role bot
        role_bot = guild.get_role(self.role_bot_id)
        if role_bot:
            bot_count = len(role_bot.members)
        else:
            bot_count = 0

        # Số thành viên role Member đang online
        role_member = guild.get_role(self.role_member_id)
        if role_member:
            online_members_with_role = sum(
                1 for m in role_member.members
                if m.status != discord.Status.offline and not m.bot)
        else:
            online_members_with_role = 0

        # Cập nhật tên các channel
        total_channel = guild.get_channel(self.total_members_channel_id)
        if total_channel:
            await total_channel.edit(name=f"👥 Thành viên: {total_members}")

        bot_channel = guild.get_channel(self.total_bots_channel_id)
        if bot_channel:
            await bot_channel.edit(name=f"🤖 Bots: {bot_count}")

        online_channel = guild.get_channel(self.online_members_channel_id)
        if online_channel:
            await online_channel.edit(
                name=f"🟢 Member online: {online_members_with_role}")

    @update_status.before_loop
    async def before_update_status(self):
        await self.bot.wait_until_ready()


async def setup(bot: commands.Bot):
    await bot.add_cog(OnlineTracker(bot))
