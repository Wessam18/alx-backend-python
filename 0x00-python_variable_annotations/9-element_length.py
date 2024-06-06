#!/usr/bin/env python3
"""import module"""

from typing import List, Sequence, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return the sum of two floats"""
    return [(i, len(i)) for i in lst]
