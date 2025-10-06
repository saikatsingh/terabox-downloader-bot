import os

# ---- TELEGRAM BOT ----
API_ID = 29563132  # your Telegram API ID
API_HASH = "b39be032fc0c567d0cda60dbea99606e"  # your Telegram API HASH
BOT_TOKEN = ""  # your Bot Token

# ---- REDIS DATABASE ----
HOST = "redis-12345.c1.us-east-1-2.ec2.cloud.redislabs.com"  # your Redis host
PORT = 6379  # Redis port
PASSWORD = "your_redis_password_here"  # Redis password (if any)

# ---- BOT SETTINGS ----
PRIVATE_CHAT_ID = -1002975449080  # channel/chat ID for storing videos
COOKIE = "PANWEB=1; csrfToken=abcdxyz123456;"  # Terabox cookie from browser
ADMINS = [6400371201]  # your Telegram user IDs
BOT_USERNAME = "Teraa_XXbot"
FORCE_LINK = "@RoldexVerse"  # your channel username
PUBLIC_EARN_API = "5b6f0e0aaa4ba917f40591418a55c06543e9e17f"  # optional: https://publicearn.com/api

# ---- AUTO DETECTION ----
# If you ever use Koyeb environment vars in future, this will auto override
API_ID = int(os.getenv("API_ID", API_ID))
API_HASH = os.getenv("API_HASH", API_HASH)
BOT_TOKEN = os.getenv("BOT_TOKEN", BOT_TOKEN)
HOST = os.getenv("HOST", HOST)
PORT = int(os.getenv("PORT", PORT))
PASSWORD = os.getenv("PASSWORD", PASSWORD)
PRIVATE_CHAT_ID = int(os.getenv("PRIVATE_CHAT_ID", PRIVATE_CHAT_ID))
COOKIE = os.getenv("COOKIE", COOKIE)
BOT_USERNAME = os.getenv("BOT_USERNAME", BOT_USERNAME)
FORCE_LINK = os.getenv("FORCE_LINK", FORCE_LINK)
PUBLIC_EARN_API = os.getenv("PUBLIC_EARN_API", PUBLIC_EARN_API)
