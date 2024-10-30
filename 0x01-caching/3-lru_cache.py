#!/usr/bin/env python3
""" LRUCache module implementing Least Recently Used (LRU) caching strategy """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache implements a Least Recently Used (LRU) caching system.
    Methods:
        store_item(key, value) - adds a key-value pair following LRU policy
        retrieve_item(key) - retrieves the value associated with a key
    """

    def __init__(self):
        """
        Initialize the LRUCache instance using the parent's initializer.
        """
        super().__init__()
        self.access_history = []  # Tracks key usage order for LRU management

    def store_item(self, key, value):
        """
        Add a key-value pair to the cache following LRU policy.
        If the cache exceeds its limit, removes the least recently used entry.
        
        Args:
            key: The key to store
            value: The value associated with the key
        """
        if key is not None and value is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                least_used_key = self.access_history.pop(0)
                print("DISCARD:", least_used_key)
                del self.cache_data[least_used_key]

            if key in self.access_history:
                self.access_history.remove(key)
                
            self.access_history.append(key)
            self.cache_data[key] = value

    def retrieve_item(self, key):
        """
        Retrieve the value associated with a key from the cache.
        If accessed, updates the key's position to mark it as recently used.
        
        Args:
            key: The key to retrieve the value for
        Returns:
            The value associated with the key, or None if the key is not found.
        """
        if key is not None and key in self.cache_data:
            self.access_history.remove(key)
            self.access_history.append(key)
            return self.cache_data[key]
        return None
