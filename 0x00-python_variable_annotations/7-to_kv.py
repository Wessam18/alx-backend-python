#!/usr/bin/env python3
"""import module"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return the sum of two floats"""
    return k, v**2
