#!/usr/bin/env python3
"""
Caching.

LRU Cache
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRU Caching."""

    def __init__(self):
        """Initialize."""
        super().__init__()

    def put(self, key, item):
        """Put item value for the key key."""
        if key is None or item is None:
            return
        if self.cache_data.get(key) is not None:
            del self.cache_data[key]
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            for k in self.cache_data.keys():
                self.cache_data.pop(k)
                print(f'DISCARD: {k}')
                break
        self.cache_data[key] = item

    def get(self, key):
        """Get item from cache."""
        if key is None:
            return None
        item = self.cache_data.get(key)
        if item is None:
            return None
        del self.cache_data[key]
        self.cache_data[key] = item
        return item
