#!/usr/bin/env python3
""" Complex types - mixed list """
import math
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ takes a list of int & float as arg &
        returns his sum as float.
        Args:
            input_list: list of int & float;
        Return:
            float;
    """
    return (str(k), math.pow(v, 2))
