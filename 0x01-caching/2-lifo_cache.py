#!/usr/bin/env python3
""" LIFOCache module implementing LIFO caching strategy """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache implements a Last-In-First-Out (LIFO) caching system.
    Methods:
        store_item(key, value) - adds a key-value pair following LIFO policy
        retrieve_item(key) - retrieves the value associated with a key
    """

    def __init__(self):
        """
        Initialize the LIFOCache instance using the parent's initializer.
        """
        super().__init__()
        self.access_stack = []  # Tracks insertion order for LIFO management

    def store_item(self, key, value):
        """
        Add a key-value pair to the cache following LIFO policy.
        If the cache exceeds its limit, removes the most recently added entry.
        
        Args:
            key: The key to store
            value: The value associated with the key
        """
        if key is not None and value is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                last_key = self.access_stack.pop()
                print("DISCARD:", last_key)
                del self.cache_data[last_key]

            if key in self.access_stack:
                self.access_stack.remove(key)
                
            self.access_stack.append(key)
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
