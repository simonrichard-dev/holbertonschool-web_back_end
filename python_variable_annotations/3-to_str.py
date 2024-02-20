#!/usr/bin/env python3
""" Basic annotations - to string """
import math


def to_str(n: float) -> str:
    """ takes a float n as arg & returns his string representation.
        Args:
            n: float;
        Return:
            str;
    """
    if type(n) is float:
        return str(n)
    else:
        return False
