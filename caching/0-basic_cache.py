#!/usr/bin/python3
""" 0-basic_cache """

from typing import Any, Optional
BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    """ Caching system BasicCache that inherits from BaseCaching.
    """
    def put(self, key, item):
        """Add an item to the cache
        if both key and item are not None"""
        if key is not None and item is not None:
            self.cache_data[key] = item
        else :
            pass

    def get(self, key):
        """Retrieve an item from the cache if
        the key is not None and exists"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
