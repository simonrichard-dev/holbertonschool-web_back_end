#!/usr/bin/env python3
"""
0. Writing strings to Redis
"""
import redis
from typing import Union, Callable, Optional
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ decorator to count how many times methods of the Cache class are called """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """ decorator to store the history of inputs and outputs for a particular function """
    @wraps(method)
    def wrapper(self, *args):
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"
        
        # Store inputs
        self._redis.rpush(input_key, str(args))
        
        # Execute the method and get the output
        output = method(self, *args)
        
        # Store output
        self._redis.rpush(output_key, str(output))
        return output
    return wrapper

def replay(self, method: Callable) -> None:
    """ Display the history of calls of a particular function."""

    r = method.__self__._redis
    method_name = method.__qualname__
    count = r.get(method_name).decode('utf-8')

    print(f"{method_name} was called {count} times:")

    inputs = f"{method_name}:inputs"
    outputs = f"{method_name}:outputs"

    input_list = r.lrange(inputs, 0, -1)
    output_list = r.lrange(outputs, 0, -1)

    for input_, output_ in zip(input_list, output_list):
        input_str = input_.decode('utf-8')
        output_str = output_.decode('utf-8')
        print(f"{method_name}(*{input_str}) -> {output_str}")

class Cache:
    """  class to write data to Redis """

    def __init__(self):
        """ Initialize the Cache with a Redis client. """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
        data = self._redis.get(name=key)
        if data is not None and fn:
            return fn(data)
        return data

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
