#!/usr/bin/env python3
"""import module"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return the sum of two floats"""
    def func(n: float) -> float:
        return multiplier * n
    return func
