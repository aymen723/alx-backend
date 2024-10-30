#!/usr/bin/env python3
""" FIFOCache module implementing FIFO caching strategy """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache implements a First-In-First-Out (FIFO) caching system.
    Methods:
        store_item(key, value) - adds a key-value pair following FIFO policy
        retrieve_item(key) - retrieves the value associated with a key
    """

    def __init__(self):
        """
        Initialize the FIFOCache instance using the parent's initializer.
        """
        super().__init__()
        self.access_order = []  # Tracks insertion order for FIFO management

    def store_item(self, key, value):
        """
        Add a key-value pair to the cache following FIFO policy.
        If the cache exceeds its limit, removes the oldest entry.
        
        Args:
            key: The key to store
            value: The value associated with the key
        """
        if key is not None and value is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                oldest_key = self.access_order.pop(0)
                print("DISCARD:", oldest_key)
                del self.cache_data[oldest_key]

            self.access_order.append(key)
            self.cache_data[key] = value

    def retrieve_item(self, key):
        """
        Retrieve the value associated with a key from the cache.
        
        Args:
            key: The key to retrieve the value for
        Returns:
            The value associated with the key, or None if the key is not found.
        """
        return self.cache_data.get(key) if key is not None else None
