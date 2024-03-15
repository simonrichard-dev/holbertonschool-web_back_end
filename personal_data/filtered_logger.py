#!/usr/bin/env python3
""" Module for implementing a filter_datum function """

from typing import List
import re
import logging


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
