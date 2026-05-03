import re
import os
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

# Load environment variables from .env file
load_dotenv()

# ── Core bot config ────────────────────────────────────────────────────────────
API_ID = int(getenv("API_ID",38677857))
API_HASH = getenv("API_HASH", "064dccd80fc2634c2fefea331df82bb0")
BOT_TOKEN = getenv("BOT_TOKEN")

OWNER_ID = int(getenv("OWNER_ID", 1329546526))
OWNER_USERNAME = getenv("OWNER_USERNAME", "Syntaxpy")
BOT_USERNAME = getenv("BOT_USERNAME", "culsorbot")
BOT_NAME = getenv("BOT_NAME", "culsor")
ASSUSERNAME = getenv("ASSUSERNAME", "Ruhaan_II")

# ── Database & logging ─────────────────────────────────────────────────────────
MONGO_DB_URI = getenv("MONGO_DB_URI")
LOGGER_ID = int(getenv("LOGGER_ID", -1003586614728))

# ── Limits (durations in min/sec; sizes in bytes) ──────────────────────────────
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 300000))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "1200000"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "1800"))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "157286400"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1288490189999"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "3000000"))

# ── External APIs ──────────────────────────────────────────────────────────────
COOKIE_URL = getenv("COOKIE_URL")                              # required (paste link)
DEEP_API = getenv("DEEP_API")                                  # optional
API_URL = getenv("API_URL")                                    # optional
API_KEY = getenv("API_KEY", None)                              # optional

# SocialDown API Settings
SOCIALDOWN_BASE_URL = os.getenv("SOCIALDOWN_BASE_URL", "https://socialdown.itz-ashlynn.workers.dev")
SOCIALDOWN_TIMEOUT = int(os.getenv("SOCIALDOWN_TIMEOUT", "30"))

# Vars For API End Pont.
#YTPROXY_URL = getenv(https://tgapi.xbitcode.com", 'https://t.me/Syntaxpy') .
#YT_API_KEY = getenv("xbit_stMImVy7KVnx3d4goutCGhgLa76cSUai" , None ) ## Your API key like: xbit_10000000xx0233

# ── Hosting / deployment ───────────────────────────────────────────────────────
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# ── Git / updates ──────────────────────────────────────────────────────────────
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/clyxdev/VivaanXmusic4.0")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN")  # needed if repo is private

# ── Support links ──────────────────────────────────────────────────────────────
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/renderpy")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/renderpy")

# ── Assistant auto-leave ───────────────────────────────────────────────────────
AUTO_LEAVING_ASSISTANT = False
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "36000000000009"))

# ── Debug ──────────────────────────────────────────────────────────────────────
DEBUG_IGNORE_LOG = True

# ── Spotify (optional) ─────────────────────────────────────────────────────────
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "22b6125bfe224587b722d6815002db2b")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "c9c63c6fbf2f467c8bc68624851e9773")

# ── Session strings (optional) ─────────────────────────────────────────────────
STRING1 = getenv("STRING_SESSION")
STRING2 = getenv("STRING_SESSION2")
STRING3 = getenv("STRING_SESSION3")
STRING4 = getenv("STRING_SESSION4")
STRING5 = getenv("STRING_SESSION5")

# ── Anti-Edit Message Detection ────────────────────────────────────────────────
EDIT_DELETE_TIME = int(getenv("EDIT_DELETE_TIME", "60"))  # seconds before deletion
EDIT_WARNING_MESSAGE = getenv(
    "EDIT_WARNING_MESSAGE",
    "⚠️ **Edited Message Detected**\n\n"
    "Your edited message will be deleted in {time} seconds.\n\n"
    "_Editing messages is not allowed in this group._"
)

# ── Anti-Abusive Word Detection ────────────────────────────────────────────────
DEFAULT_WARNING_LIMIT = int(getenv("DEFAULT_WARNING_LIMIT", "3"))
DEFAULT_ABUSE_ACTION = getenv("DEFAULT_ABUSE_ACTION", "delete_only")  # mute, ban, delete_only, warn_only
DEFAULT_MUTE_DURATION = int(getenv("DEFAULT_MUTE_DURATION", "1440"))  # minutes (24 hours)
ABUSE_WARNING_DELETE_TIME = int(getenv("ABUSE_WARNING_DELETE_TIME", "10"))  # seconds

# Valid abuse actions
VALID_ABUSE_ACTIONS = ["mute", "ban", "delete_only", "warn_only"]

# ── Media assets ───────────────────────────────────────────────────────────────
START_VIDS = [
    "https://files.catbox.moe/gw1y5s.mp4",
    "https://files.catbox.moe/gw1y5s.mp4",
    "https://files.catbox.moe/gw1y5s.mp4",
]
STICKERS = [
    "CAACAgUAAxkBAAEDrQVp92U9Nn-jTKa1q9YB4LQ3U4gxbgAC7BsAAlR6IFTnGrKf3wE4-zsE",
    "CAACAgUAAxkBAAEDrQpp92VUmRRwwCF7EyxbYoHchSKFoQACWBcAAugMKFRKVkcAAfwAAVyVOwQ",
]
HELP_IMG_URL = "https://files.catbox.moe/keb4um.jpg"
PING_VID_URL = "https://files.catbox.moe/gw1y5s.mp4"
PLAYLIST_IMG_URL = "https://files.catbox.moe/u79q4y.jpg"
STATS_VID_URL = "https://files.catbox.moe/gw1y5s.mp4"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/keb4um.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/keb4um.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/keb4um.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/keb4um.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/keb4um.jpg"
SPOTIFY_ARTIST_IMG_URL = SPOTIFY_ALBUM_IMG_URL = SPOTIFY_PLAYLIST_IMG_URL = YOUTUBE_IMG_URL

# ── Helpers ────────────────────────────────────────────────────────────────────
def time_to_seconds(time: str) -> int:
    return sum(int(x) * 60**i for i, x in enumerate(reversed(time.split(":"))))

DURATION_LIMIT = time_to_seconds(f"{DURATION_LIMIT_MIN}:00")

# ───── Bot Introduction Messages ───── #
AYU = ["💞", "🦋", "🔍", "🧪", "⚡️", "🔥", "🎩", "🌈", "🍷", "🥂", "🥃", "🕊️", "🪄", "💌", "🧨"]
AYUV = [
    "ʜᴇʟʟᴏ {0}, 🥀\n\n ɪᴛ'ꜱ ᴍᴇ {1} !\n\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ◆ ꜱᴜᴘᴘᴏʀᴛɪɴɢ ᴘʟᴀᴛꜰᴏʀᴍꜱ : ʏᴏᴜᴛᴜʙᴇ, ꜱᴘᴏᴛɪꜰʏ,\n┠ ◆ ʀᴇꜱꜱᴏ, ᴀᴘᴘʟᴇᴍᴜꜱɪᴄ , ꜱᴏᴜɴᴅᴄʟᴏᴜᴅ ᴇᴛᴄ.\n┗━━━━━━━━━━━━━━━━━⧫\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ➥ Uᴘᴛɪᴍᴇ : {2}\n┠ ➥ SᴇʀᴠᴇʀSᴛᴏʀᴀɢᴇ : {3}\n┠ ➥ CPU Lᴏᴀᴅ : {4}\n┠ ➥ RAM Cᴏɴsᴜᴘᴛɪᴏɴ : {5}\n┠ ➥ ᴜꜱᴇʀꜱ : {6}\n┠ ➥ ᴄʜᴀᴛꜱ : {7}\n┗━━━━━━━━━━━━━━━━━⧫\n\n🫧 ᴅᴇᴠᴇʟᴏᴩᴇʀ 🪽 ➪ [𝐒𝚮𝚴𝐖𝚨𝚭‎](https://t.me/Syntaxpy)",
    "ʜɪɪ, {0} ~\n\n◆ ɪ'ᴍ ᴀ {1} ᴛᴇʟᴇɢʀᴀᴍ ꜱᴛʀᴇᴀᴍɪɴɢ ʙᴏᴛ ᴡɪᴛʜ ꜱᴏᴍᴇ ᴜꜱᴇꜰᴜʟ\n◆ ᴜʟᴛʀᴀ ғᴀsᴛ ᴠᴄ ᴘʟᴀʏᴇʀ ꜰᴇᴀᴛᴜʀᴇꜱ.\n\n✨ ꜰᴇᴀᴛᴜʀᴇꜱ ⚡️\n◆ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs.\n◆ Sᴜᴘᴇʀғᴀsᴛ ʟᴀɢ Fʀᴇᴇ ᴘʟᴀʏᴇʀ.\n◆ ʏᴏᴜ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜꜱɪᴄ + ᴠɪᴅᴇᴏ.\n◆ ʟɪᴠᴇ ꜱᴛʀᴇᴀᴍɪɴɢ.\n◆ ɴᴏ ᴘʀᴏᴍᴏ.\n◆ ʙᴇꜱᴛ ꜱᴏᴜɴᴅ Qᴜᴀʟɪᴛʏ.\n◆ 24×7 ʏᴏᴜ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜꜱɪᴄ.\n◆ ᴀᴅᴅ ᴛʜɪꜱ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴍᴀᴋᴇ ɪᴛ ᴀᴅᴍɪɴ ᴀɴᴅ ᴇɴᴊᴏʏ ᴍᴜꜱɪᴄ 🎵.\n\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ◆ ꜱᴜᴘᴘᴏʀᴛɪɴɢ ᴘʟᴀᴛꜰᴏʀᴍꜱ : ʏᴏᴜᴛᴜʙᴇ, ꜱᴘᴏᴛɪꜰʏ,\n┠ ◆ ʀᴇꜱꜱᴏ, ᴀᴘᴘʟᴇᴍᴜꜱɪᴄ , ꜱᴏᴜɴᴅᴄʟᴏᴜᴅ ᴇᴛᴄ.\n┗━━━━━━━━━━━━━━━━━⧫\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ➥ Uᴘᴛɪᴍᴇ : {2}\n┠ ➥ SᴇʀᴠᴇʀSᴛᴏʀᴀɢᴇ : {3}\n┠ ➥ CPU Lᴏᴀᴅ : {4}\n┠ ➥ RAM Cᴏɴsᴜᴘᴛɪᴏɴ : {5}\n┠ ➥ ᴜꜱᴇʀꜱ : {6}\n┠ ➥ ᴄʜᴀᴛꜱ : {7}\n┗━━━━━━━━━━━━━━━━━⧫\n\n🫧 ᴅᴇᴠᴇʟᴏᴩᴇʀ 🪽 ➪ [𝐒𝚮𝚴𝐖𝚨𝚭‎](https://t.me/Syntaxpy)",
]

# ── Runtime structures ─────────────────────────────────────────────────────────
BANNED_USERS = filters.user()
adminlist, lyrical, votemode, autoclean, confirmer = {}, {}, {}, [], {}

# ── Minimal validation ─────────────────────────────────────────────────────────
if SUPPORT_CHANNEL and not re.match(r"^https?://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - Invalid SUPPORT_CHANNEL URL. Must start with https://")

if SUPPORT_CHAT and not re.match(r"^https?://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - Invalid SUPPORT_CHAT URL. Must start with https://")

if not COOKIE_URL:
    raise SystemExit("[ERROR] - COOKIE_URL is required.")

# Only allow these cookie link formats
if not re.match(r"^https://(batbin\.me|pastebin\.com)/[A-Za-z0-9]+$", COOKIE_URL):
    raise SystemExit("[ERROR] - Invalid COOKIE_URL. Use https://batbin.me/<id> or https://pastebin.com/<id>")

# Validate abuse action
if DEFAULT_ABUSE_ACTION not in VALID_ABUSE_ACTIONS:
    raise SystemExit(f"[ERROR] - Invalid DEFAULT_ABUSE_ACTION. Must be one of: {', '.join(VALID_ABUSE_ACTIONS)}")
