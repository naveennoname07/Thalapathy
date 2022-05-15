import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = 'Media_search'
USER_SESSION = 'User_Bot'
API_ID = 12345
API_HASH = '0123456789abcdef0123456789abcdef'
BOT_TOKEN = '123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11'
USERBOT_STRING_SESSION = ''

# Bot settings
CACHE_TIME = 300
USE_CAPTION_FILTER = False

# Admins, Channels & Users
ADMINS = [12345789, 'admin123', 98765432]
CHANNELS = [-10012345678, -100987654321, 'channelusername']
AUTH_USERS = []
AUTH_CHANNEL = None

# MongoDB information
DATABASE_URI = "mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[defaultauthdb]?retryWrites=true&w=majority"
DATABASE_NAME = 'Telegram'
COLLECTION_NAME = 'channel_files'  # If you are using the same database, then use different collection name for each bot

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'mizotelegram')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "𝙁𝙞𝙡𝙚 𝙉𝙖𝙢𝙚 : <code>{file_name}</code> 𝙁𝙞𝙡𝙚 𝙎𝙞𝙯𝙚 : <i>{file_size}</i>")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>🀄𝙏𝙞𝙩𝙡𝙚 : <a href={url}>{title}</a>\n\n📆 𝙔𝙚𝙖𝙧 : <a href={url}/releaseinfo>{year}</a>\n\n☀️ 𝙇𝙖𝙣𝙜𝙨  : <code>{languages}</code>\n\n📆 𝙍𝙚𝙡𝙚𝙖𝙨𝙚 𝘿𝙖𝙩𝙚 : {release_date}\n\n🌟𝙍𝙖𝙩𝙞𝙣𝙜𝙨 : <a href={url}/ratings>{rating}</a> / 10 (based on {votes} user ratings.)\n\n📺𝙎𝙩𝙤𝙧𝙮 : <code>{plot}</code>")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "False"), False)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
