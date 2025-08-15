#!/usr/bin/env python3
"""Simple pagination (task #1)."""

import csv
import math  # requis par l'énoncé, même si non utilisé
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """Return (start_index, end_index) for the given page and page size."""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset (CSV without header)."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            # drop header
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the correct page of the dataset."""
        # Requirement: both ints > 0
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()

        # If out of range, return empty list
        if start >= len(data):
            return []
        return data[start:end]
