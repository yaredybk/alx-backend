#!/usr/bin/env python3
"""
Caching

FIFO Cache
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Caching."""

    def __init__(self):
        """Initialize."""
        super().__init__()
        # self.cache_data = OrderedDict()

    def put(self, key, item):
        """Put item value for the key key."""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                for k in self.cache_data.keys():
                    self.cache_data.pop(k)
                    print(f'DISCARD: {k}')
                    break

    def get(self, key):
        """Get item from cache."""
        if key is None:
            return None
        return self.cache_data.get(key)
