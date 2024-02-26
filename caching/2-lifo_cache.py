#!/usr/bin/python3
""" 2-lifo_cache """

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ Caching system FIFOCache that inherits from BaseCaching.
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """Add an item to the cache
        if both key and item are not None"""
        if key is not None and item is not None:  # check the key and item values
            if key in self.cache_data:
                self.cache_data[key] = item

            else:
                self.cache_data[key] = item  # add item at end of dict
                if len(self.cache_data) <= BaseCaching.MAX_ITEMS:
                    pass
                elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    print("DISCARD: " + self.last_key)
                    del self.cache_data[self.last_key]
            self.cache_data[key] = item
            self.last_key = key
        else:
            return

    def get(self, key):
        """Retrieve an item from the cache if
        the key is not None and exists"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
