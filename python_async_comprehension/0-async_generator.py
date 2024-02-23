#!/usr/bin/env python3
""" Async Generator """

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ corotine that wait a random delay and return
        a yield generator
        Args:
            None
        Return:
            float;
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
