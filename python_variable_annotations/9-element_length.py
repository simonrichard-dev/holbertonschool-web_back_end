#!/usr/bin/env python3
""" Let's duck type an iterable object """
from typing import Union, List, Sequence, Tuple, Iterable



def element_length(lst):
    return [(i, len(i)) for i in lst]