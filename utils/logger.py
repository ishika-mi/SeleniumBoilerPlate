import logging
import sys

from utils.constants import LOGS_FORMATTER


class LoggerInitializer:
    FORMATTER = logging.Formatter(LOGS_FORMATTER)

    @staticmethod
    def get_console_handler():
        """
        Get the console handler.

        Returns:
            logging.StreamHandler: The console handler object.
        """
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(LoggerInitializer.FORMATTER)
        return console_handler

    @classmethod
    def init_loggers(cls, logger_name: str = "Selenium") -> logging.Logger:
        """
        Initialize the loggers.

        Parameters:
            logger_name (str): The name of the logger.

        Returns:
            logging.Logger: The logger object.
        """
        logger = logging.getLogger(logger_name)
        if not logger.handlers:
            logger.setLevel(logging.DEBUG)
            logger.addHandler(cls.get_console_handler())
            logger.propagate = False
        return logger
