#!/usr/bin/env python3
""" MRUCache module implementing Most Recently Used (MRU) caching strategy """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache implements a Most Recently Used (MRU) caching system.
    Methods:
        store_item(key, value) - adds a key-value pair following MRU policy
        retrieve_item(key) - retrieves the value associated with a key
    """

    def __init__(self):
        """
        Initialize the MRUCache instance using the parent's initializer.
        """
        super().__init__()
        self.recent_usage = []  # Tracks key usage order for MRU management

    def store_item(self, key, value):
        """
        Add a key-value pair to the cache following MRU policy.
        If the cache exceeds its limit, removes the most recently used entry.
        
        Args:
            key: The key to store
            value: The value associated with the key
        """
        if key is not None and value is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                most_recent_key = self.recent_usage.pop()
                print("DISCARD:", most_recent_key)
                del self.cache_data[most_recent_key]

            if key in self.recent_usage:
                self.recent_usage.remove(key)
                
            self.recent_usage.append(key)
            self.cache_data[key] = value

    def retrieve_item(self, key):
        """
        Retrieve the value associated with a key from the cache.
        If accessed, updates the key's position to mark it as most recently used.
        
        Args:
            key: The key to retrieve the value for
        Returns:
            The value associated with the key, or None if the key is not found.
        """
        if key is not None and key in self.cache_data:
            self.recent_usage.remove(key)
            self.recent_usage.append(key)
            return self.cache_data[key]
        return None
