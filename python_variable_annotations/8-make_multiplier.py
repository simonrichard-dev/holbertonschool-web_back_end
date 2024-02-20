#!/usr/bin/env python3
""" Complex types - mixed list """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Function to create a multiplier function.
        Args:
            multiplier (float): The multiplier value.
        Return:
            A callable function that multiplies a float;
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
