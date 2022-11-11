import os


class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5614880465:AAFXghuETOaY7Stj3AyY-CYqpTVFtm1J2Do")

    APP_ID = int(os.environ.get("APP_ID", "11004381"))

    API_HASH = os.environ.get("API_HASH", "8e0588044fcf7672cfe1341185bfc94c")

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
