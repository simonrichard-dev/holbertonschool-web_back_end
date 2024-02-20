#!/usr/bin/env python3
""" Basic annotations - floor """
import math


def floor(n: float) -> int:
    """ takes a float n as arg & returns the floor of the float.
        Args:
            n: float;
    """
    if type(n) is float:
        return math.floor(n)
    else:
        return False
