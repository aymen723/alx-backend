#!/usr/bin/env python3
""" LFUCache module implementing Least Frequently Used (LFU) caching strategy """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache implements a Least Frequently Used (LFU) caching system.
    Methods:
        store_item(key, value) - adds a key-value pair following LFU policy
        retrieve_item(key) - retrieves the value associated with a key
    """

    def __init__(self):
        """
        Initialize the LFUCache instance using the parent's initializer.
        """
        super().__init__()
        self.access_order = []    # Tracks access order to handle ties in LFU eviction
        self.access_frequency = {}  # Tracks access frequency of each key

    def store_item(self, key, value):
        """
        Add a key-value pair to the cache following LFU policy.
        If the cache exceeds its limit, removes the least frequently used entry.
        If there are ties, removes the least recently used among them.
        
        Args:
            key: The key to store
            value: The value associated with the key
        """
        if key is not None and value is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                # Find least frequently used keys
                min_frequency = min(self.access_frequency.values())
                least_frequent_keys = [k for k, v in self.access_frequency.items() if v == min_frequency]
                
                # If multiple least frequent keys, discard least recently used one
                if len(least_frequent_keys) > 1:
                    discard_key = min(least_frequent_keys, key=lambda k: self.access_order.index(k))
                else:
                    discard_key = least_frequent_keys[0]
                
                print("DISCARD:", discard_key)
                del self.cache_data[discard_key]
                del self.access_order[self.access_order.index(discard_key)]
                del self.access_frequency[discard_key]

            # Update frequency and access order
            self.access_frequency[key] = self.access_frequency.get(key, 0) + 1
            if key in self.access_order:
                self.access_order.remove(key)
            self.access_order.append(key)
            self.cache_data[key] = value

    def retrieve_item(self, key):
        """
        Retrieve the value associated with a key from the cache.
        If accessed, updates the key's frequency and its position in the access order.
        
        Args:
            key: The key to retrieve the value for
        Returns:
            The value associated with the key, or None if the key is not found.
        """
        if key is not None and key in self.cache_data:
            self.access_order.remove(key)
            self.access_order.append(key)
            self.access_frequency[key] += 1
            return self.cache_data[key]
        return None
