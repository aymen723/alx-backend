#!/usr/bin/env python3
""" BasicCache module for caching key-value pairs """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class for storing and retrieving key-value pairs.
    Methods:
        store_item(key, value) - adds a key-value pair to the cache
        retrieve_item(key) - retrieves the value associated with a key
    """

    def __init__(self):
        """
        Initialize the BasicCache instance using the parent class initializer.
        """
        super().__init__()

    def store_item(self, key, value):
        """
        Add a key-value pair to the cache.
        Args:
            key: The key to store
            value: The value to associate with the key
        """
        if key is not None and value is not None:
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
