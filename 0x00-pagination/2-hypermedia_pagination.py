#!/usr/bin/env python3
"""
Provides the Server class with methods to create pagination from CSV data.
"""
import csv
from typing import List
get_pagination_range = __import__('0-simple_helper_function').get_pagination_range


class Server:
    """Server class to manage pagination of a popular baby names database."""
    
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def load_dataset(self) -> List[List]:
        """
        Reads and caches the dataset from a CSV file.
        
        Returns:
            List[List]: The dataset without the header row.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header row

        return self.__dataset

    @staticmethod
    def assert_positive_integer(value: int) -> None:
        """
        Ensures the provided value is a positive integer.
        
        Args:
            value (int): The integer to validate.
        """
        assert isinstance(value, int) and value > 0, "Value must be a positive integer."

    def get_page(self, current_page: int = 1, items_per_page: int = 10) -> List[List]:
        """
        Retrieves a specific page of data from the dataset.
        
        Args:
            current_page (int): The desired page number.
            items_per_page (int): The number of items per page.
            
        Returns:
            List[List]: A subset of the dataset for the requested page.
        """
        self.assert_positive_integer(current_page)
        self.assert_positive_integer(items_per_page)
        
        dataset = self.load_dataset()
        start_index, end_index = get_pagination_range(current_page, items_per_page)
        try:
            data = dataset[start_index:end_index]
        except IndexError:
            data = []
        return data

    def get_pagination_info(self, current_page: int = 1, items_per_page: int = 10) -> dict:
        """
        Provides paginated data along with additional metadata.
        
        Args:
            current_page (int): The page number to display.
            items_per_page (int): The number of items per page.
            
        Returns:
            dict: A dictionary containing pagination information and the data.
        """
        total_pages = (len(self.load_dataset()) + items_per_page - 1) // items_per_page
        data = self.get_page(current_page, items_per_page)
        
        pagination_info = {
            "current_page": current_page,
            "items_per_page": items_per_page if items_per_page <= len(data) else len(data),
            "total_pages": total_pages,
            "data": data,
            "previous_page": current_page - 1 if current_page > 1 else None,
            "next_page": current_page + 1 if current_page + 1 <= total_pages else None
        }
        return pagination_info
