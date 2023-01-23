#!/usr/bin/env python3
"""function named index_range that takes two integer arguments page and page_size
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """retrieves the index range from a given page
    """
    end_index = page * page_size
    start_index = end_index - page_size
    return (start_index, end_index)
