#!/usr/bin/env python3
"""
Simple helper function for pagination.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate a start index and an end index corresponding
    to the range of indexes to return in a list
    for those particular pagination parameters.
    
    Takes two integer arguments page and page_size.
    """

    return ((page - 1) * page_size, page * page_size)
