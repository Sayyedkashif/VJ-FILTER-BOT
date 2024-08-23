# @sayyed_kashifali Follow on social media

import os
import re
from Script import script

# Helper Functions
id_pattern = re.compile(r'^-\d+$|^\d+$')  # Pattern for numeric Telegram IDs


def is_enabled(value: str, default: bool = False) -> bool:
    return str(value).lower() in ["true", "yes", "1", "enable", "y"] or default


def get_env_list(env_name: str, default: str = ""):
    value = os.getenv(env_name, default)
    return [item.strip() for item in value.split()] if value else []


# ================== Bot Information ==================

SESSION = os.getenv('SESSION', 'Sukuna')
API_ID = int(os.getenv('API_ID', '27317700'))
API_HASH = os.getenv('API_HASH', 'de1077f45e29e6abebcd2b9dd196be1d')
BOT_TOKEN = os.getenv('BOT_TOKEN', '')

# ================== Bot Settings ==================

CACHE_TIME = int(os.getenv('CACHE_TIME', 1800))
PICS = get_env_list('PICS', 'https://telegra.ph/file/b184c91d5237856461449.jpg')
NOR_IMG = os.getenv('NOR_IMG', 'https://graph.org/file/b69af2db776e4e85d21ec.jpg')
MELCOW_VID = os.getenv('MELCOW_VID', 'https://t.me/How_To_Open_Linkl')
SPELL_IMG = os.getenv('SPELL_IMG', 'https://te.legra.ph/file/15c1ad448dfe472a5cbb8.jpg')

# =========== Admins, Channels & Users ===========

LOG_CHANNEL = int(os.getenv('LOG_CHANNEL', '-1002189558653'))

ADMINS = [int(admin) for admin in get_env_list('ADMINS', '5881638979') if id_pattern.match(admin)]
CHANNELS = [int(ch) for ch in get_env_list('CHANNELS', '-1002186277686') if id_pattern.match(ch)]
AUTH_USERS = ADMINS.copy()

# Optional Channels and Support Chats
AUTH_CHANNEL = [int(ch) for ch in get_env_list('AUTH_CHANNEL', '-1002100280219 -1002236083255 -1002158262712') if id_pattern.match(ch)]
REQST_CHANNEL = int(os.getenv('REQST_CHANNEL_ID', '0'))
SUPPORT_CHAT_ID = int(os.getenv('SUPPORT_CHAT_ID', '0'))
INDEX_REQ_CHANNEL = int(os.getenv('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in get_env_list('FILE_STORE_CHANNEL', '-1002186277686') if id_pattern.match(ch)]
DELETE_CHANNELS = [int(ch) for ch in get_env_list('DELETE_CHANNELS', '0') if id_pattern.match(ch)]

# =========== Database Configuration ===========

DATABASE_URI = os.getenv('DATABASE_URI', 'mongodb+srv://username:password@cluster0.mongodb.net/?retryWrites=true&w=majority')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'techvjautobot')
COLLECTION_NAME = os.getenv('COLLECTION_NAME', 'techvjcollection')

# =========== Premium and Referral Settings ===========

PREMIUM_AND_REFERRAL_MODE = is_enabled(os.getenv('PREMIUM_AND_REFERRAL_MODE', 'True'))
REFERAL_COUNT = int(os.getenv('REFERAL_COUNT', '20'))
REFERAL_PREMIUM_TIME = os.getenv('REFERAL_PREMIUM_TIME', '1month')
PAYMENT_QR = os.getenv('PAYMENT_QR', 'https://telegra.ph/file/77d08ff4ac61a7666deea.jpg')
PAYMENT_TEXT = os.getenv('PAYMENT_TEXT', script.PAYMENT_TEXT)
OWNER_USERNAME = os.getenv('OWNER_USERNAME', 'kingvj01')

# =========== Clone Configuration ===========

CLONE_MODE = is_enabled(os.getenv('CLONE_MODE', 'False'))
CLONE_DATABASE_URI = os.getenv('CLONE_DATABASE_URI', '')
PUBLIC_FILE_CHANNEL = os.getenv('PUBLIC_FILE_CHANNEL', '')

# =========== Links ===========

GRP_LNK = os.getenv('GRP_LNK', 'https://t.me/Notcrazyhuman')
CHNL_LNK = os.getenv('CHNL_LNK', 'https://t.me/nch_Support')
TUTORIAL = os.getenv('TUTORIAL', 'https://t.me/How_To_Open_Linkl')
SUPPORT_CHAT = os.getenv('SUPPORT_CHAT', 'https:/t.me/NcHSupport')

# =========== Feature Toggles ===========

REQUEST_TO_JOIN_MODE = is_enabled(os.getenv('REQUEST_TO_JOIN_MODE', 'False'))
TRY_AGAIN_BTN = is_enabled(os.getenv('TRY_AGAIN_BTN', 'False'))
AI_SPELL_CHECK = is_enabled(os.getenv('AI_SPELL_CHECK', 'True'))
PM_SEARCH = is_enabled(os.getenv('PM_SEARCH', 'True'))
IS_SHORTLINK = is_enabled(os.getenv('IS_SHORTLINK', 'False'))
MAX_BTN = is_enabled(os.getenv('MAX_BTN', 'True'))
IS_TUTORIAL = is_enabled(os.getenv('IS_TUTORIAL', 'True'))
P_TTI_SHOW_OFF = is_enabled(os.getenv('P_TTI_SHOW_OFF', 'False'))
IMDB = is_enabled(os.getenv('IMDB', 'True'))
AUTO_FFILTER = is_enabled(os.getenv('AUTO_FFILTER', 'True'))
AUTO_DELETE = is_enabled(os.getenv('AUTO_DELETE', 'True'))
SINGLE_BUTTON = is_enabled(os.getenv('SINGLE_BUTTON', 'True'))
LONG_IMDB_DESCRIPTION = is_enabled(os.getenv('LONG_IMDB_DESCRIPTION', 'True'))
SPELL_CHECK_REPLY = is_enabled(os.getenv('SPELL_CHECK_REPLY', 'True'))
MELCOW_NEW_USERS = is_enabled(os.getenv('MELCOW_NEW_USERS', 'True'))
PROTECT_CONTENT = is_enabled(os.getenv('PROTECT_CONTENT', 'False'))
PUBLIC_FILE_STORE = is_enabled(os.getenv('PUBLIC_FILE_STORE', 'True'))
NO_RESULTS_MSG = is_enabled(os.getenv('NO_RESULTS_MSG', 'False'))
USE_CAPTION_FILTER = is_enabled(os.getenv('USE_CAPTION_FILTER', 'True'))

# =========== Shortlink Configuration ===========

VERIFY = is_enabled(os.getenv('VERIFY', 'False'))
VERIFY_SECOND_SHORTNER = is_enabled(os.getenv('VERIFY_SECOND_SHORTNER', 'False'))
VERIFY_SHORTLINK_URL = os.getenv('VERIFY_SHORTLINK_URL', '')
VERIFY_SHORTLINK_API = os.getenv('VERIFY_SHORTLINK_API', '')
VERIFY_SND_SHORTLINK_URL = os.getenv('VERIFY_SND_SHORTLINK_URL', '')
VERIFY_SND_SHORTLINK_API = os.getenv('VERIFY_SND_SHORTLINK_API', '')
VERIFY_TUTORIAL = os.getenv('VERIFY_TUTORIAL', 'https://t.me/How_To_Open_Linkl')

SHORTLINK_MODE = is_enabled(os.getenv('SHORTLINK_MODE', 'False'))
SHORTLINK_URL = os.getenv('SHORTLINK_URL', '')
SHORTLINK_API = os.getenv('SHORTLINK_API', '')

# =========== Other Settings ===========

MAX_B_TN = int(os.getenv('MAX_B_TN', '5'))
PORT = int(os.getenv('PORT', '8080'))
MSG_ALRT = os.getenv('MSG_ALRT', 'Hello My Dear Friends ❤️')
CUSTOM_FILE_CAPTION = os.getenv('CUSTOM_FILE_CAPTION', script.CAPTION)
BATCH_FILE_CAPTION = os.getenv('BATCH_FILE_CAPTION', CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = os.getenv('IMDB_TEMPLATE', script.IMDB_TEMPLATE_TXT)
MAX_LIST_ELM = int(os.getenv('MAX_LIST_ELM', '0'))  # Set to 0 for no limit

# =========== Choose Option Settings ===========

LANGUAGES = ["malayalam", "mal", "tamil", "tam", "english", "eng", "hindi", "hin", "telugu", "tel", "kannada", "kan"]
SEASONS = [f"season {i}" for i in range(1, 11)]
EPISODES = [f"E{str(i).zfill(2)}" for i in range(1, 41)]
QUALITIES = ["360p", "480p", "720p", "1080p", "1440p", "2160p"]
YEARS = [str(year) for year in range(1900, 2026)]

# =========== Stream and Download Configuration ===========

STREAM_MODE = is_enabled(os.getenv('STREAM_MODE', 'True'))
MULTI_CLIENT = is_enabled(os.getenv('MULTI_CLIENT', 'False'))
SLEEP_THRESHOLD = int(os.getenv('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(os.getenv('PING_INTERVAL', '1200'))
ON_HEROKU = 'DYNO' in os.environ
URL = os.getenv('URL', '')

# =========== Rename and Auto Approve Settings ===========

RENAME_MODE = is_enabled(os.getenv('RENAME_MODE', 'True'))
AUTO_APPROVE_MODE = is_enabled(os.getenv('AUTO_APPROVE_MODE', 'False'))

# =========== Logging Configuration ===========

LOG_STR = (
    "Current Customized Configurations are:\n"
    f"{'IMDB Results are enabled.' if IMDB else 'IMDB Results are disabled.'}\n"
    f"{'P_TTI_SHOW_OFF is enabled.' if P_TTI_SHOW_OFF else 'P_TTI_SHOW_OFF is disabled.'}\n"
    f"{'Single button mode is enabled.' if SINGLE_BUTTON else 'Single button mode is disabled.'}\n"
    f"{'Custom file caption is set.' if CUSTOM_FILE_CAPTION else 'No custom file caption found.'}\n"
    f"{'Long IMDB description is enabled.' if LONG_IMDB_DESCRIPTION else 'Long IMDB description is disabled.'}\n"
    f"{'Spell check reply is enabled.' if SPELL_CHECK_REPLY else 'Spell check reply is disabled.'}\n"
    f"{'MAX_LIST_ELM is set.' if MAX_LIST_ELM else 'No limit for list elements.'}\n"
    f"Current IMDB template: {IMDB_TEMPLATE}\n"
)
