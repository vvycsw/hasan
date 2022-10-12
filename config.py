## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgCIVfMAxxD1wVnUo6Q31f_P3nP4KUBPUW7strBYewZoYT7R8Hqod_xyDKUnwGZZLkX-_8B_AW5uDLad5pt6STIPtiz4FIYo6rFoqVF-kTgxMAqRyRfCKCrzKB4kEiK3nXPl7LtJSy0FXZGaG5WDEjUolNuSZKFJ66cHonFn1i1z9-_r1pdjDta3rchthoUo0-Qd4UI0LM0TyX0m1AZ8lrBuGNFsbXvdisHvahbzpCbg7ufd1b5rfFlFwwFfOFe6jgtAjOYH4Jiyu2mY689MDxGmV_j2BSOGhxfb_nZTPgsR4E_qZjL8sCfsk8e-oZAUg-hcwMCfqY1L8GqnGsQcCScL7KfelQAAAAE-aiueAA")
BOT_TOKEN = getenv("BOT_TOKEN", "5774874510:AAEMPiWFI1m4kUOz2agDGYX2SfDi9lf-Ejw")
BOT_NAME = getenv("BOT_NAME", "DADDY")
API_ID = int(getenv("API_ID", "11430350"))
API_HASH = getenv("API_HASH", "eae493b15b16c07b87ed6c84d671d719")
OWNER_NAME = getenv("OWNER_NAME", "Hassan")
OWNER_USERNAME = getenv("OWNER_USERNAME", "PPF88")
ALIVE_NAME = getenv("ALIVE_NAME", "DADDY")
BOT_USERNAME = getenv("BOT_USERNAME", "LROBOT")
OWNER_ID = getenv("OWNER_ID", "1891794672")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "DlIIIlIlD")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "hhhsssoff")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "rr8r9)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/46fa55b49b85c084159ce.png")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/466de30ee0f9383c8e09e.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/46fa55b49b85c084159ce.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/a282c460a7f98aedbe956.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/8fe190a2a52986bd29dc5.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
