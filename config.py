## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgC8uff9iN5_XjjhbD41yUex7IgNxMzD3q-UvW1gHCEBo2Aq-zOYkcEQlD9IdlGwD19c-iwRPmD5mo91HvU-hmMopk8BQMl_NZPgXXlcMuQtzbrZPCgaEktWVHUCLC0FockN79ve_iw1ye0OAgIJNYwlhqYNPMoA6SCTVCXqwaIhcu-guHT52bf64ZTSiAcYK207e67wSLUlKYckHjJLbPWXlcWW9frBpwP09l2GBfc7GrZowrD30yeF45gZV_FgFDSYHjQZdQya-P4ZSv5qXGk9lPCCD1MVeE6PDt-C59rqw-bCXmV7CrJbPhSfQS4J_vbYuC6AY_wfaymSE7gZ5OnDAAAAAUC8SisA")
BOT_TOKEN = getenv("BOT_TOKEN", "5469255387:AAEwBO6Y3l3qVzZ2_hWv-9bI7w-xiRTqjro")
BOT_NAME = getenv("BOT_NAME", "DADDY")
API_ID = int(getenv("API_ID", "11430350"))
API_HASH = getenv("API_HASH", "eae493b15b16c07b87ed6c84d671d719")
OWNER_NAME = getenv("OWNER_NAME", "Hassan")
OWNER_USERNAME = getenv("OWNER_USERNAME", "PPF88")
ALIVE_NAME = getenv("ALIVE_NAME", "DADDY")
BOT_USERNAME = getenv("BOT_USERNAME", "Dadymusicbot")
OWNER_ID = getenv("OWNER_ID", "1891794672")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "DlIIIlIlD")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "hhhsssoff")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "evvvvs")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5383415297").split()))
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
