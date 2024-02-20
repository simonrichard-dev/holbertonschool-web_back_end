#!/usr/bin/env python3
""" Complex types - list of floats """
import math


def sum_list(input_list: list[float]) -> float:
    """ takes a list of float as arg & returns his sum as float.
        Args:
            input_list: list of float;
        Return:
            float;
    """
    return sum(float(i) for i in input_list)