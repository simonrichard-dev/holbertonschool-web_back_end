#!/usr/bin/env python3
""" Async Generator """

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
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
