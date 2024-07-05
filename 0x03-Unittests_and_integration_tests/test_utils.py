#!/usr/bin/env python3
"""import module"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json



class TestAccessNestedMap(unittest.TestCase):
    """class test access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
            ({}, ("a",)),
            ({"a": 1}, ("a", "b")),
        ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), repr(path[-1]))


class TestGetJson(unittest.TestCase):
    """ """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, expected):
        """ """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        expected.return_value = mock_response
        
        # Call the function with the test URL
        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        # Assert that the requests.get method was called with the correct URL
        expected.assert_called_once_with(test_url)
        
        
class TestMemoize(unittest.TestCase):
    """doc doc doc"""

    def test_memoize(self) -> None:
        """doc doc doc"""

        class TestClass:
            """doc doc doc"""

            def a_method(self) -> int:
                """doc doc doc"""
                return 42

            @memoize
            def a_property(self) -> int:
                """doc doc doc"""
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=42) as mocked:
            test_class = TestClass()
            self.assertEqual(test_class.a_property, 42)
            self.assertEqual(test_class.a_property, 42)
            mocked.assert_called_once()
