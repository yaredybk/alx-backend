#!/usr/bin/env python3
"""
Caching

LIFO Cache
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Caching."""

    def __init__(self):
        """Initialize."""
        super().__init__()

    def put(self, key, item):
        """Put item value for the key key."""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and \
                    self.cache_data.get(key) is None:
                k, _ = self.cache_data.popitem()
                print(f'DISCARD: {k}')
            self.cache_data[key] = item

    def get(self, key):
        """Get item from cache."""
        if key is None:
            return None
        return self.cache_data.get(key)
