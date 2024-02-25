#!/usr/bin/python3
""" 1-fifo_cache """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ Caching system FIFOCache that inherits from BaseCaching.
    """

    def put(self, key, item):
        """Add an item to the cache
        if both key and item are not None"""
        if key is not None and item is not None:
            self.cache_data[key] = item # add item at end of dict
            if len(self.cache_data) <= BaseCaching.MAX_ITEMS:
                pass
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key = list(self.cache_data)[0]
                print('DISCARD: ' + first_key)
                del self.cache_data[first_key]
        else:
            pass

    def get(self, key):
        """Retrieve an item from the cache if
        the key is not None and exists"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
