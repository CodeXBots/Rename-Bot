import os


BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
OWNER = int(os.environ.get("OWNER", ""))
BOT_USERNAME = os.environ.get('BOT_USERNAME', "")

FORCE_SUBS = os.environ.get("FORCE_SUBS", "")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))

DB_URL = os.environ.get("DB_URL", "")
DB_NAME = os.environ.get("DB_NAME", "CodeXBots")

STRING = os.environ.get("STRING", "")
BOT_PIC = os.environ.get("BOT_PIC", "https://graph.org/file/ada3f739fed7efdbe7b08.jpg")
