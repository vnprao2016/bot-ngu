import discord
from discord.ext import commands
import logging

logging.basicConfig(level=logging.INFO)


class MyDiscordBot(commands.Bot):

    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.guilds = True
        intents.members = True
        intents.presences = True
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        await self.load_extension("commands")
        logging.info("✅ Đã load xong Cog commands.py")
        await self.load_extension("announce")
        logging.info("✅ Đã load xong Cog announce.py")
        await self.load_extension("online_tracker")
        logging.info("✅ Đã load xong Cog online_tracker.py")
        await self.load_extension("embedtool")
        logging.info("✅ Đã load xong embedtool.py")


bot = MyDiscordBot()
