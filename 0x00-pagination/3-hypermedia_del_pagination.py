#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Get paginated data using seek pagination
        Deletion-resilient hypermedia pagination
        """
        keylist = list(range(index, index + page_size))
        fulldata = self.indexed_dataset()
        max_k = max(list(fulldata.keys()))
        assert isinstance(index, int) and index >= 0 and index <= max_k, \
            "invalid range"
        data = {k: fulldata[k] for k in keylist if k in fulldata}
        next_index = index + page_size
        while next_index < len(fulldata) and fulldata[next_index] is None:
            next_index += 1
        return {
                'index': index,
                'next_index': next_index,
                'page_size': len(data),
                'data': data
                }
