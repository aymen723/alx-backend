#!/usr/bin/env python3
"""
Defines get_pagination_range helper function.
"""
from typing import Tuple


def get_pagination_range(current_page: int, items_per_page: int) -> Tuple[int, int]:
    """
    Calculates the start and end indices for paginating a list based on
    the current page number and items per page.
    
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
