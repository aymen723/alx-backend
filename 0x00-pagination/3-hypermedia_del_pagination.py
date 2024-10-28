#!/usr/bin/env python3
"""
Provides a Server class with deletion-resilient hypermedia pagination.
"""

import csv
from typing import List, Dict


class Server:
    """Server class to handle pagination of a database of popular baby names."""
    
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def load_dataset(self) -> List[List]:
        """Loads and caches the dataset from the CSV file.
        
        Returns:
            List[List]: The cached dataset, excluding the header row.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header row

        return self.__dataset

    def load_indexed_dataset(self) -> Dict[int, List]:
        """Indexes the dataset for deletion-resilient pagination.
        
        Returns:
            Dict[int, List]: Indexed dataset where each key is the record index.
        """
        if self.__indexed_dataset is None:
            dataset = self.load_dataset()
            self.__indexed_dataset = {
                index: dataset[index] for index in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, start_index: int = None, page_size: int = 10) -> Dict:
        """
        Provides a deletion-resilient page of data with pagination metadata.
        
        Args:
            start_index (int): The index of the first item to display.
            page_size (int): Number of records to include on the page.
            
        Returns:
            Dict: A dictionary with pagination metadata and the page data.
        """
        dataset = self.load_indexed_dataset()
        data_length = len(dataset)
        assert 0 <= start_index < data_length, "start_index must be within dataset range"
        
        pagination_data = {
            "start_index": start_index,
            "page_size": 0,  # Will update with actual data length
            "data": [],
            "next_index": None
        }
        
        page_data = []
        current_index = start_index

        while len(page_data) < page_size and current_index < data_length:
            record = dataset.get(current_index)
            current_index += 1
            if record is not None:
                page_data.append(record)

        pagination_data["data"] = page_data
        pagination_data["page_size"] = len(page_data)
        pagination_data["next_index"] = current_index if current_index < data_length else None

        return pagination_data
