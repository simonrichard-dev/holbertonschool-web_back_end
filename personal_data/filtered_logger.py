#!/usr/bin/env python3
"""
Filter Datum
"""

from typing import List
import re

def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str
        ) -> str:
    """Obfuscates specified fields in a log message."""
    for field in fields:
        message = re.sub(f"{field}=[^;{separator}]*",
                         f"{field}={redaction}", message)
    return message
