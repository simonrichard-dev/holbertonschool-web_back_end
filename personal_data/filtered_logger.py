#!/usr/bin/env python3
""" Module for implementing a filter_datum function """

from typing import List
import re
import logging
import csv

# Define the PII fields from the user_data.csv file
PII_FIELDS = ('name','email','phone','ssn','password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Formats the log message by filtering values."""
        message = super().format(record)
        for field in self.fields:
            message = filter_datum([field], self.REDACTION, message,
                                   self.SEPARATOR)
        return message


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str
        ) -> str:
    """ Function that returns the log message obfuscated """
    for field in fields:
        pattern = (f"{field}=.*?{separator}")
        message = re.sub(pattern, (f"{field}={redaction}{separator}"), message)
    return message


def get_logger() -> logging.Logger:
    """ function that takes no arguments and returns a logging.Logger """
    # Initialize logger named "user_data"
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)  # Only log messages up to logging.INFO level

    # Do not propagate messages to other loggers
    logger.propagate = False

    # Use a StreamHandler with RedactingFormatter as formatter
    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)

    # Add the stream handler to the logger
    logger.addHandler(stream_handler)

    return logger