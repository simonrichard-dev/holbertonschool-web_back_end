#!/usr/bin/env python3
""" Complex types - mixed list """
import math
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ takes a list of int & float as arg &
        returns his sum as float.
        Args:
            input_list: list of int & float;
        Return:
            float;
    """
    return sum(mxd_lst)
