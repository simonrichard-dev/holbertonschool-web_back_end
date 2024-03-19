#!/usr/bin/env python3
"""
0. Writing strings to Redis
"""
import redis
from typing import Union
import uuid


class Cache:
    """  class to write data to Redis """

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, float, int, bytes]) -> str:
        """ takes a data argument and returns a string """
        key = str(uuid.uuid4())  # Generate a random key
        # Store data in Redis with the generated key
        self._redis.set(name=key, value=data)
        return key
