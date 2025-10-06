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
COOKIE = COOKIE = """PANWEB=1; csrfToken=OAAbrzcre1gb_6sqbXbGDY5N; browserid=tlcu6xZ6OhQJ4YfWrpmnd4Ng5tYzMDHqMY4viIbDWcHRo_gpaMGZGJsvE_4=; lang=en; __bid_n=199b9df9c67d4834c14207; __stripe_mid=d1863cd6-2188-4c56-b703-c4f9be055e9346317b; __stripe_sid=3495286b-ade1-4080-aa49-11d77e4d3c8114b589; _ga=GA1.1.1008252608.1759760603; g_state={"i_l":0}; ndus=Y4SWugxteHuifxaeWtWnMinYwRdyMaBMt389u1Kq; _rdt_uuid=1759760624696.1f9b0580-dc5a-4541-b5fb-7f8d5026b19b; _gcl_au=1.1.1640627717.1759760625; _ga_HSVH9T016H=GS2.1.s1759760624$o1$g1$t1759760644$j40$l0$h0; ndut_fmt=0B8464492CC08328EC6168CDDBD34E5BC1FD6761EC073FABA1A6BE78B1B3F696; ab_sr=1.0.1_ZWRhNjhlNzkwYzdmZjQ5ZDExYmZmZWY5YjE2NDAwNzk2ZTZhZjVhODA2N2EzZWYxMDUyNTEyNzY1YTBmMzhlMzU2MTFkMGE0ZTVhMTY3NTMzMWI2NTI2NTExNjg0ODdmYzBmODFkMDNhZjk3ZWVmNzQ5M2VmZWJkYzc5NGExNmYzNGU3NmQ5ZDhlZTdkNjc4NTNhMTVhOTkxZjg3NTI4Mw==; ab_ymg_result={"data":"d31339c4a6dd81449d8540e8efb652a7da9322b8e09fb097b18e63572b7f6ff1f79e21533e89f5c35d251b88446ead91f305dc030ee562135d1c9ac175a5a88bdf0208bfd8f0aed3d813d56b277e5a60caf24c4b012446bb7616bf002b247a6f44c38149f289630956ab201bd04b92b9a82939d26227d96dba2c151dd27992fd","key_id":"66","sign":"31cbb9c8"}; _ga_06ZNKL8C2E=GS2.1.s1759760603$o1$g1$t1759761092$j60$l0$h0"""
  # Terabox cookie from browser
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
