#!/usr/bin/env python3
"""  Async Comprehensions """

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ coroutine that will execute async_comprehension
        four times in parallel using asyncio.gather.
        Args:
            None
        Return:
            measure runtime : float;
    """

    start = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )

    return(time.time() - start)
