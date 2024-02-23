#!/usr/bin/env python3
"""  Async Comprehensions """

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ coroutine will collect 10 random numbers
        using an async comprehensing
        Args:
            None
        Return:
            list of float;
    """
    results = [i async for i in async_generator()]
    return results

asyncio.run(async_comprehension())
