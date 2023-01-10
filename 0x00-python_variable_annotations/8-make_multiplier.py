#!/usr/bin/env python3
"""
A type annotated function that returns a function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    type-annotated function that a float multiplier
    and returns a funtion that multiplies a float by multiplier
    """
    def fn(n: float):
        return n * multiplier
    return fn
