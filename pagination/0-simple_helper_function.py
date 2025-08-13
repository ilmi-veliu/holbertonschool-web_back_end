#!/usr/bin/env python3
"""
Simple helper function for pagination
"""


def index_range(page, page_size):
    """
    Calculate the start and end indexes for pagination.
    
    Args:
        page (int): The page number (1-indexed)
        page_size (int): The number of items per page
        
    Returns:
        tuple: A tuple containing (start_index, end_index)
    """
    return (page - 1) * page_size, page * page_size
