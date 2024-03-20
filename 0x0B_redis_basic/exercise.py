#!/usr/bin/env python3
"""
0. Writing strings to Redis
"""
import redis
from typing import Union, Callable, Optional
import uuid


class Cache:
    """  class to write data to Redis """

    def __init__(self):
        """ Initialize the Cache with a Redis client. """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ takes a data argument and returns a string """
        key = str(uuid.uuid4())  # Generate a random key
        # Store data in Redis with the generated key
        self._redis.set(name=key, value=data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[
        str, bytes, int, float, None]:
        """
        Retrieve data from Redis using the given key and optionally convert it back to the desired format.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)

    def get_str(self, key: str) -> Optional[str]:
        """ 
        Retrieve data from Redis using the given key and conert it to a string
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve data from Redis using the given key and convert it to an integer.
        """
        return self.get(key, fn=int)
