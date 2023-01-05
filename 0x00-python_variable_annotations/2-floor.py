#!/usr/bin/env python3
"""
A type annotated function which takes a float
and returns the floor of the float
"""


def floor(n: float) -> int:
    """
    Returns the floor of the argument n
    """
    return int(n // 1)
