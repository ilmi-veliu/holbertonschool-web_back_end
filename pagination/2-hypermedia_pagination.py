#!/usr/bin/env python3

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and page > 0, "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "page_size must be a positive integer"
        
        start_index, end_index = index_range(page, page_size)
        data = self.dataset()
        
        if start_index >= len(data):
            return []
        
        return data[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        total_elements = len(self.dataset())
        data = self.get_page(page, page_size)
        total_pages = math.ceil(total_elements / page_size)
        
        if page < total_pages:
            next_page = page + 1      
        else:
            next_page = None

        if page > 1:
            prev_page = page - 1
        else:
            prev_page = None
        
        return {
            'page': page,
            'page_size': len(data),
            'data': data,          
            'next_page': next_page,         
            'prev_page': prev_page,
            'total_pages': total_pages
        }
