#!/usr/bin/python3
""" 1-fifo_cache """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ Caching system FIFOCache that inherits from BaseCaching.
    """

    def put(self, key, item):
        """Add an item to the cache
        if both key and item are not None"""
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            for _ in range(len(self.cache_data)):
                last_key = list(self.cache_data)[-1]
                print('DISCARD: ' + self.cache_data[last_key])
                del self.cache_data[last_key]
            self.cache_data[key] = item
        elif key is not None and item is not None:
            self.cache_data[key] = item
        else:
            pass

    def get(self, key):
        """Retrieve an item from the cache if
        the key is not None and exists"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
