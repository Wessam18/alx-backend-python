#!/usr/bin/env python3
"""import module"""
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """types of the elements"""
    if lst:
        return lst[0]
    else:
        return None
