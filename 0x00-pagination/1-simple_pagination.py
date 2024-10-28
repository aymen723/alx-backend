#!/usr/bin/env python3
"""
Defines the Server class to paginate a database of popular baby names.
"""
import csv
import math
from typing import List, Tuple


def get_pagination_range(current_page: int, items_per_page: int) -> Tuple[int, int]:
    """
    Calculates the start and end indices for a paginated list based on
    the specified page number and items per page.
    
    Args:
        current_page (int): the page number to display (1-indexed)
        items_per_page (int): the number of items on each page
        
    Returns:
        tuple(start_index, end_index): indices for the list slice
    """
    start_index, end_index = 0, 0
    for _ in range(current_page):
        start_index = end_index
        end_index += items_per_page

    return (start_index, end_index)


class Server:
    """Server class to manage pagination of a database of popular baby names."""
    
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Loads and caches the dataset from a CSV file if not already loaded."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Exclude header row

        return self.__dataset

    def get_page(self, current_page: int = 1, items_per_page: int = 10) -> List[List]:
        """
        Retrieves a specific page of records from the dataset based on the page
        number and the number of items per page.
        
        Args:
            current_page (int): the desired page number, must be a positive integer
            items_per_page (int): the number of records per page, must be positive
            
        Returns:
            A list of lists containing the data for the requested page, or an empty
            list if the indices exceed the dataset length.
        """
        assert isinstance(current_page, int) and current_page > 0, "Page number must be a positive integer"
        assert isinstance(items_per_page, int) and items_per_page > 0, "Page size must be a positive integer"

        dataset = self.dataset()
        data_length = len(dataset)
        
        start_index, end_index = get_pagination_range(current_page, items_per_page)
        if start_index >= data_length:
            return []
        
        return dataset[start_index:end_index]
