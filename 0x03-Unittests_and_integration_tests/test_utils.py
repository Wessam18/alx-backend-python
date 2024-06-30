#!/usr/bin/env python3
"""import module"""

import unittest
from parameterized import parameterized
access_nested_map = __import__('utils').access_nested_map
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)



class TestAccessNestedMap(unittest.TestCase):
    """class test access_nested_map"""
    @parameterized.expand ([
        ({"a": 1}, ("a",)),
        ({"a": {"b": 2}}, ("a",)),
        ({"a": {"b": 2}}, ("a", "b")),
    ])

    def test_access_nested_map(self, output) -> Any:
        """test access_nested_map"""
        self.assertEqual(access_nested_map, output)
