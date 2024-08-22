#!/usr/bin/env python3
"""
Caching.

LFU Cache
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """LFU Caching."""

    def __init__(self):
        """Initialize."""
        super().__init__()
        self.cache_frequency = {}

    def put(self, key, item):
        """Put item value for the key key."""
        if key is None or item is None:
            return
        count = 0
        if key in self.cache_data:
            del self.cache_data[key]
            count = self.cache_frequency[key] + 1
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lfu = []
            minv = list(self.cache_frequency.values())[0]
            for _key, _count in self.cache_frequency.items():
                if _count < minv:
                    lfu = [_key]
                    minv = _count
                elif _count == minv:
                    lfu.append(_key)
            if len(lfu) == 1:
                self.cache_data.pop(lfu[0])
                self.cache_frequency.pop(lfu[0])
                print(f'DISCARD: {lfu[0]}')
            else:
                for k in self.cache_data.keys():
                    if k in lfu:
                        self.cache_data.pop(k)
                        self.cache_frequency.pop(k)
                        print(f'DISCARD: {k}')
                        break
        self.cache_frequency[key] = count
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
        self.cache_frequency[key] += 1
        return item
