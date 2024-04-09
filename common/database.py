# database.py
from utils.logger import LoggerInitializer


class Database:
    def __init__(self, host, username, password, database):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.logging = LoggerInitializer.init_loggers("Database")

    def connect(self):
        pass  # todo create connection logic

    def disconnect(self):
        pass  # todo close connection

    def execute_query(self, query, values=None):
        pass  # todo create execute query logic
