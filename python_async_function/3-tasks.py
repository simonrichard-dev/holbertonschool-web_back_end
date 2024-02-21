#!/usr/bin/env python3
import asyncio
from asyncio.tasks import Task


wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> Task:
    async def wait_random_wrapper():
        result = await wait_random(max_delay)
        return result

    return asyncio.create_task(wait_random_wrapper())
