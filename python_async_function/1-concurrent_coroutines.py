#!/usr/bin/env python3
""" Let's execute multiple coroutines at the same time with async """
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """ corotine that wait a random delay and return it
        Args:
            n: int;
            max_delay: int;
        Return:
            list of floats;
    """
    delays = []

    for _ in range (n):
        delay = await wait_random(max_delay)
        i = 0
        while i < len(delays) and delay > delays[i]:
            i += 1
        delays.insert(i, delay)
    return (delays)
