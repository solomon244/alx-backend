#!/usr/bin/env python3
"""
class LRUCache that inherits from BaseCaching and is a caching system:
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    put(key, item)
        Add an item in the cache
        Get an item by key
    """
    def __init__(self):
        """ Initialize the class using the parent class __int__ method"""
        self.cache_data = OrderedDict()

    def get(self, key):
        """
        Get an item by key
       item corresponding to a given key or
        """
        if key is None or key not in self.cache_data.keys():
            return
        try:
            value = self.cache_data.pop(key)
            self.cache_data[key] = value
            return value
        except KeyError:
            return

    def put(self, key, item):
        """
        Add an item in the cache using LRUCache eviction techniques

        value corresponding to a given key of cache_data dictionary
        """
        if key is None or item is None:
            pass
        else:
            try:
                self.cache_data.pop(key)
            except KeyError:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    first = next(iter(self.cache_data))
                    self.cache_data.pop(first)
                    print(f"DISCARD: {first}")
            self.cache_data[key] = item
