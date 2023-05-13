import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5617535290:AAF6vw8CYybW0BDVH4hKQ4d_rKVLrWTksfo")

    APP_ID = int(os.environ.get("APP_ID", "12421436"))

    API_HASH = os.environ.get("API_HASH", "fbe8061f1148eabbacdf9e0713e8b74a")
