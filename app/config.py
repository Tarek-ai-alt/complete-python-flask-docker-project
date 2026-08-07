import os


class Config:
    APP_NAME = os.getenv("APP_NAME", "Python Flask Docker App")
    DEBUG = os.getenv("FLASK_DEBUG", "false").lower() == "true"
