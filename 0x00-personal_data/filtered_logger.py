#!/usr/bin/env python3
"""Module for the logging filter"""
import re
from typing import List

def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """for the filtering a log message"""
    pattern = '|'.join([f'{field}=[^{separator}]+'for field in fields])
    return re.sub(pattern, lambda match: match.group(0).split('=')[0] + '=' + redaction, message)
