#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = "28031075"
API_HASH = "6a309d42eda281416f798a554360e6a8"
BOT_TOKEN = "6997680088:AAEXVoUhvAjeJsVkvay_j-jzj9z88TDF61w"
SESSION = "AQGruGMAEihcxwnpBtjDh9jLPA2v1ruxUQ6zgI-32rfSQdlTD1UeExOzA00EhURoFw6BeIv7ddNMYnbZin-jhjyiE-O95Ey2TBxS8Ozhp6vZtUwVvx5bzyOlb36-LJBszXLkqxJZENM6e4c4rxxSNfXIBfJ_nkW9PDt6r_4i79Pszom0td7XhMjnf39uPwXHMrSfRs9dAZhHvPWsr0HUvTmnF1BFbfAlgdlIIS9uglFWr4jmFcXymbCxwbe37Osc-aa_yd7snPhiJ3DuHhHjp2YrLHr55laPUbNt2Z_UxBr9AWuVdVMfkGyF95Egewmh7XvCtqzgG68BA9kxeK1nHwsXWariegAAAAFbd0h7AA"
FORCESUB = "vibrantsamundra"
AUTH = config("AUTH", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
