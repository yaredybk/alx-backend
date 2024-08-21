#!/usr/bin/env python3
"""
Caching
"""
BaseCaching = __import__(base_caching).BaseCaching


class BaseCaching(BaseCaching):
    """BaseCaching 
    """

    def __init__(self):
        """Initialize
        """
        pass

    def put(self, key, item):
        """Put item value for the key key.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get item from cache."""
        if key is None:
            return None
        return self.cache_data[key]
