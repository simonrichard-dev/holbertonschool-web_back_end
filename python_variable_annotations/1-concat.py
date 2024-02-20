#!/usr/bin/env python3
""" Basic annotations - concat """


def concat(str1: str, str2: str) -> str:
    """ takes str as arguments & returns sum as a concatened str.
        Args:
            str1: str;
            str2: str;
    """
    if type(str1) is str and type(str2) is str:
        return str1 + str2
    else:
        return False
