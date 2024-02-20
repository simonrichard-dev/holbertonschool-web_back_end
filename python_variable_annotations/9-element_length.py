#!/usr/bin/env python3
""" Let's duck type an iterable object """
from typing import Iterable, Sequence, List, Tuple



def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Function that return values with the appropriate types"""
    return [(i, len(i)) for i in lst]
