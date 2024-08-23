#!/usr/bin/env python3
"""Extend Server class with more detailes about the data."""
from typing import List
import math
Server_ = __import__("1-simple_pagination").Server
index_range = __import__("0-simple_helper_function").index_range


class Server(Server_):
    """Server class to paginate a database of popular baby names."""

    def __init__(self):
        """Initialize"""
        super().__init__()

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get pages in the range."""

        start, end = index_range(page, page_size)
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        page_size = len(data)
        next_page = (page + 1) if page < total_pages else None
        prev_page = (page - 1) if page > 1 else None
        return {
                'page_size': page_size,
                'page': page,
                'data': data,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages
                }
