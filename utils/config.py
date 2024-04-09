import os

from dotenv import load_dotenv

from utils.logger import LoggerInitializer

logging = LoggerInitializer.init_loggers("Config")
load_dotenv()

DATABASE_HOST = os.getenv("DB_HOST")
DATABASE_PORT = os.getenv("DB_PORT")
DATABASE_USERNAME = os.getenv("DB_USER")
DATABASE_PASSWORD = os.getenv("DB_PASS")
