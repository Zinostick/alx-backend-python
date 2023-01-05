#!/usr/bin/env python3
"""
Annotated function that returns the appropriate types
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    An iterable type
    """
    return [(i, len(i)) for i in lst]
