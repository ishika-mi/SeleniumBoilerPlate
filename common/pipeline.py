from database import Database

from utils.config import DATABASE_HOST, DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_PORT
from utils.logger import LoggerInitializer


class DataPipeline:
    def __init__(self):
        self.database = Database(DATABASE_HOST, DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_PORT)
        self.logging = LoggerInitializer.init_loggers("Pipeline")

    def fill_scraped_data(self, fields):
        self.database.connect()

        # Example query execution
        query = "INSERT INTO scraped_data_table (field1, field2) VALUES (%s, %s)"
        values = (fields["field1"], fields["field2"])
        self.database.execute_query(query, values)

        # Disconnect from the database
        self.database.disconnect()
