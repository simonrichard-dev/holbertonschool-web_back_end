#!/usr/bin/env python3
""" 4-Task """

import asyncio
import random
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ corotine that wait a random delay and return it
        Args:
            n: int;
            max_delay: int;
        Return:
            list of floats;
    """
    coroutines = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    for coroutine in asyncio.as_completed(coroutines):
        delay = await coroutine
        delays.append(delay)
    return delays
