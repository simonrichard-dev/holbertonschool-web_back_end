#!/usr/bin/env python3
""" Complex types - list of floats """
import math
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ takes a list of float as arg & returns his sum as float.
        Args:
            input_list: list of float;
        Return:
            float;
    """
    return sum(float(i) for i in input_list)
