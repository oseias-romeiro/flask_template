import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()

class Config(object):
    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY",) # In production, should be set to a random string
    SQLALCHEMY_ECHO = os.environ.get("SQLALCHEMY_ECHO", False) # Print in console all SQL commands

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'db.sqlite3')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'db.test.sqlite3')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True


config_map = {
    "development":  DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
}

def get_env():
    if os.getenv("APP_ENV") == "production":
        return "production"
    elif os.getenv("APP_ENV") == "testing":
        return "testing"
    else:
        return "development"

def get_config() -> Config:
    print("!!! init config !!!")
    env = get_env()
    print(f"!!! env: {env} !!!")
    return config_map[env]
    # get config environment from environment variable, default to development
   
