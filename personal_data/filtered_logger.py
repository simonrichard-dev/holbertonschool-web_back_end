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
    return re.sub(r'(' + '|'.join(fields) + ')=([^' + separator + ']+)',
                  r'\1=' + redaction, message)
