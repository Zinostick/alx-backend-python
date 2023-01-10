#!/usr/bin/env python3
"""
A type annotated function which takes a list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    returns sum of a list in floates
    """
    return sum(mxd_lst)
