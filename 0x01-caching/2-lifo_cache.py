#!/usr/bin/env python3
"""
lifo_cache.
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    A class used to represent LIFOCache
        value corresponding to a given key of cache_data dictionary
    """
    def __init__(self):
        """ Initialize the class using the parent class __int__ method"""
        super().__init__()

    def put(self, key, item):
        """
        Add an item in the cache using LIFO eviction techniques
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key not in self.cache_data.keys():
                    last = self.cache_data.popitem()
                    print(f"DISCARD: {last[0]}")
                else:
                    self.cache_data.pop(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data.keys():
            return
        return self.cache_data.get(key)
