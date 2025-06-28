from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://imgur.com/a/uMcbXPy")
START_IMG = getenv("START_IMG", "https://imgur.com/a/uMcbXPy")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+fD9UDpzeWt9lMjU6")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/+fD9UDpzeWt9lMjU6")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1548566939").split()))


FAILED = "https://telegra.ph/file/a5077450218a99f2264d7.jpg"
