import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "ElizaAssistant")
ALIVE_NAME = getenv("ALIVE_NAME", "Eliza")
BOT_USERNAME = getenv("BOT_USERNAME", "MrsElizaRobot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "ElizaAssistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "ElizaSupporters")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Updates_of_ElizaBot")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/3c6f4d1d2e8f45ecdbbca.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/PereraSehath/AnnieMusicNew")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/3c6f4d1d2e8f45ecdbbca.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/e2a7a0d47771df86853af.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/29af938b00b22c52c6ed8.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/df2bc263ee00c486d7555.jpg")
