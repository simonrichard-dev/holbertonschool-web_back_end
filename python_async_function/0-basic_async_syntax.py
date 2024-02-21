#!/usr/bin/env python3
""" The basics of async """
import asyncio
import random


async def wait_random(max_delay: float = 10) -> float:
    """ corotine that wait a random delay and return it
        Args:
            max_delay: float;
        Return:
            float;
    """
    dealay = random.uniform(0, max_delay)
    await asyncio.sleep(dealay)
    return (dealay)
