#!/usr/bin/env python3
"""
Filter Datum
"""

from typing import List
import re

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """Obfuscates specified fields in a log message.

    Args:
        fields (List[str]): A list of strings representing fields to obfuscate.
        redaction (str): A string representing the value by which the fields will be obfuscated.
        message (str): A string representing the log line.
        separator (str): A string representing the character separating all fields in the log line.

    Returns:
        str: The log message with obfuscated fields.

    """
    return re.sub(r'(' + '|'.join(fields) + ')=([^' + separator + ']+)',
                  r'\1=' + redaction, message)
