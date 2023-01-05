#!/usr/bin/env python3
"""
A type annotated function that returns a sum of floates
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Takes a list of floats as argument and returns
    their sum as a float
    """
    return float(sum(input_list))
