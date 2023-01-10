#!/usr/bin/env python3
"""
A type annotated function that returns a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple. The first element of the tuple is the string k
    The second element is the square of the int/float v
    And should be annotated as a float
    """
    return (k, v * v)
