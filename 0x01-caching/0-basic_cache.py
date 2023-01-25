#!/usr/bin/env python3
"""BasicCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """allows storing and
    retrieving items from a dictionary.
    """
    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item 
        """
        return self.cache_data.get(key, None)
