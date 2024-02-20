#!/usr/bin/env python3
""" Basic annotations - add """


def add (a: float, b: float) -> float:
    """  takes a float a and a float b as arguments and returns their sum as a float.
        Args:
        a: float;
        b: float;
    """
    if type(a) is float and type(b) is float:
        return a + b
    else:
        return False