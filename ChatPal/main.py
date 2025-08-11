import os
from dotenv import load_dotenv
from keep_alive import keep_alive
from bot import bot  # lấy bot từ bot.py

# Load biến môi trường từ .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN") or os.getenv("TOKEN")

if not TOKEN:
    raise ValueError(
        "❌ Chưa có token! Thêm DISCORD_TOKEN vào file .env hoặc Secrets.")

# Giữ bot hoạt động trên Replit


keep_alive()


# Chạy bot chính thức
bot.run(TOKEN)
