import re
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

API_ID = int(environ.get("API_ID", "24210243"))
API_HASH = environ.get("API_HASH", "509031fb3790b968e489f71d591ebce5")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002294535138"))
ADMINS = int(environ.get("ADMINS", "8050649116"))
DB_URI = environ.get("DB_URI", "")
DB_NAME = environ.get("DB_NAME", "chatgpthanzobot")
OPENAI_API = environ.get("OPENAI_API", "")
AI = is_enabled((environ.get("AI","True")), False)
