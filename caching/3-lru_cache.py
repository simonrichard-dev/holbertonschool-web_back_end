#!/usr/bin/python3
""" 3-lru_cache """

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ Caching system LRUCache that inherits from BaseCaching.
    """

    def __init__(self):
        """ Initialize an instance of the LRUCache class """
        super().__init__()
        self.cache_data = {}
        self.keys = []

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return
        self.cache_data[key] = item

        if key in self.keys:
            self.keys.remove(key)
        self.keys.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            least_recently = self.keys.pop(0)
            print("DISCARD: " + least_recently)
            del self.cache_data[least_recently]

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is None or key not in self.cache_data:
            return None
        self.keys.remove(key)
        self.keys.append(key)
        return self.cache_data[key]
