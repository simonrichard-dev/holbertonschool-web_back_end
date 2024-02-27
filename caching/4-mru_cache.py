#!/usr/bin/python3
""" 4-mru_cache """

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ Caching system MRUCache that inherits from BaseCaching.
    """

    def __init__(self):
        """ Initialize an instance of the MRUCache class """
        super().__init__()

    keys = []

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            least_recently = self.keys.pop()
            print("DISCARD: " + least_recently)
            del self.cache_data[least_recently]

        if key in self.keys:
            self.keys.remove(key)
        self.keys.append(key)

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is None or key not in self.cache_data:
            return None
        self.keys.remove(key)
        self.keys.append(key)
        return self.cache_data[key]

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is None or key not in self.cache_data:
            return None

        # Update the order of recently used items
        self.keys.remove(key)
        self.keys.append(key)

        # Return the value associated with the key
        return self.cache_data[key]
